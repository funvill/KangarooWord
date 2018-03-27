'''
Created by: Steven Smethurst
Created on: March 26, 2018
http://blog.abluestar.com 
'''

from itertools import chain
from itertools import combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

word_list = list()
with open('20k.txt') as f:
    word_list = f.read().splitlines()

wordCount = len(word_list)
print("Dictionary word count: ", wordCount)

outputFile = open('result_20k.txt', 'w')

'Stats - Report the largest word'
largestKangarooWord = "" 
largestKangarooWordCount = 0 ; 

progress = 0
for word in word_list:
    progress+= 1 
        
    if word.startswith("#"):
        continue
    if len(word) < 5:
        continue

    print("progress: ", progress, "/", wordCount, ": ", end='')

    subWordList = list()
    for item in set(powerset(word)):
        if len(item) < 4:
            continue
        combo = "".join(item)
        if combo == word:
            continue
        if combo in word_list:            
            subWordList.append( combo )
    if len(subWordList) > 0:
        print(word, ", subWordCount: ", len(subWordList), ", ", end='')
        print(word, ", subWordCount: ", len(subWordList), ", ", end='', file=outputFile)
        for subword in set(subWordList):            
            outputFile.write("%s, " % subword)
            print(subword, ", ", end='')
        print("")
        print("", file=outputFile)
        outputFile.flush()
        
        if len(subWordList) > largestKangarooWordCount:
            largestKangarooWordCount = len(subWordList)
            largestKangarooWord = word 
            print("New largest KangarooWord!!! ", largestKangarooWord, largestKangarooWordCount )        

print("\n\n\nDONE!!!!\n\n\n")
print("largest KangarooWord!!! ", largestKangarooWord, largestKangarooWordCount )
