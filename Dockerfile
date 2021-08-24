FROM archlinux

RUN pacman -Syu --noconfirm python3
WORKDIR /root
