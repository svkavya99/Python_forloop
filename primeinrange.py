a=int(input("ENTER MIN VALUE OF RANGE\n"))
b=int(input("ENTER MAX VALUE OF GIVEN RANGE\n"))
for i in range(a,b):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
        
