#!/bin/sh

make distclean
./configure --prefix=/usr/local/popcorn/aarch64 --target=aarch64-linux-gnu --enable-debug --enable-gcc-wrapper --enable-optimize --disable-shared CC=/usr/local/popcorn/bin/clang CFLAGS='-target aarch64-linux-gnu -popcorn-alignment'
cp include/musl_pthread.h include/pthread.h
make -j16
cp include/gnu-pthread.h include/pthread.h
make install