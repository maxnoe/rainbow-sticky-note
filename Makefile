all: build/rainbow_notes.pdf rainbow.png


build/rainbow_notes.pdf: FORCE build/norainbow.pdf build/colormaps.pdf
	latexmk -norc -r latexmkrc rainbow_notes.tex 


build/%.pdf: plot_%.py | build
	python $<


build:
	mkdir -p build


rainbow.png: build/rainbow_notes.pdf
	pdftoppm -r 300 -singlefile -png $< > $@


clean:
	rm -rf build rainbow.png


.PHONY: all clean FORCE

FORCE:
