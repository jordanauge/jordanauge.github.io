# Home assistant

https://github.com/home-assistant/core/archive/0.111.2.zip
mkdir homeassistant-0.111.2
unzip 
debmake -n -b ':py3'
dpkg-buildpackage -uc -b

