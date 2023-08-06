from __future__ import annotations
from typing import AnyStr, NamedTuple
from subprocess import Popen, PIPE
from . import format as fmt


class SectionHeader(NamedTuple):
    name: str
    section_type: str
    address: int
    offset: int
    size: int

    @staticmethod
    def from_line(line: AnyStr) -> SectionHeader:
        # assume the line starts with "  [xx] " as in the output from readelf
        line = line[7:]
        # replace missing section names with a sensible default
        if line.startswith(" "):
            name = ""
            section_type, address, offset, size = line.split()[0:4]
        else:
            name, section_type, address, offset, size = line.split()[0:5]
        address = fmt.address_to_int(address)
        offset = fmt.address_to_int(offset)
        size = fmt.address_to_int(size)
        return SectionHeader(name, section_type, address, offset, size)

    def contains(self, file_offset: int) -> bool:
        """Check whether this section contains the given offset into the file"""
        return self.offset <= file_offset < (self.offset + self.size)


class SectionHeaderTable:

    def __init__(self, filename: AnyStr):
        self.filename = filename

        # Use `readelf` to read the section headers in the given file
        cmd = f"readelf -SW {filename}"
        p = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            raise RuntimeError(stderr.decode())

        # Convert lines into section headers, excluding the first row of column names
        lines = [line for line in stdout.decode().split("\n") if line.startswith('  [')][1:]
        self.headers = [SectionHeader.from_line(line) for line in lines]

    def __iter__(self):
        return iter(self.headers)

    def print(self):
        print("{0:<50s} {1:<18s} {2:<18s} {3:<18s} {4}".format("Name", "Type", "Address", "Offset", "Size"))
        for header in self.headers:
            print(f"{header.name:<50s} {header.section_type:<18s} 0x{header.address:0>16x} 0x{header.offset:0>16x} {header.size:>9}")

    def get_section_header(self, file_offset: int) -> SectionHeader:
        """Get the header for the section which contains the given offet into the file"""
        for sh in self:
            if sh.contains(file_offset):
                return sh
        raise KeyError(f"no section containing {file_offset=} was found")
