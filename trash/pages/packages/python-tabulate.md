wget  https://github.com/astanin/python-tabulate/archive/v0.8.5.tar.gz -O python-tabulate-0.8.5.tar.gz
tar xf python-tabulate-0.8.5.tar.gz
mv python-tabulate-0.8.5 python3-tabulate-0.8.5
cd python3-tabulate-0.8.5/
debmake -n -b ':py3'
deb_control_add_build_depend python3-nose # manual fix needed due to multiple lines
# Manually add python-nose too !!
sudo mk-build-deps -i
dpkg-buildpackage -uc -b
