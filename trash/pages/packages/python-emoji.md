git clone https://github.com/carpedm20/emoji.git python-emoji-0.5.1
debmake -n -b ':py2'
dpkg-buildpackage -uc -b
