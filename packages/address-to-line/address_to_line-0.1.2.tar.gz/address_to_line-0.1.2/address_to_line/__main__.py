from . import resolve_source_locations
import sys


def main():
    maps_file = sys.argv[1]
    address_file = sys.argv[2]
    with open(address_file, "r") as f:
        lines = f.readlines()
    addresses = [int(line, base=16) for line in lines]
    results = resolve_source_locations(maps_file, addresses)

    print("source files:")
    unique_files = list({s.file for s in results})
    for file in unique_files:
        print(f"{file}")

    print()
    print("source locations:")
    for s in results:
        print(s)


if __name__ == "__main__":
    main()
