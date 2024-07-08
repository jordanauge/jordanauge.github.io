---
title: python-awesome-slugify
pypi: https://pypi.org/project/awesome-slugify/
version: 1.6.5
git: https://github.com/dimka665/awesome-slugify
release: outdated
---

# Steps

git clone https://github.com/voronind/awesome-slugify.git python-awesome-slugify-1.6.5
cd python-awesome-slugify-1.6.5/
sed -i '1s/^/#\/usr\/bin\/env python\n/' setup.py
debmake -n -b ':py2'
dpkg-buildpackage -uc -b
