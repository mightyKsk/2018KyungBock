#369 프로그램 made by 박우혁 1.0

import time

#모드 함수
def mainUI():#메인 창(UI)
    print('='*30)
    print('$$$ 안녕하세요! 이 코드는 369 게임을 하는 코드입니다. $$$')
    print('원하시는 게임 모드를 선택하세요!\n')
    print('1. 1인 플레이\n')
    print('2. 2인 플레이\n')
    print('3. 컴퓨터가 하는거 구경하기\n')
    print('4. 만든이\n')
    print('5. 종료\n')
    print('='*30)

def playerone_vs_computer():
    num = 1
    numc = str(num)
    c3 = numc.count('3')
    c6 = numc.count('6')
    c9 = numc.count('9')
    cA = c3 + c6 + c9
    print('$$$ 컴퓨터와 대전 모드입니다. $$$\n')
    선공 = input('선공하시겠어요? (y or n): ')
    
    if 선공 == 'y':
        유저입력 = 'a'
        while 유저입력 != '그만': #게임 진행중
            유저입력 = input('당신의 턴입니다 ("그만"으로 종료): ')
            if 0 == 0: #유저의 턴일때
                if cA == 0: # 369가 포함 안될시 
                    답 = numc

                elif cA != 0:
                    답 = '짝'*cA

                if 유저입력 == 답: #정답
                    num += 1
                    numc = str(num)
                    c3 = numc.count('3')
                    c6 = numc.count('6')
                    c9 = numc.count('9')
                    cA = c3 + c6 + c9
                    
                    time.sleep(0.5)
                    
                    if cA == 0: #컴퓨터 턴
                        print('\n', num, '\n') #컴퓨터 대답

                        num += 1
                        numc = str(num)
                        c3 = numc.count('3')
                        c6 = numc.count('6')
                        c9 = numc.count('9')
                        cA = c3 + c6 + c9

                    elif cA != 0:
                        print('\n', '짝'*cA, '\n')

                        num += 1
                        numc = str(num)
                        c3 = numc.count('3')
                        c6 = numc.count('6')
                        c9 = numc.count('9')
                        cA = c3 + c6 + c9

                else: #오답
                    print('패배\n')
                    유저입력 = input('계속하시겠어요? 아무입력이나 하세요. ("그만"으로 종료): ')
                    print('\n')
    
    elif 선공 == 'n':
        유저입력 = 'a'
        print('1')
        num = 2
        numc = str(num)
        c3 = numc.count('3')
        c6 = numc.count('6')
        c9 = numc.count('9')
        cA = c3 + c6 + c9
        while 유저입력 != '그만': #게임 진행중
            유저입력 = input('당신의 턴입니다 ("그만"으로 종료): ')
            if 0 == 0: #유저의 턴일때
                if cA == 0: # 369가 포함 안될시 
                    답 = numc

                elif cA != 0:
                    답 = '짝'*cA

                if 유저입력 == 답: #정답
                    num += 1
                    numc = str(num)
                    c3 = numc.count('3')
                    c6 = numc.count('6')
                    c9 = numc.count('9')
                    cA = c3 + c6 + c9
                    
                    time.sleep(0.5)
                    
                    if cA == 0: #컴퓨터 턴
                        print('\n', num, '\n') #컴퓨터 대답

                        num += 1
                        numc = str(num)
                        c3 = numc.count('3')
                        c6 = numc.count('6')
                        c9 = numc.count('9')
                        cA = c3 + c6 + c9

                    elif cA != 0:
                        print('\n', '짝'*cA, '\n')

                        num += 1
                        numc = str(num)
                        c3 = numc.count('3')
                        c6 = numc.count('6')
                        c9 = numc.count('9')
                        cA = c3 + c6 + c9

                else: #오답
                    print('패배')
                    유저입력 = input('계속하시겠어요? 아무입력이나 하세요. ("그만"으로 종료): ')

def player_vs_player():
    num = 1
    numc = str(num)
    c3 = numc.count('3')
    c6 = numc.count('6')
    c9 = numc.count('9')
    cA = c3 + c6 + c9
    print('$$$ 대전 모드입니다. $$$\n')
    선공 = input('선공하실 플레이어의 이름을 넣어주세요 : ')
    후공 = input('후공하실 플레이어의 이름을 넣어주세요 : ')

    while True:
        if cA == 0: # 369가 포함 안될시 
            답 = numc

        elif cA != 0:
            답 = '짝'*cA

        print(선공, end='')
        선공입력 = input('님의 턴입니다 : ')

        if 선공입력 == 답: 
            print('\n')
            num += 1
            numc = str(num)
            c3 = numc.count('3')
            c6 = numc.count('6')
            c9 = numc.count('9')
            cA = c3 + c6 + c9
            if cA == 0: # 369가 포함 안될시 
                답 = numc
            elif cA != 0:
                답 = '짝'*cA

            print(후공, end='')
            후공입력 = input('님의 턴입니다 : ')

            if 후공입력 == 답: 
                print('\n')
                num += 1
                numc = str(num)
                c3 = numc.count('3')
                c6 = numc.count('6')
                c9 = numc.count('9')
                cA = c3 + c6 + c9
            else:
                print('\n')
                print(선공, '님의 승리!')
                break

        else:
            print('\n')
            print(후공, '님의 승리!')
            break

def computer():
    유저입력 = int(input('몇까지 시킬건가요? :'))
    turn = 0
    num = 1
    numc = str(num)
    c3 = numc.count('3')
    c6 = numc.count('6')
    c9 = numc.count('9')
    cA = c3 + c6 + c9
    
    while turn < 유저입력 :
        if cA == 0:
            print(num)
        
            num += 1
            numc = str(num)
            c3 = numc.count('3')
            c6 = numc.count('6')
            c9 = numc.count('9')
            cA = c3 + c6 + c9
        
            turn += 1
    
        elif cA != 0:
            print('짝'*cA)
        
            num += 1
            turn += 1
            numc = str(num)
            c3 = numc.count('3')
            c6 = numc.count('6')
            c9 = numc.count('9')
            cA = c3 + c6 + c9
 
        else:
            print('s')

mainUI()

while True: # 모드실행 입력
    mainin = input('\n메인화면의 입력을 기다리고 있습니다 (0을 입력하여 메인화면 새로고침): ') # 메인화면입력
    
    if mainin == '0':
        mainUI()

    elif mainin == '1':
        playerone_vs_computer()
    elif mainin == '2':
        player_vs_player()

    elif mainin == '3':
        computer()
    
    elif mainin == '4':
        print('\n'*2,)
        print('='*30)
        print('만든이 : 박우혁 (20812)')
        print('지식의 부족을 대량의 코드로 매꾼 노가다작입니다.')
        print('제작시간 대략 4, 5시간정도')
        print('='*30)

    elif mainin == '종료':
        print('\n안녕히! \n')
        time.sleep(1)
        break
    elif mainin == '5':
        print('\n안녕히! \n')
        time.sleep(1)
        break
    
    else:
        print('다시 입력하세요')

