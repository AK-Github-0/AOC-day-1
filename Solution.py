f = open("input.txt", "r")
a = []
b = []
for x in f:
  try:
    a.append(int(x))
  except:
    b.append(sum(a))
    a.clear()
b.append(sum(a))
print(max(b),sum(sorted(b)[-3:]))
