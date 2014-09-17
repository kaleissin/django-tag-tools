
clean:
	-rm -rf dist
	-rm -rf build
	-rm -rf *.egg-info
	-find . -name '*.pyc' -exec rm -rf {} \;
	-find tagtools -type d -empty -exec rmdir {} \;
