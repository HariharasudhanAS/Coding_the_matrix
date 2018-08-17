def makeInverseIndex(strlist):
    '''Copied from github'''
    dictionary=dict()
    for (index,ele) in enumerate(strlist):
        for j in ele.split():
            curset=dictionary[j] if j in dictionary else set()
            curset.add(index)
            dictionary[j]=curset
    return dictionary

def orSearch(inverseIndex, query):
    '''Searches for the queries in inverseIndex'''
    a=set()
    for i in query:
        if i in inverseIndex.keys():
            a = a | inverseIndex[i] #Dont use add as add is only for one element
    return a

def andSearch(inverseIndex, query):
    '''Searches for docs that contains all words in query'''
    if inverseIndex[query[0]]:
        a=inverseIndex[query[0]]
        for i in query:
            if i in inverseIndex.keys():
                a = a & inverseIndex[i]
            else:
                a=set()
                break
    else:
        a=set()
    return a

f = open('stories_small.txt')
stories = list(f)
inverseIndex = makeInverseIndex(stories)

print(orSearch(inverseIndex,['and','the','of']))
