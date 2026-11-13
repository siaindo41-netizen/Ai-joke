# ai-joke-03 entry

A Python 3.13 program (standard library only) that writes one original
one-liner about AI coding agents to `entry.txt` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, else `/output`).

The joke is a single fixed string: no randomness, no network, no input
besides the environment variable, so two runs always write the same bytes.
The output is UTF-8, 68 characters, with no trailing newline.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

License: MIT (see LICENSE).
