USER := $(shell whoami)

# Append username to the venv path to avoid collisions
VENV = venv/horizons_$(USER)
PYTHON = ${VENV}/bin/python3
PIP = ${VENV}/bin/pip
all: venv install

venv:
	python3 -m venv ${VENV}

# Run the following to activate the Python Virtual Environment
activate:
	@echo . ./${VENV}/bin/activate

# Prerequisites libldap2-dev libsasl2-dev libssl-dev
install: venv
	${PIP} install --upgrade pip
	${PIP} install -r requirements

