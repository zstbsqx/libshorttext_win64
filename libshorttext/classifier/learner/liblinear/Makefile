CXX ?= g++
CC ?= gcc
CFLAGS = -O3
LIBS = blas/blas.a
#LIBS = -lblas

all: train predict lib

lib: linear.o tron.o blas/blas.a
	$(CXX) -shared -m64 linear.o tron.o blas/blas.a -o liblinear.dll

train: tron.o linear.o train.c blas/blas.a
	$(CXX) $(CFLAGS) -o train train.c tron.o linear.o $(LIBS)

predict: tron.o linear.o predict.c blas/blas.a
	$(CXX) $(CFLAGS) -o predict predict.c tron.o linear.o $(LIBS)

tron.o: tron.cpp tron.h
	$(CXX) $(CFLAGS) -c -o tron.o tron.cpp

linear.o: linear.cpp linear.h
	$(CXX) $(CFLAGS) -c -o linear.o linear.cpp

blas/blas.a: blas/*.c blas/*.h
	make -C blas OPTFLAGS='$(CFLAGS)' CC='$(CC)';

clean:
	make -C blas clean
	make -C matlab clean
	rm -f tron.o linear.o train predict liblinear.dll
