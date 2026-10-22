#!/usr/bin/env python3
"""Restore the approved cover PDFs losslessly before Quarto renders."""
import json
from materialize_fispm_downloads import ROOT, assemble

if __name__ == '__main__':
    for manifest in json.loads((ROOT / 'data/pm-cover-downloads/manifest.json').read_text()):
        assemble(manifest)
