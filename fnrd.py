text=input()
count = 1
for i in range(len(text)):
    try:
        if text[i]==text[i+1]:
            count+=1
        else:
            print(str(count)+str(text[i]),end='')
            count=1
    except:
        print(str(count)+str(text[i]),end='')
