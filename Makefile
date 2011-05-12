# Targets
.PHONY: clean distclean docs ghdocs test runserver

# Initial vars

test: runserver
	/bin/bash ./test_run.sh
