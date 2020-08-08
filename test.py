def MyExpMod(a, n, m):
    print("a = ",a)
    print("n = ",n)
    print("m = ",m)
    print("-----------")
    result =1
    for i in range(1,n+1,1):
        #print("? = ",result,'/',i)
        result = result*a
        i+=1
    result = result%m
    return result
       

def gcd(a, m):
    if a < m: 
        (a, m) = (m, a) 
        while m != 0: 
            (a, m) = (m, a % m)
        return a


def MyInvMod(a, m):   
   if (gcd(a,m) != 1):
       a=a/gcd(a,m)
       m=m/gcd(a,m)
   result2 = (1+m)/a
   
   return result2


result = MyExpMod(3,7,11)
result2 = MyInvMod(3,11)
print("a^n mod m = ",result)
print("a^(-1) mod m = ",result2) 