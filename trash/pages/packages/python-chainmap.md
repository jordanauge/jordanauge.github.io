---
title: python-chainmap
pypi: https://pypi.org/project/chainmap/
version: 1.0.2
release: 
---

# Steps

wget https://files.pythonhosted.org/packages/56/09/0f2f2e693bb102083b7e77fc2b7f97b9195dc4c90dcfa85038a2d128161b/chainmap-1.0.2.tar.gz
tar xf chainmap-1.0.2.tar.gz
mv chainmap-1.0.2 python-chainmap-1.0.2
cd python-chainmap-1.0.2
debmake -n -b ':py2'
dpkg-buildpackage -uc -b
