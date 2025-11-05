# Makefile for LaTeX Beamer presentation

MAIN = presentation
TEX = pdflatex
BIB = bibtex

.PHONY: all clean view

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex references.bib
	$(TEX) $(MAIN)
	$(BIB) $(MAIN)
	$(TEX) $(MAIN)
	$(TEX) $(MAIN)

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).nav $(MAIN).out $(MAIN).snm $(MAIN).toc
	rm -f $(MAIN).bbl $(MAIN).blg $(MAIN).synctex.gz
	rm -f $(MAIN).vrb $(MAIN).fls $(MAIN).fdb_latexmk

view: $(MAIN).pdf
	xdg-open $(MAIN).pdf 2>/dev/null || open $(MAIN).pdf 2>/dev/null || echo "Please open $(MAIN).pdf manually"

quick: $(MAIN).tex
	$(TEX) $(MAIN)

help:
	@echo "Available targets:"
	@echo "  all    - Full compilation with bibliography"
	@echo "  quick  - Quick compilation without bibliography"
	@echo "  clean  - Remove auxiliary files"
	@echo "  view   - Open PDF after compilation"
	@echo "  help   - Show this help message"