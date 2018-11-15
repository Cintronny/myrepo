import random

nouns = ("tuition", "students", "college", "fees", "university", "semester", "school", "books", "class")
verbs = ("pay", "will", "make", "fighting", "helps", "can", "access", "attending", "don't", "gonna", "learn")
adj = ("free", "many", "new")
num = random.randrange(0:4)
num_two = random.range(5:9)
vernum = random.randrange(0:5)
vernum_two = random.randrange(6:11)
adnum = random.randrange(0:1)
adnum_two = random.randrange(2:3)
first_half = (adj[adnum] + ' ' + nouns[num] + ' ' + verbs[vernum])
second_half = (adj[adnum_two] + ' ' + verbs[vernum_two] + ' ' + nouns[num_two])
print first_half + ' ' + second_half
