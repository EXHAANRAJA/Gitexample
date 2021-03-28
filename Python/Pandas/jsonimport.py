import pandas as pd
import json

with open(r"C:\Users\rajaa\Desktop\Github Repo\Python-Examples\Python\Pandas\states.json") as f:
  data = json.load(f)

for state in data['states']:
  print(state)

# To Delete any json object 
for state in data['states']:
  del state['area_codes']

#Json object print without area code
newstring = json.dumps(data,indent=2,sort_keys=True)
for newstring in data['states']:
  print(newstring)









