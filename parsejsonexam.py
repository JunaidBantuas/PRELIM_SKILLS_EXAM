import json
import yaml

with open('covid_cases.json','r') as jsonpa:
    data = json.load(jsonpa)
print(data)