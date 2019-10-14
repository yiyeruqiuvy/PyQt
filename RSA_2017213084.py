import math
import random as r

#素数生成函数
def generate_prime_number(start, end):
    i = start
    g = []
    while i <= end:
        k = True
        for j in range(2,int(math.sqrt(end))):
            if i%j == 0:
                k = False
                break
        if k:
            g.append(i)
        i+=1
    return g

#求质数
def generate_cp(x):
    s = []
    for i in range(2,x):
            if x%i == 0:
                s.append(i)
    return set(s)

#rsa算法生成公钥，私钥
def generate_rsa():
    #生成p，q
    prime = generate_prime_number(15,55)
    p = prime[r.randint(0,len(prime)-1)]
    q = prime[r.randint(0,len(prime)-1)]

    #计算n，hn，确定随机数e,互质啊啊啊啊
    n = p*q
    hn = (p-1) * (q-1)
    cp_hn = generate_cp(hn)
    ck = True
    e = r.randint(2, hn)
    while ck:
        cp_e = generate_cp(e)
        if len(cp_e)>len(cp_hn):
            if(cp_e-cp_hn) == max(cp_hn,cp_e):
                ck = False
                break

        else:
            if(cp_hn-cp_e) == max(cp_hn,cp_e):
                ck = False
                break
        e = r.randint(2, hn)

    #确定公钥
    PK = (e,n)

    #确定私钥
    i = 1
    ok = True
    while ok:
        if(i*e)%hn == 1:
            ok = False
        i+=1
    d = i-1
    SK = (d,n)
    print(p,q,n,hn,e,d)
    return[PK,SK]

k = generate_rsa()

print(k)


#解密
x = generate_cp(66)
y = generate_cp(87)
print(x)
print(y)
print(x-y)
print(max(x,y))