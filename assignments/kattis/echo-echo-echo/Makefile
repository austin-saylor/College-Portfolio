all:
	g++ -o echo echo.cpp

run:
	./echo

clean:
	rm -f *.o echo

test:
	cat 1.in | ./echo | diff - 1.ans
	cat 2.in | ./echo | diff - 2.ans