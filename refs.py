# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:47:46 2021

@author: danaukes
"""

import re
import yaml
import os
import json
import subprocess

subprocess.run('pandoc-citeproc -y bibliography.bib > bib.yaml',shell=True)

# path0 = '~/websites/website_hugo_framework/content'
path0 = '../content'
path0 = os.path.normpath(os.path.expanduser(path0))

search = re.compile('\{\{ *< *cite "([a-zA-Z0-9]*)" *>\}\}')

all_files = []
all_refs = []

for path,dirs,files in os.walk(path0):
    # print('path:',path,'dirs:',dirs,'files:',files)
    
    for file in files:
        if os.path.splitext(file)[1]=='.md':
            all_files.append(os.path.join(path,file))

for file in all_files:
    # if 'foldable-background' in file:
    # print(file)
    with open(file,'rb') as f:
        sb=f.read()
    s = sb.decode()
    
    results = re.findall(search, s)
    all_refs.extend(results)

all_refs = [item for item in all_refs if len(item)>0]
all_refs = list(set(all_refs))                
all_refs.sort()

# with open(file,'rb') as f:
    # sb=f.read()
    
    
path = './refs.yaml'    
path = os.path.normpath(os.path.expanduser(path))

with open(path,'w') as f:
    yaml.dump(all_refs,f)
    
path2 = './bib.yaml'    
path2 = os.path.normpath(os.path.expanduser(path2))
    
with open(path2,'rb') as f:
    tb = f.read()
# t = tb.decode('utf-16-le')
t = tb.decode()
# try:
y = yaml.load(t,Loader=yaml.Loader)
# except Exception as e:
    # print(e)
    # json.load(f)

my_y = []
for item in all_refs:
    for ref in y['references']:
        if ref['id']==item:
            ref['abstract']=""
            issued = []
            try:
                for item in ref['issued']:
                    issued1=[]
                    try:
                        issued1.append(item['year'])
                    except KeyError:
                        issued1.append(1)
                    try:
                        issued1.append(item['month'])
                    except KeyError:
                        issued1.append(1)
                    try:
                        issued1.append(item['day'])
                    except KeyError:
                        issued1.append(1)
                    issued.append(issued1)
                ref['issued']={}
                ref['issued']['date-parts'] = issued
            except KeyError:
                pass
            my_y.append(ref)

path3 = '../data/bib.json'    
path3 = os.path.normpath(os.path.expanduser(path3))

with open(path3,'w') as f:
    json.dump(my_y, f,sort_keys=True,indent=True)
