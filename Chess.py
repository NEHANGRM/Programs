c=input("Enter the Co-ordinates of KING,ROOK,BISHOP:").split(',')
if((int(c[0])==int(c[2]) or int(c[1])==int(c[3])) and ((int(c[0])-int(c[1]))==(int(c[4])-int(c[5])))):
    print("King is in check by Rook and Bishop")
elif(int(c[0])==int(c[2]) or int(c[1])==int(c[3])):
    print("King is in check by Rook")
elif((int(c[0])-int(c[1]))==(int(c[4])-int(c[5]))):
    print("King is in check by Bishop")

        
