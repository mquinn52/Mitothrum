# Product video generator

`python3 render.py OUTDIR [slug ...]` renders one 1080×1920, 25-second video per
product in `products.json` (text and motion only, brand colors, platform safe
areas, on-screen affiliate disclosure for the whole video, silent audio track),
plus a cover image. Needs Python 3 with Pillow and NumPy, ffmpeg, and the Inter
font. To add a product, add an entry to `products.json` using only claims
already published on the site, with a "who should skip it" line.

Rendered videos aren't stored in the repository; captions and the posting
guide are delivered with each batch.
