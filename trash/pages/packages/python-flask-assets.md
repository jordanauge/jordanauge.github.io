---
title: python-flask-assets
pypi: https://pypi.org/project/Flask-Assets/
version: 0.12
github: https://github.com/miracle2k/flask-assets
---

# Steps

wget https://github.com/miracle2k/flask-assets/archive/0.12.tar.gz
tar xf 0.12.tar.gz
mv flask-assets-0.12 python-flask-assets-0.12
cd python-flask-assets-0.12
sed -i '1s/^/#\/usr\/bin\/env python\n/' setup.py
mv Makefile Makefile.old
debmake -n -b ':py2'
sed -i "/Build-Depends/s/$/, dh-python/" debian/control 
dpkg-buildpackage -uc -b

