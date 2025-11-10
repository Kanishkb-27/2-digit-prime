prime=[True for i in range(100)]
p=2
while(p*p<=99):
    if(prime[p]==True):
        for i in range(p*p,100,p):
            prime[i]=False
    p+=1
for p in range(2,100):
    if prime[p]:
        if p in range(10,100):
            print(p)