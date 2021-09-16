PYTHON = python3

.DEFAULT_GOAL = help

server:
	${PYTHON} server.py

client:
	${PYTHON} client.py

help:
	@echo "---------------HELP----------------------"
	@echo "To setup the server type ---- make server"
	@echo "To setup the client type ---- make client"
	@echo "-----------------------------------------"




