# compiler name
CXX = g++
# g++ compiler flags
# -g: adds debugging information to the executable file
# -Wall: turns on most, but not  all, compiler warnings
# -std=c++17: uses c++17 standard
# put all the required flags separated by space
CXXFLAGS = -c -g -Wall -std=c++17

# the build target executable file; .exe is not required
PROGRAM = shapes

# list .cpp files separated by space
CPPFILES = shapes.cpp

# make all rule/default rule that'll be run when we run "make"
# first compile each file to object file
# then make a single binary/executable program
all:
	$(CXX) $(CXXFLAGS) $(CPPFILES)
	$(CXX) -o $(PROGRAM) $(CPPFILES)

# make clean rule
# delete object and binary files
clean:
	rm -f $(PROGRAM) *.o

# FIXME #fixed#
# add a rule to run the program

run:
	./$(PROGRAM)