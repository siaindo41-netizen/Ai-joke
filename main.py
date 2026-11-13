#!/usr/bin/env python3
"""ai-joke-03 entry: writes one original one-liner about AI coding agents.

The joke is a single fixed string (no randomness, no network, no I/O
besides the output file), so two runs always write the same bytes.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

JOKE = "My agent broke the build, then wrote a postmortem blaming my prompt."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
