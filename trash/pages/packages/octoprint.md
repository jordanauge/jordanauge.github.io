# Package information

octoprint
v0.15+dev
https://github.com/foosel/OctoPrint.git
2018/11/22

# Steps

# Source: https://www.lesimprimantes3d.fr/forum/topic/4536-tuto-installer-octoprint-sur-une-raspbian/
git clone --depth 1 https://github.com/foosel/OctoPrint.git octoprint-0.15+dev
sed -i "s/flask.*/flask\",/g" setup.py
debmake -n -b ':py2'
cat debian/pydist-overrides <<EOF
awesome_slugify python-awesome-slugify
chainmap python-chainmap
emoji python-emoji
pylru python-pylru
sarge python-sarge
flask_login python-flask-login
flask_assets python-flask-assetss
EOF

cp scripts

## Packaging errors

1. package not installable

flask version -> commented version
scandir -> commented package
    but finally apt download from sid, and copied to repo

2. missing packages

I: dh_python2 tools:113: replacing shebang in debian/octoprint/usr/bin/octoprint
I: dh_python2 pydist:220: Cannot find package that provides flask_login. Please add package that provides it to Build-Depends or add "flask_login python-flask-login" line to debian/pydist-overrides or add proper  dependency to Depends by hand and ignore this info.
I: dh_python2 pydist:220: Cannot find package that provides flask_assets. Please add package that provides it to Build-Depends or add "flask_assets python-flask-assets" line to debian/pydist-overrides or add proper  dependency to Depends by hand and ignore this info.

# TODO

remove python3-all from build dependencies


# TODO manual after install

install python-tornado 4.5.3
