#

```
#git clone git@github.com:platformio/platformio-core.git
wget https://github.com/platformio/platformio-core/archive/v3.6.7.tar.gz

tar xf v3.6.7.tar.gz
cd platformio-core-3.6.7

debmake -n -b ':py3'
. ../../package_helper.sh

# The Makefile would call the following tools but we disable it for the build
mv Makefile Makefile.old
#deb_control_add_build_depend pylint
#deb_control_add_build_depend isort
#deb_control_add_build_depend yapf

sed -i 's/click>=5,<6/click>=5/' setup.py

# ./package_parse_deps.py
bottle - OK (version=0.12.15-2, specifier=<0.13)
click - OK (version=7.0-1, specifier=>=5)
colorama - OK (version=0.3.7-1, specifier=)
pyserial - OK (version=3.4-4, specifier=!=3.3,<4,>=3)
requests - OK (version=2.21.0-1, specifier=<3,>=2.4.0)
semantic_version - OK (version=2.6.0-2, specifier=<3,>=2.5.0)
python3-bottle
python3-click
python3-colorama
python3-serial
python3-requests
python3-semantic-version

# Only python2 seems to be working for platformio, so python deps
deb_add_depend python-bottle
...

deb_build
```

TODO: dependencies

```
(jordan@adreena)(~/repos/perso/packages/python/platformio-core-3.6.7) ./package_parse_deps.py
['bottle<0.13', 'click>=5,<6', 'colorama', 'pyserial>=3,<4,!=3.3', 'requests>=2.4.0,<3', 'semantic_version>=2.5.0,<3']
```

TODO: check file 99-platformio-udev.rules

================================================================================
NEW RELEASE 4.0.3

wget https://github.com/platformio/platformio-core/archive/v4.0.3.tar.gz -O platformio-core-4.0.3.tar.gz
tar xf platformio-core-4.0.3.tar.gz
cd platformio-core-4.0.3
debmake -n -b ':py3'
. ../../package_helper.sh
deb_control_add_depend python3-tabulate
# python3-tabulate (>=0.8.3), python3-tabulate (<1.0)
dpkg-buildpackage -uc -b



# Inspecting dependencies

    "bottle<0.13",
    "click>=5,<8",
    "colorama",
    "pyserial>=3,<4,!=3.3",
    "requests>=2.4.0,<3",
    "semantic_version>=2.8.1,<3",
    "tabulate>=0.8.3,<1"

../package_parse_deps.py 
bottle - OK (version=0.12.15-2, specifier=<0.13)
click - OK (version=7.0-2, specifier=<8,>=5)
colorama - OK (version=0.4.1-1, specifier=)
pyserial - OK (version=3.4-4, specifier=!=3.3,<4,>=3)
requests - OK (version=2.21.0-1, specifier=<3,>=2.4.0)
semantic_version - OK (version=2.8.2-2, specifier=<3,>=2.8.1)
tabulate - Wrong version (version=0.8.2-1.1, specifier=<1,>=0.8.3)
python3-bottle
python3-click
python3-colorama
python3-serial
python3-requests
python3-semantic-version
python3-tabulate

# We have rebuilt tabulate

Depends: ${misc:Depends}, ${python3:Depends}, python3-bottle (<0.13), python3-click (>=5), python3-click (<8), python3-colorama, python3-serial (>=3), python3-serial (<4), python3-serial(!=3.3), python3-requests (>=2.4.0), python3-requests (<3) python3-semantic-version (>=2.8.1), python3-semantic-version (<3), python3-tabulate (>=0.8.3), python3-tabulate (<1.0)

!= not working

Depends: ${misc:Depends}, ${python3:Depends}, python3-bottle (<<0.13), python3-click (>=5), python3-click (<<8), python3-colorama, python3-serial (>=3), python3-serial (<<3.3), python3-serial (>>3.3),  python3-serial (<<4), python3-requests (>=2.4.0), python3-requests (<<3), python3-semantic-version (>=2.8.1), python3-semantic-version (<<3), python3-tabulate (>=0.8.3), python3-tabulate (<<1.0)

CF: https://www.debian.org/doc/debian-policy/ch-relationships.html

not working either

Conflicts: python3-serial (=3.3)


# issue : package is built using python2

dh_auto_install: Please use the third-party "pybuild" build system instead of python-distutils
dh_auto_install: This feature will be removed in compat 12.
pyversions: missing X(S)-Python-Version in control file, fall back to debian/pyversions
pyversions: missing debian/pyversions file, fall back to supported versions


change shebang line of setup.py to python3 before using debmake

(jordan@adreena)(~) pio run
Please wait while upgrading PlatformIO...
PlatformIO has been successfully upgraded to 4.0.3!


# TODO

https://docs.platformio.org/en/latest/faq.html#platformio-udev-rules





## Version 5.2.5

wget https://github.com/platformio/platformio-core/archive/refs/tags/v5.2.5.tar.gz -O platformio-core-5.2.5.tar.gz
tar xf platformio-core-5.2.5.tar.gz
cd platformio-core-5.2.5/
 . ~/repos/perso/packages/package_helper.sh
 
deb_control_add_depend python3-tabulate
# python3-tabulate (>=0.8.3), python3-tabulate (<1.0)

copy deps
add pylint
sudo mk-build-deps -i

dpkg-buildpackage -uc -b


pylint fails due to missing deps:
install manually
sudo apt install python3-semantic-version python3-jsondiff
... or make them build deps!!


mv Makefile Makefile.old should solve the pylint problem
