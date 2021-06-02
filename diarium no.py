#disarium no
def disarium(n):
    cnt=0
    temp=n
    while n:
        n=n//10
        r=n%10
        cnt=cnt+1
    i=1
    k=0
    print(n)
    n=temp
    print(n)
    while n:
        r=n//pow(10,cnt-1)
        n=n%pow(10,cnt-1)
        k=k+pow(r,i)
        i+=1
        cnt-=1
    n=temp
    if k==n:
        return True
    else:
        return False
