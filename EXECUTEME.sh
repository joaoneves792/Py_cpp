#! /bin/sh
#Compile c++ code into shared library (Using g++)
g++ -o mylib.so -shared -fPIC  mylib.cpp
#See that the symbols under extern "C" are not mangled:
nm mylib.so
#Have fun!
python3 ./py.py
