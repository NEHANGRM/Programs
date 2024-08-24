f=open("number_power_product.txt","wt")
f.write("2 3 4 2 5 4 3 2 6 3")
f.close()
fo=open("number_power_product.txt","rt")
r=fo.readlines()
fo.close()
lo=r[0].split(' ')
print(r)
def reverse_list_recursive(lt):
    if(lt==[]):
        return ""
    else:
        return(str(lt[-1])+str(reverse_list_recursive(lt[:-1])))
l=list(reverse_list_recursive(lo))
print(l)
    
        
