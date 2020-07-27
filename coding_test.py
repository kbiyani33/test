from itertools import combinations
def isprime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

st=input()
st2=st[::-1]
c=len(st)
#print(c)
res=[]
res2=[]
for i in range(1,len(st)+1):
    res+=list(combinations(st,i))
for j in range(1,len(st2)+1):
    res2+=list(combinations(st2,j))
l=[]
for i in res:
    x=""
    for j in i:
        x+=j
    l.append(int(x))
l2=[]
for i in res2:
    x=""
    for j in i:
        x+=j
    l2.append(int(x))
#print(l)
#print(l2)
ll=[]
for i in l:
    if isprime(i):
        ll.append(i)

for i in l2:
    if isprime(i) and (i not in l):
        ll.append(i)
#ll=sorted(ll)
print(ll)
r=ll[-1]-ll[0]
mean=0
for i in ll:
    mean+=i
mean=mean/len(ll)
length=len(ll)
if(length%2==0):
    median=(ll[length//2]+ll[(length//2)-1])/2
else:
    median=ll[(length-1)//2]
mean=round(mean,2)
median=round(median,2)
r=round(r,2)
d={"mean":mean,"median":median,"range":r}
print(str(d))
