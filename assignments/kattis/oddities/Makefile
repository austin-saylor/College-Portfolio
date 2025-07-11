all:
	g++ -o main main.cpp

run:
	./main

clean:
	rm -f *.o main

test:
	cat 1.in | ./main | diff - 1.ans