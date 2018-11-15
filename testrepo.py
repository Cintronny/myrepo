import random

nouns = ("tuition", "students", "college", "fees", "university", "semester", "")
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
num = random.randrange(0,5)
print nouns[num] + ' ' + verbs[num] + ' ' + adj[num]
