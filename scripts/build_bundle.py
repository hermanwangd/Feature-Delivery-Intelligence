from pathlib import Path
import hashlib, json, zipfile, sys, os
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
output=Path(sys.argv[2]) if len(sys.argv)>2 else root.parent/(root.name+'-multica-handoff.zip')
ignore_names={'BUNDLE-MANIFEST.json'}
ignore_parts={'__pycache__','.pytest_cache','.git','.fdi-work'}

def files():
    out=[]
    for p in root.rglob('*'):
        if not p.is_file(): continue
        rel=p.relative_to(root)
        if any(part in ignore_parts for part in rel.parts): continue
        if rel.name in ignore_names: continue
        out.append(p)
    return sorted(out,key=lambda p:str(p.relative_to(root)).replace('\\','/'))

entries=[]
for p in files():
    rel=str(p.relative_to(root)).replace('\\','/')
    entries.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':p.stat().st_size})
manifest={'schema_version':'1.0','bundle':root.name,'files':entries}
(root/'BUNDLE-MANIFEST.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

# Fixed timestamp and sorted paths for deterministic ZIP.
zip_paths=files()+[root/'BUNDLE-MANIFEST.json']
zip_paths=sorted(zip_paths,key=lambda p:str(p.relative_to(root)).replace('\\','/'))
with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in zip_paths:
        rel=f"{root.name}/{str(p.relative_to(root)).replace(os.sep,'/')}"
        zi=zipfile.ZipInfo(rel,date_time=(2026,9,2,0,0,0))
        zi.compress_type=zipfile.ZIP_DEFLATED
        zi.external_attr=(0o100644 & 0xFFFF)<<16
        z.writestr(zi,p.read_bytes())
print(output)
print(hashlib.sha256(output.read_bytes()).hexdigest())
