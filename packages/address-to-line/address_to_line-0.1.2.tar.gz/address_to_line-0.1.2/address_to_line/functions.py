from typing import Tuple, Dict, List, NamedTuple
from collections import defaultdict
from .maps import MemoryMap
from .sections import SectionHeaderTable
import subprocess


class SourceLocation(NamedTuple):
    address: int
    function: str
    file: str
    line: int

    def __repr__(self):
        return f"0x{self.address:0>16x} is {self.file}:{self.line} ({self.function})"


def address_to_offset(memory_map: MemoryMap, section_header_table: Dict[str, SectionHeaderTable], address: int) -> Tuple[str, str, int]:
    # Get the region which contains the address of interest
    region = memory_map.get_region(address)

    # Calculate the offset into the file of this address
    offset_into_file = region.offset_into_file(address)

    # Get the section headers for the file which backs the relevant memory region
    ht = section_header_table[region.filename]

    # Get the header for the section in the file which contains the offset
    sh = ht.get_section_header(offset_into_file)

    # The address relative to the start of the section i.e. the offset into the section containing the address
    pc_offset = offset_into_file - sh.offset

    return sh.name, region.filename, pc_offset


def resolve_source_locations(maps_file: str, addresses: List[int]) -> List[SourceLocation]:
    memory_map = MemoryMap(maps_file)
    section_header_table = {filename: SectionHeaderTable(filename) for filename in memory_map.distinct_filenames()}
    collected_addresses = defaultdict(list)
    source_locations: List[SourceLocation] = list()
    for address in addresses:
        section_name, binary_file, offset = address_to_offset(memory_map, section_header_table, address)
        collected_addresses[(binary_file, section_name)].append((f"{offset:x}", address))
    for (binary_file, section_name), values in collected_addresses.items():
        offsets, return_addresses = list(map(list, zip(*values)))
        cmd = f"addr2line -fC -j {section_name} -e {binary_file} {' '.join(offsets)}"
        proc = subprocess.run(cmd.split(), capture_output=True)
        stdout = proc.stdout.decode()
        lines = iter(stdout.split("\n"))
        for address in return_addresses:
            function_name = next(lines)
            source_location = next(lines)
            source_file, line = source_location.split(":")
            line = None if line == "?" else int(line)
            source_locations.append(SourceLocation(address, function_name, source_file, line))
    return source_locations
