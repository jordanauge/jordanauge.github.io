# Not the correct version ! master
git clone --recursive https://github.com/LibrePCB/LibrePCB.git librepcb-0.1 && cd librepcb-0.1
git submodule update --init --recursive

debmake -n

add_build_dep libcsfml-dev
sudo mk-build-deps -i
dpkg-buildpackage -uc -b


