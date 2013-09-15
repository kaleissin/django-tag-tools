
clean:
	-find . -name '*.pyc' -exec rm -rf {} \;
	-find tagtools -type d -empty -exec rmdir {} \;
	-rm -rf dist
	-rm -rf build
	-rm -rf *.egg-info
