#打印1-100的数，并且自动跳过7的倍数和包含7的数
                                                                                                                                                                                
a=0
while a<100:
    a+=1
    if a%7!=0 and (a-7)%10!=0 and a//10!=7:
        print(a)

