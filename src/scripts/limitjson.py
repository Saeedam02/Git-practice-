import json
from pathlib import Path
def read_json(file):
    with open(file,'r') as f :
        data=json.load(f)
        return data
    
# the following func is used to write inside of a file
def write_json(data,file):
    with open(file,'w') as f:
        json.dump(data,f,indent=4)
    
data=read_json(Path('./data/result.json'))
data['messages']=data['messages'][:100]

write_json(data,Path('./data/result_shorten.json'))