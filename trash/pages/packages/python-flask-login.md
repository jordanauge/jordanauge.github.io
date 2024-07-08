---
title: python-flask-login
version: 0.4.1
pypi: https://pypi.org/project/Flask-Login/
github: https://github.com/maxcountryman/flask-login
release: yes
---

apt install python-nose python-nose-yanc python-semantic-version

wget https://github.com/maxcountryman/flask-login/archive/0.4.1.tar.gz
tar xf 0.4.1.tar.gz
mv flask-login-0.4.1 python-flask-login-0.4.1
cd python-flask-login-0.4.1
mv Makefile Makefile.old # so that pybuild properly used
debmake -n -b ':py2'
sed -i "/Build-Depends/s/$/, python-nose, python-nose-yanc, python-semantic-version/" debian/control
dpkg-buildpackage -uc -b

