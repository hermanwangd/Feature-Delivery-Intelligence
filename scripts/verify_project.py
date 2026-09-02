import hashlib,json,sys
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
manifest=json.loads((root/'BUNDLE-MANIFEST.json').read_text(encoding='utf-8'))
expected={x['path']:x['sha256'] for x in manifest['files']}
ignored={'BUNDLE-MANIFEST.json'}
ignored_parts={'__pycache__','.pytest_cache','.git','.fdi-work'}
actual={str(p.relative_to(root)).replace('\\','/') for p in root.rglob('*') if p.is_file() and not any(part in ignored_parts for part in p.relative_to(root).parts) and str(p.relative_to(root)).replace('\\','/') not in ignored}
fail=[]
for rel,dig in expected.items():
    p=root/rel
    if not p.exists(): fail.append('missing '+rel); continue
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got!=dig: fail.append('digest '+rel)
extra=sorted(actual-set(expected))
if extra: fail += ['unexpected '+x for x in extra]
for x in fail: print('FAIL',x)
if fail: raise SystemExit(1)
print(f'Manifest: {len(expected)} files / 0 failures / 0 unexpected')
