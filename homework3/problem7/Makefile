# $UWHPSC/codes/fortran/newton/Makefile

OBJECTS = functions.o newton.o test1.o
OBJECTS2 = functions.o newton.o test_quartic.o
MODULES = functions.mod newton.mod

FFLAGS = -g

.PHONY: test1 clean test_quartic 

test1: test1.exe
	./test1.exe

test1.exe: $(MODULES) $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test1.exe

test_quartic: test_quartic.exe
	./test_quartic.exe

test_quartic.exe: $(MODULES) $(OBJECTS2)
	gfortran $(FFLAGS) $(OBJECTS2) -o test_quartic.exe



%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

%.mod: %.f90
	gfortran $(FFLAGS) -c $<

clean:
	rm -f *.o *.exe *.mod

