def divide(divisor,codeword,new_codeword):
    rem=[]
    for i in codeword:
        if(len(rem)==len(divisor)):
            break
        else:
            rem.append(i)
    cont=0
    cont1=len(divisor)-1
    new_divisor=divisor[:]
    while(cont!=len(new_codeword)):
        for i in range(len(divisor)):
            if((rem[i]==1 and divisor[i]==1) or (rem[i]==0 and divisor[i]==0)):
                rem[i]=0
            else:
                rem[i]=1
        cont+=1
        cont1+=1
        if(cont==len(new_codeword)):
            break
        for i in range(len(divisor)):
            if(i==len(divisor)-1):
                rem[i]=codeword[cont1]
            else:
                rem[i]=rem[i+1]
        if(rem[0]==0):
            for i in range(len(divisor)):
                divisor[i]=0
        else:
            for i in range(len(divisor)):
                divisor[i]=new_divisor[i]
    rem.pop(0)
    return(rem)


#starting of program

codeword=[int(x) for x in input("enter the data: ").split()]
new_codeword=codeword[:]
new_codeword2=new_codeword[:]
divisor=[1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1]
#divisor=[1,1,1,1,1]
print("generating polynomial: ","".join([str(x) for x in divisor]))
codeword.extend([0 for x in range(len(divisor)-1)])
print("modified dataword: ","".join([str(x) for x in codeword]))

#calling the function divide
rem=divide(divisor,codeword,new_codeword)

print("CRC checksum is : ","".join([str(x) for x in rem]))
new_codeword.extend(rem)
print("the final codeword transmitted is: ","".join([str(x) for x in new_codeword]))
choice=int(input("do you want to do test error detection  0:No 1:yes"))

if(choice==0):
    print("No error detected")
else:
    errorcodeword=new_codeword[:]
    pos=int(input("enter the position at which you want to insert error "))
    if(errorcodeword[pos-1]==0):
        errorcodeword[pos-1]=1
        print("erroneous data is: ","".join([str(x) for x in errorcodeword ]))
        rem=divide(divisor,errorcodeword,new_codeword2)
        print("CRC checksum is: ","".join([str(x) for x in rem]))
        print("error detected")

    else:
        errorcodeword[pos-1]=0
        print("erroneous data is: ","".join([str(x) for x in errorcodeword ]))
        rem=divide(divisor,errorcodeword,new_codeword2)
        print("CRC checksum is: ","".join([str(x) for x in rem]))
        print("error detected")






