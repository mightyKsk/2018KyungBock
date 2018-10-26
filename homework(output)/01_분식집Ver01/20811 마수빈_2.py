print('어서오세요. 메뉴판을 보시고 각 메뉴를 얼마씩 주문할지 말씀해주세요.')
print('  ')
print('                     -메뉴-')
print('  김밥류            떡볶이류            라면류')
print('김밥 1500원       떡볶이 3500원     라면 3000원')
print('참치김밥 2000원    라볶이 4000원     떡라면 3500원')
print('치즈김밥 2500원    쫄볶이 3500원     치즈라면 3500원')
print('돈까스김밥 3500원  치즈라볶이 4500원  만두라면 3500원')
print('날치알김밥 3500원  치즈떡볶이 4500원  짬뽕라면 3500원')
print('새우김밥   3500원  치즈쫄볶이 4500원  콩나물라면 3500원')
print('  ')

while True :
    menu_select=int(input("메뉴의 종류를 선택하세요(1.김밥류, 2.떡볶이류, 3.라면류,0.종료 :"))
    if(menu_select==0)  : break
    if not(1<=menu_select<=3) :
        print("잘못 선택하셨습니다.다시 선택하세요")
        continue
    else :
        if(menu_select==1) :
            print("김밥류를 선택하셨습니다")
            sub_menu_select=int(input())
    
