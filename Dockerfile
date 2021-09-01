FROM archlinux

RUN pacman -Syu --noconfirm python3
COPY flashcards.py /root
WORKDIR /cpbox
