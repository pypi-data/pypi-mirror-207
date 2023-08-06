from distutils.core import setup

with open("README.md", "r") as f:
    long_description = ''.join(f.readlines())

with open("LICENSE.md", "r") as g:
    license = ''.join(g.readlines())

setup(
    name='address_to_line',
    version='0.1.2',
    description='Convert addresses to source file and line number',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    author='Adam Tuft',
    packages=['address_to_line']
)
