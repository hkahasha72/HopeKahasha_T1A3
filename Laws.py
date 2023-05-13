import json

with open('questions.json') as f:
    data = json.load(f)

for answer in data['questions']:
    print(answer)
    
