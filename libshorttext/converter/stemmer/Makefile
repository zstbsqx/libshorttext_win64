all = lib

lib: porter.o
	gcc -shared -m64 porter.o -o porter.dll

porter.o: porter.c
	gcc -O3 -m64 -c -o porter.o porter.c

clean:
	rm -f porter.o porter.dll *.pyc
