# `address_to_line`

Translate return addresses into source locations using the `readelf` and `addr2line` utilities from the [GNU Binutils](https://www.gnu.org/software/binutils/) package.

## Requirements

This package depends on the `readelf` and `addr2line` utilities from the [GNU Binutils](https://www.gnu.org/software/binutils/) package.

## Usage

Converting return addresses captured from within some process requires a copy of that process' `/proc/[pid]/maps` file.

### Command line:

```commandline
python3 -m address_to_line <proc_map_file> <addresses>
```

where `proc_map_file` is a copy of a process' `/proc/[pid]/maps` file and `addresses` is a text file containing 1 (hexaecimal) return address per line.

### Code:

```python
from address_to_line import resolve_source_locations
proc_map_file = "memory_map.txt" # The relevant /proc/[pid]/maps file
addresses_file = "addresses.txt" # Contains 1 (hexadecimal) return address per line
with open(addresses_file, "r") as f:
    addresses = [int(line, base=16) for line in f.readlines()]
# A list of named tuples of address, function, source file and line
source_locations = resolve_source_locations("memory_map.txt", addresses)
```
