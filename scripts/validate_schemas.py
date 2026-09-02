import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
count=0
for p in sorted((root/'contracts').rglob('*.json')):
    Draft202012Validator.check_schema(json.loads(p.read_text(encoding='utf-8'))); count+=1
print(f'JSON Schemas: {count} PASS')
