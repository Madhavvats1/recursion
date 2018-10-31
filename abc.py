def pali(n):
    n=str(n)
    if len(n)==1:
        return True
    elif len(n)==0:
        return True
    else:
        if n[0]==n[-1]:
            return pali(n[1:-1])
        else:
            return False
print(pali("12321"))