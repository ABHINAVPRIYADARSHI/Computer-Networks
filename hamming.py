a=[int(x) for x in input("enter the dataword").split()]
a=a[::-1]
for i in range(len(a)-1):
    a.insert((2**i)-1,0)

a[0]=(a[0]+a[2]+a[4]+a[6])%2
a[1]=(a[1]+a[2]+a[5]+a[6])%2
a[3]=(a[3]+a[4]+a[5]+a[6])%2
a=a[::-1]
print("the codeword is : ")
for i in range(len(a)):
    print(a[i],end=" ")

b=[int(x) for x in input("\nenter the received codeword ").split()]
b=b[::-1]
b[0]=(b[0]+b[2]+b[4]+b[6])%2
b[1]=(b[1]+b[2]+b[5]+b[6])%2
b[3]=(b[3]+b[4]+b[5]+b[6])%2

if( b[0]==0 and b[1]==0 and b[3]==0):
    print("no error")
else:
    i=b[3]*(2**2)+b[1]*(2**1)+b[0]*(2**0)
    print("error is found at position ",i)
