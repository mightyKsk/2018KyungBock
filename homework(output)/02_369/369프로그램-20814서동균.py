
# coding: utf-8

# In[10]:


print('주의! 이 프로그램은 369 게임이 아닌\n369게임이라는 탈을 쓴 그냥 컴퓨터 혼자서 짝짝거리는 프로그램입니다.')
print('3의 배수이면 짝, 6의 배수이면 짝짝, 9의 배수이면 짝짝짝, 18의 배수이면 짝짝짝짝이 출력됩니다')
lastnum=int(input('마지막 숫자를 입력해 주세요:'))
if(lastnum==0):
    print('종료')
else:
    lastnum=lastnum+1
    for num in range(1, lastnum):
        if (num%18==0):
            print('짝짝짝짝')
        elif(num%9==0):
            print('짝짝짝')
        elif(num%6==0):
            print('짝짝')
        elif(num%3==0):
            print('짝')
        else:
            print(num)

