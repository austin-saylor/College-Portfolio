# compiler name
CXX = g++
# c++ compiler flags
# -g: adds debugging information to the executable file
# - Wall turns on most, but not  all, compiler warnings
# -std=C++17 uses c++17 standard
# add all the required flags separated by space
CXXFLAGS = -c -g -Wall -std=c++17

# the build target executable file; .exe is not required
PROGRAM = guess.exe

# list .cpp files separated by space
CPPFILES = main.cpp

# make build rule/default rule that'll be run when we run "make" or make build
# first compile each file to object file
# then make a single binary program
build:
	$(CXX) $(CXXFLAGS) $(CPPFILES)
	$(CXX) -o $(PROGRAM) *.o

run:
	./$(PROGRAM)
	
# make clean rule
# delete object and binary files
clean:
	rm -f $(PROGRAM) *.o

all: build run clean
	@printf "All done!\n"