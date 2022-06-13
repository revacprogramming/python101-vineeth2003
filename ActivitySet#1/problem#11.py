# Tuples
import string
filename = open("dataset/mbox-short.txt")
counts = dict()
for line in filename:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1

t = []
for count,email in counts.items:
  newtup = (count,email)
  t.append(newtup)

t = sorted(t, reverse=true)

for count,email in t[:10] :()
print(count,email)
