.PHONY: run create-uml clean

PYTHON = python3
TEST_DIR = tests
VENV_DIR = venv
DOCS = docs
PLANTUML = java -jar ~/plantuml.jar
PIP = $(VENV_DIR)/bin/pip

$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

all: test run create-doc-folder create-docs create-uml clean

venv: clean
	@echo "Creating a new virtual environment..."
	python3 -m venv $(VENV_DIR)
	$(PIP) install -r requirements.txt
	touch $(VENV_DIR)/bin/activate
	@echo "Virtual environment rejuvenated."

run: $(VENV_DIR)/bin/activate
	$(PYTHON) convexpolygonarea.py

test: venv
	$(VENV_DIR)/bin/python $(TEST_DIR)/test_convexpolygonarea.py

create-doc-folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

# Create HTML docs
create-docs: create-doc-folder
	pdoc -o ./docs point.py polygon.py convexpolygonarea.py # creates .md docs inside docs
	@echo "html docs created and saved in $(DOCS)"

create-uml:
# use shell command which to check if java is installed and is in the $PATH
ifeq ($(shell which java), )
	$(error "No java found in $(PATH). Install java to run plantuml")
endif
# use wildcard function to check if file exists
ifeq ($(wildcard ~/plantuml.jar), )
	@echo "Downloading plantuml.jar in home folder..."
	curl -L -o ~/plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
endif
	$(PLANTUML) uml/Point.plantuml
	$(PLANTUML) uml/Polygon.plantuml
	$(PLANTUML) uml/Results.plantuml
	$(PLANTUML) uml/Solution.plantuml
	@echo "UML diagrams created and saved in uml folder"

clean:
	rm -rf __pycache__
	rm -rf $(VENV_DIR)