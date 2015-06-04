AR     = ar rcv
RANLIB = ranlib 

HEADERS = blas.h blasp.h
FILES = dnrm2.o daxpy.o ddot.o dscal.o 

CFLAGS = $(OPTFLAGS) 
FFLAGS = $(OPTFLAGS)

blas: $(FILES) $(HEADERS)
	$(AR) blas.a $(FILES)  
	$(RANLIB) blas.a

clean:
	rm -f *.o *.a

.c.o:
	$(CC) $(CFLAGS) -m64 -c $*.c


