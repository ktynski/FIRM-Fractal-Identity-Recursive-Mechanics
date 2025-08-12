#!/bin/bash
echo "🔄 Testing LaTeX compilation..."
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode main.tex > compile_test_output.log 2>&1
if [ -f main.pdf ]; then
    echo "✅ SUCCESS: PDF generated successfully!"
    ls -la main.pdf
else
    echo "❌ FAILED: No PDF produced"
    echo "Last 20 lines of error log:"
    tail -20 compile_test_output.log
fi
