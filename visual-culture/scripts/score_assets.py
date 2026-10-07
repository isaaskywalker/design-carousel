"""Score manifest judgments; does not search, infer popularity, or clear rights."""
import json,sys
from pathlib import Path
WEIGHTS=dict(relevance=.35,recognizability=.20,recency=.15,composition_fit=.20,source_confidence=.10)
def evaluate(asset,mode):
    weights=WEIGHTS.copy()
    if mode=='timeless':
        weights['recency']=0
        total=sum(weights.values())
        weights={k:v/total for k,v in weights.items()}
    scores=asset['scores']
    for k,v in scores.items():
        if v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not 0<=v<=1):
            raise ValueError('Invalid score: '+k)
    if any(scores[k] is None for k in weights if weights[k]>0):
        return None,'pending'
    total=sum(weights[k]*scores[k] for k in weights if weights[k]>0)
    passed=total>=.70 and scores['relevance']>=.60 and scores['source_confidence']>=.50
    if mode=='latest':
        if not (asset.get('event_at') or asset.get('published_at')):
            return round(total,6),'pending'
        passed=passed and scores['recency']>=.60
    if asset['status'] in ('reference_only','failed') or asset['rights_status']=='restricted':
        return round(total,6),'reject'
    return round(total,6),'select' if passed else 'reject'
def score_manifest(manifest):
    for a in manifest['assets']:
        a['weighted_total'],a['decision']=evaluate(a,manifest['recency_mode'])
    return manifest
if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit('Usage: python score_assets.py input.json output.json')
    src,dest=map(Path,sys.argv[1:])
    if src.resolve()==dest.resolve():
        raise SystemExit('Use a different output path to preserve the input.')
    data=score_manifest(json.loads(src.read_text()))
    dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
