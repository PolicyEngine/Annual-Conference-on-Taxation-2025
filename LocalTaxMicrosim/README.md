# Annual Conference on Taxation 2025

Beamer presentation: **Calibrating Survey and Administrative Data to Enable Local Tax Microsimulation**

## Files

- `presentation.tex` - Main LaTeX/Beamer presentation file
- `references.bib` - Bibliography file with citations
- `Makefile` - Build automation

## Compilation

### Using Make (Recommended)
```bash
make          # Full compilation with bibliography
make quick    # Quick compilation (no bibliography)
make clean    # Remove auxiliary files
make view     # Compile and open PDF
```

### Manual Compilation
```bash
pdflatex presentation
bibtex presentation
pdflatex presentation
pdflatex presentation
```

## Requirements

- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Beamer package
- Standard LaTeX packages: booktabs, amsmath, graphicx, natbib

### Installing LaTeX

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:**
Download MiKTeX from https://miktex.org/

## Customization

### Title Slide
Update author, institution, and date in lines 18-22 of `presentation.tex`

### Content
- Main findings and data are in the Results section
- Update revenue estimates with your actual numbers
- Add your PolicyEngine screenshots/charts where indicated

### Theme
Currently using Madrid theme with custom colors. To change:
- Line 2: Change theme with `\usetheme{[themename]}`
- Lines 11-13: Adjust colors

## Presentation Tips

1. **Practice with notes**: Use `\note{}` commands to add speaker notes
2. **Timing**: Aim for 15-20 slides for a 20-minute talk
3. **Backup slides**: Keep technical details in the appendix

## Troubleshooting

**Missing packages:** Install texlive-latex-extra or equivalent
**Bibliography issues:** Ensure bibtex runs between pdflatex compilations
**Font issues:** Install cm-super package for better font rendering