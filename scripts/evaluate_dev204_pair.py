#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.dev204_validation import evaluate_dev204_gate


def main() -> None:
    parser = argparse.ArgumentParser(description='Evaluate one frozen DEV-204 RED/GREEN evidence pair.')
    parser.add_argument('--red', required=True)
    parser.add_argument('--green', required=True)
    args = parser.parse_args()
    red = json.loads(Path(args.red).read_text())
    green = json.loads(Path(args.green).read_text())
    print(json.dumps(evaluate_dev204_gate(red, green), sort_keys=True))


if __name__ == '__main__':
    main()
