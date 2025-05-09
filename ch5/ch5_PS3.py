s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
# output: 2 
# 20 and 20.0 are considered same in set, but "20" is different from 20 and 20.0