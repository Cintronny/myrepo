import random

nouns = ("tuition", "students", "college", "fees", "university", "semester", "school", "books", "class")
verbs = ("pay", "will", "make", "fighting", "ability", "helps", "can", "access", "attending", "don't", "gonna", "learn",)
adj = ("free", "many", "new")
num = random.randrange(0,5)
print nouns[num] + ' ' + verbs[num] + ' ' + adj[num]
