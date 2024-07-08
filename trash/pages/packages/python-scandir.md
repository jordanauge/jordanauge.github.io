---
title: python-scandir
version: 1.9.0
pypi: https://pypi.org/project/scandir/
release: yes
github: https://github.com/benhoyt/scandir
---

wget https://github.com/benhoyt/scandir/archive/v1.9.0.tar.gz
tar xf v1.9.0.tar.gz
mv scandir-1.9.0/ python-scandir-1.9.0/
cd python-scandir-1.9.0/
debmake -n -b ':py2'
dpkg-buildpackage -uc -b
