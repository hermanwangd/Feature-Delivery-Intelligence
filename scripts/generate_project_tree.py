from pathlib import Path
import sys
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
out=root/'PROJECT-TREE.txt'
ignore={'__pycache__','.pytest_cache','.git','.fdi-work'}
lines=[root.name+'/']

def walk(d,prefix=''):
    entries=[p for p in d.iterdir() if p.name not in ignore and p.name not in {'BUNDLE-MANIFEST.json','PROJECT-TREE.txt','VERIFICATION-SUMMARY.json'}]
    entries.sort(key=lambda p:(p.is_file(), p.name.lower()))
    for i,p in enumerate(entries):
        last=i==len(entries)-1
        branch='└── ' if last else '├── '
        lines.append(prefix+branch+p.name+('/' if p.is_dir() else ''))
        if p.is_dir(): walk(p,prefix+('    ' if last else '│   '))
walk(root)
out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(out)
