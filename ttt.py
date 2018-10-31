x=int(input())
def summ(n):
    n=str(n)
    x=0
    for i in n:
        x=x+int(i)**2
    return x
lism=[]
def rex(n,lis):
    if summ(n)==1:
        return True
    else:
        lis.append(n)
        if summ(n) in lis:
            return False
        else:
            return rex(summ(n),lis)
print(rex(x,lism))
