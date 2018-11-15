import random

nouns = ("Tuition", "students", "college", "fees", "university", "semester", "dollars", "student", "money", "time", "Semester", "Cashapp", "Student", "Tuition", "Tuition", "PayPal", "people", "school", "books", "class", "email", "we’re", "year")
verbs = ("pay", "will", "make", "education", "fighting", "ability", "money", "needs", "help", "can", "win", "looking", "Thanks", "access", "attend", "don’t", "gonna", "learn", "just")
adj = ("free", "just", "many", "new")
num = random.randrange(0,24)
vernum = random.randrange(0,19)
adnum = random.randrange(0,4)
print adj[adnum] + ' ' + nouns[num] + ' ' + verbs[vernum]
