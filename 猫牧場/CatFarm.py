
import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image
from PIL import ImageTk

import pygame
from pygame.locals import *
import os
import sys
import random
from pygame import mixer
# import pgzrun
import math

key = ""
koff = False

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    # global koff
    # koff = True
    global key
    key = ""

px = 90  # キャラの初期配置のx座標
py = 90  # キャラの初期配置のy座標
dir = 0
ani = 0

e1x = 570  # 敵キャラ１の初期配置のx座標
e1y = 570  # 敵キャラ１の初期配置のy座標
e1_dir = 1
e1_ani = 0

e2x = 630  # 敵キャラ２の初期配置のx座標
e2y = 360  # 敵キャラ２の初期配置のy座標
e2_dir = 0
e2_ani = 0

e3x = 630  # 敵キャラ３の初期配置のx座標
e3y = 170  # 敵キャラ３の初期配置のy座標
e3_dir = 3
e3_ani = 0

timer = 0
cry1_timer = 100
cry2_timer = 60
cry3_timer = 20

DIR_DOWN = 0
DIR_LEFT = 1
DIR_RIGHT = 2
DIR_UP = 3
ANIMATION = [0, 1, 0, 2]

player_speed = 15
enemy_speed = 10

music_set_volume = 0.07   # BGMの音量
sound_volume = 0.05       # 効果音の音量

_cry1_timer = 40
_cry2_timer = 40
_cry3_timer = 40
cry1_flg = 0
cry2_flg = 0
cry3_flg = 0

food = ""
food_flg = 0

food1_timer = 0
food2_timer = 0
food3_timer = 0
eat1_flg = 0
eat2_flg = 0
eat3_flg = 0

fx = 0
fy = 0

SCREEN_RECT = Rect(0, 0, 500, 500)
CS = 32
SCREEN_NCOL = SCREEN_RECT.width//CS
SCREEN_NROW = SCREEN_RECT.height//CS
SCREEN_CENTER_X = SCREEN_RECT.width//2//CS
SCREEN_CENTER_Y = SCREEN_RECT.height//2//CS

p_wx, p_wy = 1, 1

map_data = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,3,4,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,5,6,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,3,4,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,5,6,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


# 画像描写
# a = 0
def draw_screen():  

    global player,enemy,girl,cat1,cat2,cat3,e1x,e2x,e3x,e1y,e2y,e3y,food

    canvas.delete("SCREEN")
    
    for y in range(SCREEN_NROW):
        for x in range(SCREEN_NCOL):
            canvas.create_image(x*60+30, y*60+30, image=tile[0], tag="SCREEN") # 草原
            canvas.create_image(x*60+30, y*60+30, image=tile[map_data[y][x]], tag="SCREEN") # タイル

    if food_flg == 1:
        food = fx, fy
        canvas.create_image(food, image=tile[1] ,tag="food") # 餌
            
    girl = px, py
    canvas.create_image(girl, image=img_player[ani], tag="SCREEN") # 人間

    cat1 = e1x, e1y
    canvas.create_image(cat1, image=img_enemy1[e1_ani], tag="SCREEN"), # 猫１
    cat2 = e2x, e2y    
    canvas.create_image(cat2, image=img_enemy2[e2_ani], tag="SCREEN"), # 猫２
    cat3 = e3x, e3y
    canvas.create_image(cat3, image=img_enemy3[e3_ani], tag="SCREEN") # 猫３
    

# 壁チェック
def check_wall(cx, cy ,di ,dot):

    global food

    chk = False

    if di == DIR_UP:        # 上移動チェック

        mx = int((cx-30)/60)
        my = int((cy-30-dot)/60)
        
        if map_data[my][mx] > 1:
            chk = True

        mx = int((cx+29)/60)

        if map_data[my][mx] > 1:
            chk = True      

    if di == DIR_LEFT:      # 左移動チェック

        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)

        if map_data[my][mx] > 1:
            chk = True

        my = int((cy+29)/60)

        if map_data[my][mx] > 1:
            chk = True  

    if di == DIR_RIGHT:     # 右移動チェック

        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)

        if map_data[my][mx] > 1:
            chk = True

        my = int((cy+29)/60)

        if map_data[my][mx] > 1:
            chk = True

    if di == DIR_DOWN:      # 下移動チェック

        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)

        if map_data[my][mx] > 1:
            chk = True

        mx = int((cx+29)/60)

        if map_data[my][mx] > 1:
            chk = True
    
    return chk


# メインキャラの動き（キーボード操作による座標遷移）
def move_player():

    global px,py,key,ani,dir,player_speed,food_flg,fx,fy,e1x,e1y,\
        food1_timer,food2_timer,food3_timer

    # print(px,py,fx,fy)
    # print(px-fx,py-fy)

    if key == "Down" and py < 710:   # キャラの下移動限界のy座標
        
        dir = DIR_DOWN
   
        if  check_wall(px ,py ,dir ,player_speed) == False:
            py = py + player_speed
    
    if key == "Left" and px > 30:    # キャラの左移動限界のx座標

        dir = DIR_LEFT

        if  check_wall(px ,py ,dir ,player_speed) == False:
            px = px - player_speed
            
    if key == "Right" and px < 870:  # キャラの右移動限界のx座標

        dir = DIR_RIGHT

        if  check_wall(px ,py ,dir ,player_speed) == False:
            px = px + player_speed
                      
    if key == "Up" and py > 40:      # キャラの上移動限界のy座標
        
        dir = DIR_UP

        if  check_wall(px ,py ,dir ,player_speed) == False:        
            py = py - player_speed        
    
    # 餌投下
    if key == "space":
    
        canvas.create_image(px, py+48, image=tile[1] ,tag="food")

        food_flg = 1
        fx = px
        fy = py+48
        food1_timer = 0
        food2_timer = 0
        food3_timer = 0

    if food_flg == 1:

        # 餌撤去
        if key == "Return":

            canvas.delete("food")
            food_flg = 0
            fx = ""
            fy = ""
            food1_timer = 0
            food2_timer = 0
            food3_timer = 0

    ani = dir*3 + ANIMATION[timer%4]

# 敵キャラ1の動き（ランダムの座標遷移）
def move_enemy1():

    global e1x,e1y,e1_ani,e1_dir,cry_sound,cry1_timer,_cry1_timer,cry1_flg,\
        food,food1_timer,eat1_flg

    cry1_timer += 1

    if cry1_timer > 120:

        cry1_sound = mixer.Sound('sounds/cat1.mp3')
        cry1_sound.set_volume(sound_volume)
        cry1_sound.play()

        cry1_timer = 0

    if food1_timer == 0:

        if e1x%60 == 30 and e1y%60 == 30:

            e1_dir = random.randint(0, 3)   

        if e1_dir == DIR_DOWN and e1y < 710:   # 敵キャラの下移動
            
            if  check_wall(e1x , e1y, e1_dir, enemy_speed) == False:
                e1y = e1y + enemy_speed
    
        if e1_dir == DIR_LEFT and e1x > 30:    # 敵キャラの左移動

            if  check_wall(e1x , e1y, e1_dir, enemy_speed) == False:
                e1x = e1x - enemy_speed
        
        if e1_dir == DIR_RIGHT and e1x < 870:  # 敵キャラの右移動

            if  check_wall(e1x , e1y, e1_dir, enemy_speed) == False:
                e1x = e1x + enemy_speed
                    
        if e1_dir == DIR_UP and e1y > 40:      # 敵キャラの上移動
            
            if  check_wall(e1x , e1y, e1_dir, enemy_speed) == False:        
                e1y = e1y - enemy_speed

        e1_ani = e1_dir*3 + ANIMATION[timer%4]

        # 人間と接触すると鳴く
        if cry1_flg == 1:
            _cry1_timer += 1

            if _cry1_timer == 40:
                cry1_flg = 0

        if abs(e1x-px) <= 40 and abs(e1y-py) <= 40 and _cry1_timer >= 40:
            
            # 鳴き声
            cry4_sound = mixer.Sound('sounds/cat4.mp3')
            cry4_sound.set_volume(sound_volume)
            cry4_sound.play()

            cry1_flg = 1
            _cry1_timer = 0


    # 餌と接触すると食べる
    if food_flg == 1:
            
        if abs(e1x-fx) <= 28 and abs(e1y-fy) <= 28 and food1_timer <= 10:

            food1_timer += 1
            e1x = e1x
            e1y = e1y
            eat1_flg = 1

            if food1_timer == 10:

                # 食べる音
                cry1_sound = mixer.Sound('sounds/cat7.mp3')
                cry1_sound.set_volume(sound_volume)
                cry1_sound.play()

                eat1_flg = 0
                food1_timer = 0        

            e1_ani = e1_dir*3 + ANIMATION[timer%4]

        if food1_timer > 10:
            food1_timer = 0        

# 敵キャラ2の動き（ランダムの座標遷移）
def move_enemy2():

    global e2x,e2y,e2_ani,e2_dir,cry2_timer,_cry2_timer,cry2_flg,\
        food,food2_timer,eat2_flg

    cry2_timer += 1

    if cry2_timer > 120:

        cry2_sound = mixer.Sound('sounds/cat2.mp3')
        cry2_sound.set_volume(sound_volume)
        cry2_sound.play()

        cry2_timer = 0    

    if food2_timer == 0:    
    
        if e2x%60 == 30 and e2y%60 == 30:

            e2_dir = random.randint(0, 3)

        if e2_dir == DIR_DOWN and e2y < 710:   # 敵キャラの下移動限界のy座標
            
            if  check_wall(e2x , e2y, e2_dir, enemy_speed) == False:
                e2y = e2y + enemy_speed    
        
        if e2_dir == DIR_LEFT and e2x > 30:    # 敵キャラの左移動限界のx座標

            if  check_wall(e2x , e2y, e2_dir, enemy_speed) == False:
                e2x = e2x - enemy_speed
        
        if e2_dir == DIR_RIGHT and e2x < 870:  # 敵キャラの右移動限界のx座標

            if  check_wall(e2x , e2y, e2_dir, enemy_speed) == False:
                e2x = e2x + enemy_speed
                    
        if e2_dir == DIR_UP and e2y > 40:      # 敵キャラの上移動限界のy座標
            
            if  check_wall(e2x , e2y, e2_dir, enemy_speed) == False:        
                e2y = e2y - enemy_speed

        e2_ani = e2_dir*3 + ANIMATION[timer%4]

        # 人間と接触すると鳴く
        if cry2_flg == 1:
            _cry2_timer += 1

            if _cry2_timer == 40:
                cry2_flg = 0

        if abs(e2x-px) <= 40 and abs(e2y-py) <= 40 and _cry2_timer >= 40:
            
            # 鳴き声
            cry4_sound = mixer.Sound('sounds/cat5.mp3')
            cry4_sound.set_volume(sound_volume)
            cry4_sound.play()

            cry2_flg = 1
            _cry2_timer = 0

    # 餌と接触すると食べる
    if food_flg == 1:

        if abs(e2x-fx) <= 28 and abs(e2y-fy) <= 28 and food2_timer <= 10:

            food2_timer += 1

            e2x = e2x
            e2y = e2y

            eat2_flg = 1

            if food2_timer == 10:

                # 食べる音
                cry2_sound = mixer.Sound('sounds/cat7.mp3')
                cry2_sound.set_volume(sound_volume)
                cry2_sound.play()

                eat2_flg = 0
                food2_timer = 0        

            e2_ani = e2_dir*3 + ANIMATION[timer%4]

        if food2_timer > 10:
            food2_timer = 0

# 敵キャラ３の動き（ランダムの座標遷移）
def move_enemy3():

    global e3x,e3y,e3_ani,e3_dir,cry3_timer,_cry3_timer,cry3_flg,\
        food,food3_timer,eat3_flg

    cry3_timer += 1

    if cry3_timer > 120:

        cry3_sound = mixer.Sound('sounds/cat3.mp3')
        cry3_sound.set_volume(sound_volume)
        cry3_sound.play()

        cry3_timer = 0     

    if food3_timer == 0:    
    
        if e3x%60 == 30 and e3y%60 == 30:

            e3_dir = random.randint(0, 3)

        if e3_dir == DIR_DOWN and e3y < 710:   # 敵キャラの下移動限界のy座標
            
            if  check_wall(e3x , e3y, e3_dir, enemy_speed) == False:
                e3y = e3y + enemy_speed    
        
        if e3_dir == DIR_LEFT and e3x > 30:    # 敵キャラの左移動限界のx座標

            if  check_wall(e3x , e3y, e3_dir, enemy_speed) == False:
                e3x = e3x - enemy_speed
        
        if e3_dir == DIR_RIGHT and e3x < 870:  # 敵キャラの右移動限界のx座標

            if  check_wall(e3x , e3y, e3_dir, enemy_speed) == False:
                e3x = e3x + enemy_speed
                    
        if e3_dir == DIR_UP and e3y > 40:      # 敵キャラの上移動限界のy座標
            
            if  check_wall(e3x , e3y, e3_dir, enemy_speed) == False:        
                e3y = e3y - enemy_speed

        e3_ani = e3_dir*3 + ANIMATION[timer%4]

        # 人間と接触すると鳴く
        if cry3_flg == 1:
            _cry3_timer += 1

            if _cry3_timer == 40:
                cry3_flg = 0

        if abs(e3x-px) <= 40 and abs(e3y-py) <= 40 and _cry3_timer >= 40:
            
            # 鳴き声
            cry4_sound = mixer.Sound('sounds/cat6.mp3')
            cry4_sound.set_volume(sound_volume)
            cry4_sound.play()

            cry3_flg = 1
            _cry3_timer = 0

    # 餌と接触すると食べる
    if food_flg == 1:

        # if abs(e3x-fx) <= 40 and abs(e3y-fy) <= 40 and food3_timer <= 10:
        if abs(e3x-fx) <= 28 and abs(e3y-fy) <= 28 and food3_timer <= 10:            

            food3_timer += 1

            e3x = e3x
            e3y = e3y

            eat3_flg = 1

            if food3_timer == 10:

                # 食べる音
                cry3_sound = mixer.Sound('sounds/cat7.mp3')
                cry3_sound.set_volume(sound_volume)
                cry3_sound.play()

                eat3_flg = 0
                food3_timer = 0        

            e3_ani = e3_dir*3 + ANIMATION[timer%4]

        if food3_timer > 10:
            food3_timer = 0          

# メイン処理
def main():
    global key,koff,timer

    timer = timer + 1

    draw_screen()
    move_player()
    move_enemy1()
    move_enemy2()
    move_enemy3()

    if koff == True:
        key = ""
        koff = False

    root.after(100,main)

root = tkinter.Tk()

# 背景画像
tile = [
    tkinter.PhotoImage(file="images/tile_1.png"),#平地
    tkinter.PhotoImage(file="images/food_1.png"),#餌
    tkinter.PhotoImage(file="images/fence_1.png"),#柵
    tkinter.PhotoImage(file="images/tree_1.png"),#木1
    tkinter.PhotoImage(file="images/tree_2.png"),#木2
    tkinter.PhotoImage(file="images/tree_3.png"),#木3
    tkinter.PhotoImage(file="images/tree_4.png")#木4
]

# メインキャラのアニメーション画像
img_player = [
    tkinter.PhotoImage(file="images/majo_0.png"),#下0～2
    tkinter.PhotoImage(file="images/majo_1.png"),
    tkinter.PhotoImage(file="images/majo_2.png"),    
    tkinter.PhotoImage(file="images/majo_3.png"),#左3～5
    tkinter.PhotoImage(file="images/majo_4.png"),
    tkinter.PhotoImage(file="images/majo_5.png"),
    tkinter.PhotoImage(file="images/majo_6.png"),#右6～8
    tkinter.PhotoImage(file="images/majo_7.png"),
    tkinter.PhotoImage(file="images/majo_8.png"),
    tkinter.PhotoImage(file="images/majo_9.png"),#上9～11
    tkinter.PhotoImage(file="images/majo_10.png"),
    tkinter.PhotoImage(file="images/majo_11.png")
]

# 敵キャラ１のアニメーション画像
img_enemy1 = [
    tkinter.PhotoImage(file="images/cat1_0.png"),#下0～2
    tkinter.PhotoImage(file="images/cat1_1.png"),
    tkinter.PhotoImage(file="images/cat1_2.png"),    
    tkinter.PhotoImage(file="images/cat1_3.png"),#左3～5
    tkinter.PhotoImage(file="images/cat1_4.png"),
    tkinter.PhotoImage(file="images/cat1_5.png"),
    tkinter.PhotoImage(file="images/cat1_6.png"),#右6～8
    tkinter.PhotoImage(file="images/cat1_7.png"),
    tkinter.PhotoImage(file="images/cat1_8.png"),
    tkinter.PhotoImage(file="images/cat1_9.png"),#上9～11
    tkinter.PhotoImage(file="images/cat1_10.png"),
    tkinter.PhotoImage(file="images/cat1_11.png")
]

# 敵キャラ２のアニメーション画像
img_enemy2 = [
    tkinter.PhotoImage(file="images/cat2_0.png"),#下0～2
    tkinter.PhotoImage(file="images/cat2_1.png"),
    tkinter.PhotoImage(file="images/cat2_2.png"),    
    tkinter.PhotoImage(file="images/cat2_3.png"),#左3～5
    tkinter.PhotoImage(file="images/cat2_4.png"),
    tkinter.PhotoImage(file="images/cat2_5.png"),
    tkinter.PhotoImage(file="images/cat2_6.png"),#右6～8
    tkinter.PhotoImage(file="images/cat2_7.png"),
    tkinter.PhotoImage(file="images/cat2_8.png"),
    tkinter.PhotoImage(file="images/cat2_9.png"),#上9～11
    tkinter.PhotoImage(file="images/cat2_10.png"),
    tkinter.PhotoImage(file="images/cat2_11.png")
]

# 敵キャラ３のアニメーション画像
img_enemy3 = [
    tkinter.PhotoImage(file="images/cat3_0.png"),#下0～2
    tkinter.PhotoImage(file="images/cat3_1.png"),
    tkinter.PhotoImage(file="images/cat3_2.png"),    
    tkinter.PhotoImage(file="images/cat3_3.png"),#左3～5
    tkinter.PhotoImage(file="images/cat3_4.png"),
    tkinter.PhotoImage(file="images/cat3_5.png"),
    tkinter.PhotoImage(file="images/cat3_6.png"),#右6～8
    tkinter.PhotoImage(file="images/cat3_7.png"),
    tkinter.PhotoImage(file="images/cat3_8.png"),
    tkinter.PhotoImage(file="images/cat3_9.png"),#上9～11
    tkinter.PhotoImage(file="images/cat3_10.png"),
    tkinter.PhotoImage(file="images/cat3_11.png")
]

root.title("猫牧場  ")
root.resizable(False, False)
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

canvas = tkinter.Canvas(width=900,height=780)  # 背景の大きさ
canvas.pack()

# pygame.mixer.music.set_volume(music_set_volume)
pygame.mixer.init()

main()
root.mainloop()

# pgzrun.go()
