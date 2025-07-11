.PHONY: run clean

PYTHON = python3
TEST_DIR = tests
VENV_DIR = venv
PIP = $(VENV_DIR)/bin/pip

$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

all: test run clean

venv: clean
	@echo "Creating a new virtual environment..."
	python3 -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt
	touch $(VENV_DIR)/bin/activate
	@echo "Virtual environment rejuvenated."

run: $(VENV_DIR)/bin/activate
	$(PYTHON) sorttwonumbers.py

test: venv
	$(VENV_DIR)/bin/python $(TEST_DIR)/test_sorttwonumbers.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV_DIR)