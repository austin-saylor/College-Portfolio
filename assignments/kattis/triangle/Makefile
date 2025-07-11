# compiler name
CXX = g++
# c++ compiler flags
# -g : adds debugging information to the executable file
# -Wall : turns on most, but not  all, compiler warnings
# -std=C++17 : uses c++17 standard
# put all the required flags separated by space
CXXFLAGS = -c -g -Wall -std=c++17

PROGRAM = triangle_area.exe

# list .cpp files separated by space
CPPFILES = main.cpp

# make build rule/default rule that'll be run when we run "make"
# first compile each file to object file
# then make a single binary program
all:
	$(CXX) $(CXXFLAGS) $(CPPFILES)
	$(CXX) -o $(PROGRAM) *.o

run:
	./$(PROGRAM)
	
# make clean rule
# delete object and binary files
clean:
	rm -f $(PROGRAM) *.o

test:
	@echo "diff doesn't work correctly on floating point numbers, e.g. 5.0 and 5.0000000 are different!"
	@echo "stick to unit testing!"