import random

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
num = random.randrange(0,5)
print nouns[num] + ' ' + verbs[num] + ' ' + adj[num]
