#분식집 스크립트 made by 20812 박우혁
#======기본설정========
김밥류 = ["일반김밥", "치즈김밥", "고기김밥", "야채김밥"]
라면류 = ['라면 I' , '라면 II' , '라면 III', '라면 IV']
다른류 = ['밥', '비싼밥', '돈가스']

def 입장():
    입장여부 = input("들어간다 = 응 / 나간다 = 아니 : ")
    
    if 입장여부 == '응' :
        메뉴판()
    elif 입장여부 == '아니' :
        print("============================")
        print("============================")
        print("============================")
        print('       안녕히 가십쇼')
        print("============================")
        print("============================")
        print("============================")
    else:
        입장()

def 메뉴판():
    print("김밥류 : " , 김밥류)
    print("라면류 : " , 라면류)
    print("다른류 : " , 다른류)
    while True:
        류_선택 = input("원하시는 카테고리를 골라주세요! ('아니'로 나가기 , 나가면 못돌아옴.): ")
        
        if 류_선택 == '김밥류' :
            세부선택 = int(input("원하시는 메뉴를 골라주세요! (0부터 순서대로) : "))
            if 세부선택 <= 3 :
                print(김밥류[세부선택])
                print('((((((((@')
            else :
                continue
        elif 류_선택 == '라면류' :
            세부선택 = int(input("원하시는 메뉴를 골라주세요! (0부터 순서대로) : "))
            if 세부선택 <= 3 :
                print(라면류[세부선택])
                print('~~~~~~~~~~~~')
            else :
                continue
        elif 류_선택 == '다른류' :
            세부선택 = int(input("원하시는 메뉴를 골라주세요! (0부터 순서대로) : "))
            if 세부선택 <= 2 :    
                print(다른류[세부선택])
                print('~~~~~~&@')
            else :
                continue
        elif 류_선택 == '아니' :
            print("============================")
            print("============================")
            print("============================")
            print('       안녕히 가십쇼')
            print("============================")
            print("============================")
            print("============================")
            break
        
        else :
            continue

#출력
print("분식집에 오신것을 환영합니다~!")
입장()

