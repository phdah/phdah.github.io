# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   = python3.10 -msphinx
SOURCEDIR     = .
BUILDDIR      = _build



# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

gen-module:
	@sphinx-apidoc -o ./modules ./pipelines/lib/pipelines

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) && cp -r ./$(BUILDDIR)/html ./docs

build: gen-module html

port-forward:
	@python3 -m http.server 8080 --directory ./$(BUILDDIR)/html
