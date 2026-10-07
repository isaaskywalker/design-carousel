from pathlib import Path
import json
from jsonschema import Draft202012Validator
root=Path(__file__).resolve().parents[1]
for p in root.rglob('*.schema.json'):
    Draft202012Validator.check_schema(json.loads(p.read_text()))
for skill in ('visual-culture','design-carousel'):
    for p in (root/skill/'examples').glob('*.json'):
        names={'visual-strategy':'visual-strategy','brief':'carousel-brief','culture-dna':'visual-culture-dna','asset-manifest':'asset-manifest','slide-plan':'slide-plan','design-plan':'design-plan'}
        schema=root/skill/'schemas'/(names[p.stem]+'.schema.json')
        Draft202012Validator(json.loads(schema.read_text())).validate(json.loads(p.read_text()))
m=json.loads((root/'visual-culture/examples/asset-manifest.json').read_text())
ids=[a['id'] for a in m['assets']]
assert len(ids)==len(set(ids))
weights=dict(relevance=.35,recognizability=.20,recency=.15,composition_fit=.20,source_confidence=.10)
for a in m['assets']:
    vals=a['scores']
    active=[k for k in vals if not (m['recency_mode']=='timeless' and k=='recency')]
    if any(vals[k] is None for k in active):
        assert a['weighted_total'] is None and a['decision']!='select'
    else:
        w=weights.copy()
        if m['recency_mode']=='timeless':
            w['recency']=0; total=sum(w.values()); w={k:v/total for k,v in w.items()}
        assert abs(a['weighted_total']-sum(w[k]*vals[k] for k in w if w[k]>0))<1e-6
    if a['status']=='ready': assert Path(a['local_path']).is_file()
print('PASS: schemas, examples, IDs, score state, ready paths')
