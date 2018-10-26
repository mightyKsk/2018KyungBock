
# coding: utf-8

# In[3]:


num=int(input('369 369! 369 369! '))

   
while (num!=0) :
    if (num%9==0) :
        print('짝짝짝!')
    elif (num%6==0) :
        print('짝짝!')
    elif (num%3==0) :
        print('짝!')
    else :
        print('%d!'%num)
    num=int(input())
print('오늘은 여기까지~')

