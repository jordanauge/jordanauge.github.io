wget https://pypi.python.org/packages/source/s/sarge/sarge-0.1.5.post0.tar.gz
tar xf sarge-0.1.5.post0.tar.gz
mv sarge-0.1.5.post0 python-sarge-0.1.5.post0
cd python-sarge-0.1.5.post0
sed -i '1s/^/#\/usr\/bin\/env python\n/' setup.py
debmake -n -b ':py2'

# Not needed anymore after the mv
#sed -i "/Package/s/sarge/python-&/" debian/control

dpkg-buildpackage -uc -b

