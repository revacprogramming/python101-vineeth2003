# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
hand = open("dataset/romeo.txt")
for line in hand:
  line = line.rstrip()
  x = re.findall('\S*[0-9]\S*', line)
  if line(x)>0:
    print(x)