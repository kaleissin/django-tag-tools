
clean:
	-rm -rf dist
	-rm -rf build
	-rm -rf *.egg-info
	-rm -rf django_tag_tools.egg-info
	-find . -name __pycache__ -type d -exec rm -rf {} \; -prune
	-find . -name '*.pyc' -exec rm -rf {} \;
	-find tagtools -type d -empty -exec rmdir {} \; -prune
