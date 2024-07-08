# No release
# https://github.com/jlhutch/pylru.git
# Version 1.1.0 found on https://pypi.org/project/pylru/

# Steps

git clone https://github.com/jlhutch/pylru.git python-pylru-1.1.0
cd python-pylru-1.1.0
sed -i '1s/^/#\/usr\/bin\/env python\n/' setup.py
debmake -n -b ':py2'
dpkg-buildpackage -uc -b
