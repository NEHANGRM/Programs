def minion_game(string):
    pl1=0
    win=0
    pl2=0
    lt=[]
    ltt=[]
    d={}
    s=""
    vowel='AEIOUaeiou'
    for i in range(len(string)):
        for k in range(i,len(string)):
            for j in range(k,len(string)):
                    s+=string[j]
                    lt.append(s)
            s=""
        break
    for i in lt:
        ltt.append(lt.count(i))
    for i in range(len(lt)):
        d.update({lt[i]:ltt[i]})
    for i in d.items():
        t=i[0]
        if(t[0] not in vowel):
            pl1+=i[1]
        else:
            pl2+=i[1]
    if(pl1>pl2):
        print("Stuart {}".format(pl1))
    if(pl1<pl2):
        print("Kevin {}".format(pl2))
    if(pl1==pl2):
        print("Draw")
                
if __name__ == '__main__':
    s = input()
    minion_game(s)

