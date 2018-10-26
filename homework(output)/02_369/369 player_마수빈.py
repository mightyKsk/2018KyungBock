
# coding: utf-8

# In[ ]:


print('이 프로그램은 혼자서 369게임을 합니다.')
print('룰은 아래와 같습니다.')
print('3의 배수: 짝')
print('6의 배수: 짝짝')
print('9의 배수: 짝짝짝')
print('6의 배수이면서 9의 배수: 짝짝짝짝짝')
print('당신이 해야할 것은 마지막 숫자를 입력하고 지켜보는 것입니다.')
i='yes'
while (i=='yes') :
    last=int(input('마지막 숫자를 입력하세요:  '))
    number=last+1
    for a in range(1,number) :
        if (a%9==0 and a%6==0) :
            print('짝짝짝짝짝', end=' ')
        elif (a%9==0 and a%6!=0) :
            print('짝짝짝', end=' ')
        elif (a%9!=0 and a%6==0) :
            print('짝짝', end=' ')
        elif (a%3==0) :
            print('짝', end=' ')
        else :
            print(a, end=' ')
    print(' 번호 끝!')
    i=str(input('한 번 더? yes or no:  '))
print('Thank you for playing!')

