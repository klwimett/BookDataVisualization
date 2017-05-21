import json

with open('just_titles_short.json') as file1:
    titles = json.load(file1)

titles_split = []

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

for t in titles:
    t = str(t).strip()
    words_per_title = t.split(" ")
    titles_split += words_per_title

print "The unique words used in the titles, and their frequeny"
print wordListToFreqDict(titles_split)

