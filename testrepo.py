import random

nouns = ("tuition", "students", "college", "fees", "university", "semester", "school", "books", "class")
verbs = ("pay", "will", "make", "fighting", "ability", "helps", "can", "access", "attending", "don't", "gonna", "learn")
adj = ("free", "many", "new")
num = random.randrange(0,9)
vernum = random.randrange(0,12)
adnum = random.randrange(0,3)
print nouns[num] + ' ' + verbs[vernum] + ' ' + adj[adnum]
