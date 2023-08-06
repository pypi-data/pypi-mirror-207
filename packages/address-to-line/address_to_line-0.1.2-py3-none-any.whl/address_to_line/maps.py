from __future__ import annotations
from typing import Iterable, AnyStr, NamedTuple
from . import format as fmt


class MemoryRegion(NamedTuple):
    address_low: int   # start of the memory region
    address_high: int  # uppermost address of the region
    permissions: str   # permissions flags
    file_offset: int   # offset into the file of the section which this region maps
    device: str
    inode: str
    filename: str      # the file mapped by this region

    @staticmethod
    def from_line(line: AnyStr) -> MemoryRegion:
        """Parse a line from a /proc/[pid]/maps file as a MemoryRegion"""
        sections = line.split()
        num_sections = len(sections)
        assert(num_sections == 6 or num_sections == 5)
        filename = sections[5] if num_sections == 6 else ""
        memory_bound, permissions, offset, device, inode = sections[0:5]
        file_offset = fmt.address_to_int(offset)
        address_low, address_high = (fmt.address_to_int(value) for value in memory_bound.split("-"))
        return MemoryRegion(address_low, address_high, permissions, file_offset, device, inode, filename)

    def contains(self, address: int) -> bool:
        """Check whether this memory region contains the given address"""
        return self.address_low <= address <= self.address_high

    def offset(self, address: int) -> int:
        """Calculate the offset into this memory region of the given address"""
        assert(self.contains(address))
        return address - self.address_low

    def offset_into_file(self, address: int) -> int:
        """Calculate the offset of an address into the file mapped by this region"""
        assert(self.contains(address))
        return self.offset(address) + self.file_offset

    def backed_by_file(self) -> bool:
        """Check whether this region is backed by a file"""
        return self.filename.startswith("/")


class MemoryMap:

    def __init__(self, filename: AnyStr):
        self.filename = filename
        with open(filename, 'r') as f:
            self.regions: Iterable[MemoryRegion] = [MemoryRegion.from_line(line) for line in f.readlines()]

    def __iter__(self) -> Iterable[MemoryRegion]:
        return iter(self.regions)

    def get_region(self, address: int) -> MemoryRegion:
        """Get the region which contains the address"""
        for region in self.regions:
            if region.contains(address):
                return region
        raise KeyError(f"address {address} not found")

    def distinct_filenames(self) -> Iterable[AnyStr]:
        """List the unique files backing the memory regions in this map"""
        return list(set(region.filename for region in self if region.backed_by_file()))
