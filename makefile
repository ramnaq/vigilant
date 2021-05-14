# Python 3.8.5

PYTHON = python

help:
	@echo "--------------------HELP------------------"
	@echo "To run all .lcc examples, type 'make all'"
	@echo "To run example1.lcc, type 'make ex1'"
	@echo "To run example2.lcc, type 'make ex2'"
	@echo "To run example3.lcc, type 'make ex3'"
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

ex1:
	@echo 'Run example1.lcc'
	${PYTHON} main.py example1.lcc

ex2:
	@echo 'Run example2.lcc'
	${PYTHON} main.py example2.lcc

ex3:
	@echo 'Run example3.lcc'
	${PYTHON} main.py example3.lcc
