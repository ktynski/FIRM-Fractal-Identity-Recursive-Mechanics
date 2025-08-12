#!/bin/bash
echo "Compiling FIRM paper..."
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex  
pdflatex -interaction=nonstopmode main.tex
echo "Compilation complete!"
ls -la main.pdf