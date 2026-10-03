# Sharal & Beyond

Open index.html in your browser. It contains the complete page, styling, notes and map images; no internet connection or server is required.

## Publish on an existing GitHub Pages site

Add index.html to a folder such as `world` in your existing Pages publishing source. Once your usual Pages deployment completes, the guide will appear under `/world/` on that site. Only index.html is needed for publication. Do not replace an existing homepage unless you intend to.

## Update the guide

Keep this folder as your editable source. Replace or edit `DnD World.md` using Obsidian, keeping `# Heading` for each main place or region. Run `python build.py` (or `py build.py` on Windows) to rebuild index.html, then upload the rebuilt page. The contents menu updates automatically. Python 3 is required only for rebuilding; no extra packages are required.

The lightweight converter supports the supplied note's headings, paragraphs and line breaks, plus subheadings. It does not implement all Markdown extensions. Styling and page layout live in template.html.

Dale's wording is retained without editorial changes. The page opens directly with the contents and map. “Sharal & Beyond” remains the browser-tab title.

## Map

`map-corrected.png` is the default map, with all requested place-name corrections. `DnD Map.jpeg` is the untouched original photograph. Both images are embedded in index.html. Use “Original photo” to switch to the photograph and “Back to map” to return, either on the page or in the full-size view. Keep both image files alongside build.py when rebuilding.
