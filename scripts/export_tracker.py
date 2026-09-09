"""Export live issues and capture requests. Raw capture data stays private."""
from pathlib import Path
import csv
import json
import os
import re
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
REPOSITORY='WoWHellgarve-HolyDeeW/WoWHellgarve-Bugtracker'

def api_get(endpoint):
    headers={'Accept':'application/vnd.github+json','User-Agent':'WoWHellgarve-QA-export','X-GitHub-Api-Version':'2022-11-28'}
    token=os.environ.get('GITHUB_TOKEN')
    if token: headers['Authorization']='Bearer '+token
    request=urllib.request.Request('https://api.github.com/repos/'+REPOSITORY+endpoint,headers=headers)
    with urllib.request.urlopen(request,timeout=40) as response:return json.load(response)

def write_csv(path,headers,rows):
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('w',encoding='utf-8',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(headers)
        for row in rows:
            writer.writerow(["'"+x if isinstance(x,str) and x.startswith(('=','+','-','@')) else x for x in row])

def main():
    # Only maintainers assign stable local IDs. Public issue text cannot replace
    # another report's identity or redirect an existing coverage link.
    identity_map=json.loads((ROOT/'config/issue-map.json').read_text(encoding='utf-8'))
    by_number={entry['number']:ident for ident,entry in identity_map.items()}
    if len(by_number)!=len(identity_map):raise RuntimeError('Duplicate issue mapping')
    issues=[]
    for page in range(1,101):
        batch=api_get(f'/issues?state=all&per_page=100&page={page}')
        issues.extend(x for x in batch if 'pull_request' not in x)
        if len(batch)<100:break
    else:raise RuntimeError('Pagination limit reached; refusing a partial export')
    issues.sort(key=lambda x:x['number'])
    rows=[];request_rows=[];by_local={}
    for issue in issues:
        labels=[x['name'] for x in issue['labels']]
        def values(prefix):return '; '.join(sorted(x[len(prefix):] for x in labels if x.startswith(prefix)))
        text=issue.get('body') or ''
        ident=by_number.get(issue['number'],'GH-'+str(issue['number']))
        cov=re.search(r'\bCOV-\d+\b',text)
        coverage=cov.group(0) if cov else ''
        assignees='; '.join(x['login'] for x in issue['assignees'])
        row=[ident,issue['number'],issue['title'],issue['state'],values('status:'),values('priority:'),values('cause:'),values('evidence:'),assignees,coverage,issue['updated_at'],issue['html_url']]
        rows.append(row);by_local[ident]={'url':issue['html_url'],'state':issue['state'],'status':values('status:')}
        if 'kind:capture' in labels:
            request_rows.append([ident,coverage,issue['title'],values('priority:'),values('status:'),assignees,issue['state'],issue['updated_at'],issue['html_url']])
    write_csv('reports/issues.csv',['Local ID','Issue','Title','GitHub state','Workflow status','Priority','Cause','Evidence','Assigned to','Coverage ID','Updated UTC','GitHub URL'],rows)
    write_csv('coverage/requests.csv',['Request ID','Coverage ID','Subject','Priority','Workflow status','Assigned to','GitHub state','Updated UTC','GitHub URL'],request_rows)
    coverage_file=ROOT/'coverage/scenarios.csv'
    with coverage_file.open(encoding='utf-8',newline='') as stream:
        reader=csv.DictReader(stream);headers=list(reader.fieldnames);coverage_rows=list(reader)
    for name in ['Bug URL','Current issue status','Capture request URL']:
        if name not in headers:headers.append(name)
    for row in coverage_rows:
        bug=by_local.get(row['Bug ID'],{})
        request=by_local.get(row['Capture request ID'],{})
        row['Bug URL']=bug.get('url','')
        row['Current issue status']=bug.get('status','')
        row['Capture request URL']=request.get('url','')
    write_csv('coverage/scenarios.csv',headers,[[row.get(h,'') for h in headers] for row in coverage_rows])
    print(json.dumps({'issues':len(rows),'captureRequests':len(request_rows),'coverageScenarios':len(coverage_rows)}))

if __name__=='__main__':main()
