#Impotant things before run this code!
#1.google meet window should be independent (no tabs in the google meet window)
#2.chat in google meet has to be activated and textbox should be always focused.
#  if not, you have to manually do it
#3.in case of LOL you should press pgdn key when the ACTUAL game is running
#4.do not clsoe the game while this code is running. if you did, u shuld run this code again.
#5.python 3.7 or latest version should be installed on your computer.
#6.this code can ONLY run in 64-bit operating system. Otherwise it might cause some error.
#7.follwing libraries MUST be installed on venv or default
# pynput, time, pygetwindow, os
from pynput.keyboard import Key, Controller
import time
from pynput import keyboard
import pygetwindow as gw
import os

enb=False
Game=""
a=0
c=0
message = "네" # 메세지 지정
def alt_tab():
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt_l)

#문자 입력 function
def yee(): 
    keyboard = Controller()
    keyboard.type(message) 
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#구글 미팅 title 학인 
while True:
    try:
        MeetingWindow = gw.getWindowsWithTitle('Meet')[0]
        break
    except:
        print("구글미팅을 찾을수 없습니다. 구글미팅이 켜저있는지, 주소(meet.google.com)가 올바른지 확인하세요. 5초후에 다시 시도합니다.")
        time.sleep(5)
        
#게임 프로세스 수동 지정
print("-------------------------------------------------")
print("지금 하려는 게임을 키고 PAGE DOWN 키를 누르시오.")
while enb == False:
    import keyboard
    import pygetwindow as gw
    if keyboard.is_pressed('page_down'):
        
        GameTitle=gw.getActiveWindowTitle()
        Game=gw.getActiveWindow()
        print("지금 하고있는 게임 :",GameTitle)
        Game.minimize()

        # PyGetWindow 라이브러리 특성상 .activate() 로 이미 활성화된 윈도우를 수동으로 포커스를 해제(다른 윈도우로 이동) 후 다시 .activate() 시키면 exception 에러가 뜸. 
        # 에러가 나도 작동엔 지장 없기에 except 에서 아무것도 안함.
        try:
        
            MeetingWindow.activate()
       
        except:
            print("")
        break #whlie 문이고, pgdn 키프레스만 기다리면 되기에 한번 하고 break 로 끝냄.

#break 이후 다시 다른 반복문을 작동시키기 위해 enb를 true 로 지정.
enb=True
    
import keyboard
import pygetwindow as gw
time.sleep(0.5)
Game.restore()
MeetingWindow = gw.getWindowsWithTitle('Meet')[0]

while enb == True:

    #pgup 키 작동코드 / 스왑 / 게임으로 리턴할때 메세지 보냄
    if keyboard.is_pressed('page_up'):
        yee()
        c+=1
        time.sleep(0.02)
        if c==1:
            Game.minimize()
            try:
                MeetingWindow.restore()
                MeetingWindow.activate()
            except:
                print("")
                
            a=a+1
            print('앙',a,"기모찌!")
            
        if c==2:
            Game.restore()
            Game.activate()
            c=-1
            
    #pgdn 키 작동코드 / 그냥 스왑
    if keyboard.is_pressed('page_down'):
        c+=1
        time.sleep(0.02)
        if c==1:
            Game.minimize()
            try:
                MeetingWindow.restore()
                MeetingWindow.activate()
            except:
                print("")
            a=a+1
            print('시',a,"발!")
            
        if c==2:
            Game.restore()
            Game.activate()
            c=-1
