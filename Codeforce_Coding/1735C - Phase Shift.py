for _ in range(int(input())):
  n=int(input())
  t=input()
  used=set()
  mapping={}
  def has(l,c):
    while l in mapping:
      l = mapping[l]
      if l == c: return True
    return False
  for c in t:
    if c in mapping: 
        continue
    for i in range(26):
      l=chr(i+ord('a'))
      if l in used or l == c or (l in mapping and has(l,c) and len(mapping) < 25): 
        continue
      mapping[c]=l
      used.add(l)
      break
  print(''.join(mapping[c] for c in t))

  