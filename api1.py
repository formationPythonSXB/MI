import requests
import json

url = "https://api.github.com/orgs/Yunohost-Apps/repos"

i=1
r = requests.get(url,"page="+str(i))

if r.status_code != 200:
    raise Exception(r.text)

while r.text != "[]" :
    issues = json.loads(r.text)

    for issue in issues:
        print(issue["pushed_at"])
      
    i+=1
    r = requests.get(url,"page="+str(i))

    if r.status_code != 200:
        raise Exception(r.text)
    
    