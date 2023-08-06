from .functions import resolve_source_locations


def check_depends():
    from shutil import which
    depends = ["readelf", "addr2line"]
    exists = [which(app) is not None for app in depends]
    missing = list()
    for app, found in zip(depends, exists):
        if not found:
            missing.append(app)
    if not all(exists):
        raise ImportError(f"""
***
*** Failed to find one or more dependencies on your path: {', '.join(missing)}.
*** Please install the GNU Binutils package (see https://www.gnu.org/software/binutils/)
***""")


check_depends()
del check_depends
