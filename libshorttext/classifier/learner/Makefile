all = lib
TARGET = util

all: lib  test
	make -C liblinear

test: util.c
	g++ -Iliblinear test.cpp -o test

lib: ${TARGET}.o
	gcc -shared -m64 ${TARGET}.o -o ${TARGET}.dll

${TARGET}.o: ${TARGET}.c
	gcc -Iliblinear -O3 -m64 -c -o ${TARGET}.o ${TARGET}.c

clean:
	rm -rf ${TARGET}.o ${TARGET}.dll *.pyc test
	make -C liblinear clean
