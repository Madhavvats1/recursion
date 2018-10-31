Y=input()
count=0
for i in range(len(Y)-3):
    if Y[i]+Y[i+1]=="co" and Y[i+3]=="e":
        count=count+1
print(count)
