import json

with open('open-library-data-condensed.json') as file1:
    data = json.load(file1)

justTitles = []

for book in data[:10000]:
    isbnKey = book.keys()[0]
    bookData = book[isbnKey]
    title = bookData["title"]
    onlyFirstPart = title.split("(")[0]
    justTitles.append(onlyFirstPart)

with open('just_titles.json', 'w') as outfile:
    json.dump(justTitles, outfile, indent=2)
