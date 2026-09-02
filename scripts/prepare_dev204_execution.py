#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime.dev204_validation import prepare_all_execution_packets


def main() -> None:
    parser = argparse.ArgumentParser(description='Prepare frozen DEV-204 RED/GREEN agent packets and reviewer-only rubrics.')
    parser.add_argument('--scenario-pack', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    result = prepare_all_execution_packets(Path(args.scenario_pack), Path(args.output_dir))
    result['claim_boundary'] = 'PACKETS_PREPARED_NOT_EXECUTED'
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
