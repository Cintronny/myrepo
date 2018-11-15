import random

nouns = ("tuition", "students", "college", "fees", "university", "semester", "school", "books", "class")
verbs = ("pay", "will", "make", "fighting", "helps", "can", "access", "attending", "don't", "gonna", "learn")
adj = ("free", "many", "new")
num = random.randrange(0,9)
vernum = random.randrange(0,11)
adnum = random.randrange(0,3)
first_half = (adj[adnum] + ' ' + nouns[num] + ' ' + verbs[vernum])
second_half = (adj[adnum] + ' ' + verbs[vernum] + ' ' + nouns[num])
print first_half + ' ' + second_half
