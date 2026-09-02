#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, sys
import yaml


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def validate_recovery(root: Path) -> list[str]:
    errors=[]
    current=(root/'governance'/'CURRENT').read_text(encoding='utf-8').strip()
    cand=root/'governance'/'baselines'/'GB-0001-CANDIDATE.yaml'
    if current != 'NONE':
        errors.append(f'recovery workspace expected CURRENT=NONE, got {current!r}')
    if not cand.exists():
        errors.append('missing GB-0001-CANDIDATE.yaml')
        return errors
    data=yaml.safe_load(cand.read_text(encoding='utf-8'))
    if data.get('status') != 'CANDIDATE': errors.append('candidate baseline status must be CANDIDATE')
    if not str(data.get('promotion_state','')).startswith('BLOCKED_'): errors.append('recovery candidate must remain promotion-blocked')
    for m in data.get('modules',[]):
        if m.get('byte_identity') == 'VERIFIED' and not m.get('sha256') and not m.get('tree_sha256'):
            errors.append(f"{m.get('id')}: VERIFIED byte identity without digest")
        if m.get('local_path'):
            p=root/m['local_path']
            if not p.exists(): errors.append(f"{m.get('id')}: local path missing: {m['local_path']}")
    return errors


def validate_approved(root: Path) -> list[str]:
    errors=[]
    current=(root/'governance'/'CURRENT').read_text(encoding='utf-8').strip()
    if not current or current == 'NONE': return ['no approved CURRENT baseline']
    path=root/'governance'/'baselines'/f'{current}.yaml'
    if not path.exists(): return [f'CURRENT baseline file missing: {path.name}']
    data=yaml.safe_load(path.read_text(encoding='utf-8'))
    if data.get('status') != 'APPROVED': errors.append('CURRENT baseline status is not APPROVED')
    for m in data.get('modules',[]):
        lp=m.get('local_path'); expected=m.get('sha256')
        if not lp or not expected:
            errors.append(f"{m.get('id')}: missing local_path/sha256")
            continue
        p=root/lp
        if not p.exists(): errors.append(f"{m.get('id')}: missing file {lp}"); continue
        actual=sha256(p)
        if actual != expected: errors.append(f"{m.get('id')}: digest mismatch")
        if m.get('classification') == 'CANDIDATE': errors.append(f"{m.get('id')}: candidate selected by approved baseline")
    return errors


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root', nargs='?', default='.')
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--expect-recovery-blocked', action='store_true')
    g.add_argument('--require-approved', action='store_true')
    a=ap.parse_args()
    root=Path(a.root)
    errors=validate_recovery(root) if a.expect_recovery_blocked else validate_approved(root)
    for e in errors: print('FAIL', e)
    if errors: return 1
    print('PASS recovery candidate is safely blocked' if a.expect_recovery_blocked else 'PASS approved baseline verified')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
