help:
	@echo "--------------------HELP------------------"
	@echo "To run all .lcc examples, type 'make all'"
	@echo "------------------------------------------"

all:
	@echo 'Run example1.lcc'
	python main.py example1.lcc
	@echo
	@echo 'Run example2.lcc'
	python main.py example2.lcc
	@echo
	@echo 'Run example3.lcc'
	python main.py example3.lcc

