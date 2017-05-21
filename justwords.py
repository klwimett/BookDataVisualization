import json

with open('just_titles_short.json') as file1:
    titles = json.load(file1)

titles_split = []

for t in titles:
    t = str(t)
    x = str.split(t)
    titles_split.append(x)

print titles_split
