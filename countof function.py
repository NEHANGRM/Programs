
l=['b', 'ba', 'ban', 'bana', 'banan', 'banana', 'a', 'an', 'ana', 'anan', 'anana', 'n', 'na', 'nan', 'nana', 'a', 'an', 'ana', 'n', 'na', 'a']
lt=[]
d={}
for i in l:
    lt.append(l.count(i))
for i in range(len(l)):
    d.update({l[i]:lt[i]})
print(d)
