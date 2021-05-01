# Python 3.8.5

PYTHON = python

help:
	@echo "--------------------HELP------------------"
	@echo "To run all .lcc examples, type 'make all'"
	@echo "------------------------------------------"

all:
	@echo 'Run example1.lcc'
	${PYTHON} main.py example1.lcc
	@echo
	@echo 'Run example2.lcc'
	${PYTHON} main.py example2.lcc
	@echo
	@echo 'Run example3.lcc'
	${PYTHON} main.py example3.lcc
	@echo 'Run example4.lcc'
	${PYTHON} main.py example4.lcc

