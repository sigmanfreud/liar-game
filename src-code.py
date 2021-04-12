import itertools;
def binaryseq(k):
  return ["".join(seq) for seq in itertools.product("01", repeat=k)]
def binarysubset(k):
  resultlist = []
  for i in range (1, k+1):
    for j in binaryseq(i):
      resultlist.append(j)
  return resultlist
print(binarysubset(3))
def function(alist):
  blist = []
  for i in alist:
    blist.append(len(i))
  maxlength = max(blist)
  resultlist = []
  for i in binarysubset(maxlength):
    count = 0
    for j in alist:
      if j.find(i) >= 0:
        count = count + 1
    resultlist.append(count)
  return resultlist

def playermove(alist):
  list1 = function(alist)
  j= len(alist)
  checkmovelist = [abs(1/2 - i/j) for i in list1]
  s = checkmovelist.index(min(checkmovelist))
  print (binarysubset(4)[s])
  return binarysubset(4)[s]

def updatestringlist(alist, string1):
  blist = alist.copy()
  for i in alist:
    if i.find(string1) >= 0:
      alist.remove(i)
  if len(alist) >= 0.5 * len(blist):
    return alist
  else:
    return [x for x in alist if x not in blist]
  print (alist)

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def playtime(x):
  y = binaryseq(x)
  count = 0
  while len(y) > 0:
    y = updatestringlist(y, playermove(y))
    count = count + 1
  return count

print(playtime(1))


  



      

