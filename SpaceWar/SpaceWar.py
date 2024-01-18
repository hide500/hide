
# import os
import pygame
import sys
import random
import math
from pygame import mixer
import time

########### 変数定義 ###########

# STARTタイトル
img_title_before = pygame.image.load("img/title.png")           # 画像読み込み
img_title = pygame.transform.rotozoom(img_title_before,0,1.4)   # 画像加工

# ENDタイトル
img_endtitle_before = pygame.image.load("img/gameover.png")           # 画像読み込み
img_endtitle = pygame.transform.rotozoom(img_endtitle_before,0,1.4)   # 画像加工

# CLEARタイトル
img_cleartitle_before = pygame.image.load("img/gameclear.png")            # 画像読み込み
img_cleartitle = pygame.transform.rotozoom(img_cleartitle_before,0,1.4)   # 画像加工

img_cleartitle_1_before = pygame.image.load("img/gameclear1.png")             # 画像読み込み
img_cleartitle_1 = pygame.transform.rotozoom(img_cleartitle_1_before,0,1.1)   # 画像加工

# 背景
img_bg = pygame.image.load("img/universe.png")

# 自機
img_player_before = pygame.image.load('img/player.png')                 # 画像読み込み
img_player = pygame.transform.scale(img_player_before, (70, 70))        # 画像加工
player_rest = pygame.transform.scale(img_player_before, (25, 25))       # 画像加工(残機)

 # 自機弾
img_weapon_before = pygame.image.load('img/bullet.png')                 # 画像読み込み
img_weapon = pygame.transform.scale(img_weapon_before, (70, 70))        # 画像加工

# 敵機（ステージ１）
enemy_ship_1_before = pygame.image.load('img/enemy.png')                # 画像読み込み
enemy_ship_1 = pygame.transform.scale(enemy_ship_1_before, (120, 120))  # 画像加工

# 敵機（ステージ２）
enemy_ship_2_before = pygame.image.load('img/enemy1.png')               # 画像読み込み
enemy_ship_2 = pygame.transform.scale(enemy_ship_2_before, (135, 135))  # 画像加工

# 敵機（ステージ３）
enemy_ship_3_before = pygame.image.load('img/enemy2.png')               # 画像読み込み
enemy_ship_3 = pygame.transform.scale(enemy_ship_3_before, (140, 140))  # 画像加工

# 敵機（ラスボス）
boss_before = pygame.image.load('img/boss.png')               # 画像読み込み
boss = pygame.transform.scale(boss_before, (500, 260))        # 画像加工

# 敵機弾（ステージ１）
enemy_bullet_1_before = pygame.image.load('img/enemy_bullet.png')      # 画像読み込み
enemy_bullet_1 = pygame.transform.scale(enemy_bullet_1_before, (20, 20)) # 画像加工

# 敵機弾（ステージ２）
enemy_bullet_2_before = pygame.image.load('img/enemy_bullet1.png')      # 画像読み込み
enemy_bullet_2 = pygame.transform.scale(enemy_bullet_2_before, (32, 32)) # 画像加工

# 敵機弾（ステージ３）
enemy_bullet_3_before = pygame.image.load('img/enemy_bullet2.png')      # 画像読み込み
enemy_bullet_3 = pygame.transform.scale(enemy_bullet_3_before, (17, 17)) # 画像加工

# 敵機弾（ラスボス）
enemy_bullet_4_before = pygame.image.load('img/boss_bullet.png')        # 画像読み込み
enemy_bullet_4 = pygame.transform.scale(enemy_bullet_4_before, (500, 500)) # 画像加工

# 爆発エフェクト（通常機体）
img_explode = [
    None,
    pygame.image.load("img/bom1.png"), # 爆発1枚目
    pygame.image.load("img/bom1.png"), # 爆発2枚目
    pygame.image.load("img/bom2.png"), # 爆発3枚目
    pygame.image.load("img/bom2.png"), # 爆発4枚目
    pygame.image.load("img/bom2.png"), # 爆発5枚目
    pygame.image.load("img/bom3.png"), # 爆発6枚目
    pygame.image.load("img/bom3.png")  # 爆発7枚目
]

# 爆発エフェクト（ラスボス）
img_explode_boss = [
    None,
    pygame.image.load("img/bossbom1.png"), # 爆発1枚目
    pygame.image.load("img/bossbom1.png"), # 爆発2枚目
    pygame.image.load("img/bossbom1.png"), # 爆発3枚目
    pygame.image.load("img/bossbom1.png"), # 爆発4枚目
    pygame.image.load("img/bossbom1.png"), # 爆発5枚目
    pygame.image.load("img/bossbom2.png"), # 爆発6枚目
    pygame.image.load("img/bossbom2.png"), # 爆発7枚目
    pygame.image.load("img/bossbom2.png"), # 爆発8枚目
    pygame.image.load("img/bossbom2.png"), # 爆発9枚目
    pygame.image.load("img/bossbom2.png"), # 爆発10枚目
    pygame.image.load("img/bossbom2.png"), # 爆発11枚目
    pygame.image.load("img/bossbom2.png"), # 爆発12枚目
    pygame.image.load("img/bossbom3.png"), # 爆発13枚目
    pygame.image.load("img/bossbom3.png"), # 爆発14枚目
    pygame.image.load("img/bossbom3.png"), # 爆発15枚目
    pygame.image.load("img/bossbom3.png"), # 爆発16枚目
    pygame.image.load("img/bossbom3.png"), # 爆発17枚目
    pygame.image.load("img/bossbom3.png"), # 爆発18枚目
    pygame.image.load("img/bossbom4.png"), # 爆発19枚目
    pygame.image.load("img/bossbom4.png"), # 爆発20枚目
    pygame.image.load("img/bossbom4.png"), # 爆発21枚目
    pygame.image.load("img/bossbom4.png"), # 爆発22枚目
    pygame.image.load("img/bossbom4.png"), # 爆発23枚目
    pygame.image.load("img/bossbom4.png"), # 爆発24枚目
    pygame.image.load("img/bossbom4.png"), # 爆発25枚目
    pygame.image.load("img/bossbom5.png"), # 爆発26枚目
    pygame.image.load("img/bossbom5.png"), # 爆発27枚目
    pygame.image.load("img/bossbom5.png"), # 爆発28枚目
    pygame.image.load("img/bossbom5.png"), # 爆発29枚目
    pygame.image.load("img/bossbom5.png"), # 爆発30枚目
    pygame.image.load("img/bossbom6.png"), # 爆発31枚目
    pygame.image.load("img/bossbom6.png"), # 爆発32枚目
    pygame.image.load("img/bossbom6.png"), # 爆発33枚目
    pygame.image.load("img/bossbom6.png"), # 爆発34枚目
    pygame.image.load("img/bossbom6.png"), # 爆発35枚目
    pygame.image.load("img/bossbom7.png"), # 爆発36枚目
    pygame.image.load("img/bossbom7.png"), # 爆発37枚目
    pygame.image.load("img/bossbom7.png"), # 爆発38枚目
    pygame.image.load("img/bossbom7.png"), # 爆発39枚目
    pygame.image.load("img/bossbom7.png"), # 爆発40枚目
    pygame.image.load("img/bossbom8.png"), # 爆発41枚目
    pygame.image.load("img/bossbom8.png"), # 爆発42枚目
    pygame.image.load("img/bossbom8.png"), # 爆発43枚目
    pygame.image.load("img/bossbom8.png"), # 爆発44枚目
    pygame.image.load("img/bossbom8.png")  # 爆発45枚目
]

# インデックス（ゲーム画面の番号）
idx = 0
# idx = 6

# 画面サイズ
wide = 760          # 横サイズ
hight = 860         # 縦サイズ

WHITE = (255,255,255)
bg_y = 0
px = 380            # プレイヤーのX座標
py = 740            # プレイヤーのY座標
bx = 0              # 弾のX座標
by = 0              # 弾のY座標
timer = 0           # タイマー変数

space = 0
score = 0           # 得点
shot_enemy = 0      # 撃墜数
BULLET_MAX = 1000   # 弾の最大値
ENEMY_MAX = 100     # 敵の最大数
ENEMY_BULLET = 1

Launch_angle = 90   # 敵弾の発射角度

stage = 1                 # ステージ
rest = 5                  # 自機の残機
end_flg = 0               # エンディングで使用するフラグ
eship_flg = 0             # 対象を敵機とするフラグ 

music_set_volume = 0.07   # BGMの音量
sound_volume = 0.05       # 効果音の音量

limit_stage = 30          # ステージ１～３の制限時間
limit_boss = 45           # ボス戦の制限時間

# レベル＝normal
rate_stage1_normal = 21   # ステージ１の敵出現フレーム数
rate_stage2_normal = 27   # ステージ２の敵出現フレーム数
rate_stage3_normal = 35   # ステージ３の敵出現フレーム数

# レベル＝easy
rate_stage1_easy = 24     # ステージ１の敵出現フレーム数
rate_stage2_easy = 30     # ステージ２の敵出現フレーム数
rate_stage3_easy = 38     # ステージ３の敵出現フレーム数

# レベル＝hard
rate_stage1_hard = 18     # ステージ１の敵出現フレーム数
rate_stage2_hard = 24     # ステージ２の敵出現フレーム数
rate_stage3_hard = 32     # ステージ３の敵出現フレーム数

# レベル＝super
rate_stage1_super = 15    # ステージ１の敵出現フレーム数
rate_stage2_super = 21    # ステージ２の敵出現フレーム数
rate_stage3_super = 29    # ステージ３の敵出現フレーム数

rate_boss = 10000         # ボス戦の敵出現フレーム数

enemy_bullet_speed_1 = 10 # 敵機弾のスピード(stage1)
enemy_bullet_speed_2 = 11 # 敵機弾のスピード(stage2)
enemy_bullet_speed_3 = 12 # 敵機弾のスピード(stage3)
boss_bullet_speed = 30    # ラスボス弾のスピード（3本用）

bull_n = 0
bull_x =[0]*BULLET_MAX
bull_y =[0]*BULLET_MAX
bull_f =[False]*BULLET_MAX

ebull_n = 0
ebull_x = [0]*ENEMY_MAX
ebull_y = [0]*ENEMY_MAX
ebull_a = [0]*ENEMY_MAX
ebull_f =[False]*ENEMY_MAX
ebull_f2 = [False]*ENEMY_MAX
e_list = [0]*ENEMY_MAX  # 敵機のリスト
e_speed = [0]*ENEMY_MAX # 敵機のスピード
e_HP = [0]*ENEMY_MAX    # 敵機のHP
e_timer = [0]*ENEMY_MAX # 敵機用のタイマー

EFFECT_MAX = 100     # エフェクトの最大数
e_n = 0
e_l = [0]*EFFECT_MAX # エフェクトの対象リスト
e_x = [0]*EFFECT_MAX # エフェクトのX座標
e_y = [0]*EFFECT_MAX # エフェクトのY座標

p_invincible = 0     # 無敵状態を管理する


########### メソッド ###########

# 自機の弾準備
def set_bullet():
    global bull_n
    bull_f[bull_n] = True
    bull_x[bull_n] = px-17
    bull_y[bull_n] = py-17
    bull_n = (bull_n+1)%BULLET_MAX

# 自機の弾発射
def move_bullet(screen):

    for i in range(BULLET_MAX):

        if bull_f[i] == True:
            bull_y[i] = bull_y[i] - 32
            screen.blit(img_weapon,[bull_x[i],bull_y[i]])

            if bull_y[i] < 0:
                bull_f[i] = False

# 自機の動き
def move_player(screen,key):

    global px,py,space,rest,p_invincible,idx,timer,HP,score,shot_enemy,effect_flg,r
    
    if key[pygame.K_UP] == 1:
        py = py - 10
        if py < 20:
            py = 20

    if key[pygame.K_DOWN] == 1:
        py = py + 10
        if py > 800:
            py = 800

    if key[pygame.K_LEFT] == 1:
        px = px - 10
        if px < 10:
            px = 10

    if key[pygame.K_RIGHT] == 1:
        px = px + 10
        if px > 710:
            px = 710
    
    # 弾の発射
    space = (space+1)*key[pygame.K_SPACE]
    
    # 5フレーム毎に弾を飛ばす
    if space%15 == 1:

        # 弾道音
        shot_sound = mixer.Sound('sound/shot.wav')
        shot_sound.set_volume(sound_volume)
        shot_sound.play()

        set_bullet()
    
    # 無敵状態なら点滅させる
    if p_invincible%2 == 0:

        screen.blit(img_player,[px-16,py-16])

    if p_invincible > 0:
        
        # 無敵時は当たり判定を無効にする
        p_invincible = p_invincible - 1
        return
    
    elif idx == 3 or idx == 4 or idx == 5 or idx == 6:
      
      for i in range(ENEMY_MAX):

        if ebull_f[i] == True:

            w = img_enemy[e_list[i]].get_width()
            h = img_enemy[e_list[i]].get_height()

            # r = int((w+h)/4+(32+32)/4)

            # ステージ１～３
            if stage == 1 or stage == 2 or stage == 3:

                r = int((w+h)/4+(32+32)/4)

            # ラスボス戦    
            if stage == 4:

                # r = int((w+h)/4+(250+250)/4)
                
                if h < 500:
                    r = 62
                if h > 500:
                    r = 200
            
            # 自機への当たり判定（敵機、及び敵機弾に接触）
            if distance(ebull_x[i],ebull_y[i],px,py) < r*r:

                # 自機接触のエフェクト座標
                effect(px,py)

                # 自機爆発エフェクトフラグ
                effect_flg = 1

                # 自機接触時の爆発音
                bom_own_sound = mixer.Sound('sound/hit_own.wav')
                bom_own_sound.set_volume(sound_volume)
                bom_own_sound.play()                

                # 自機へのダメージ
                rest = rest - 1

                if rest <= 0:

                    idx = 1
                    timer = 0

                if rest > 0:

                    if p_invincible == 0:

                        # 無敵時間
                        p_invincible = 50

                    # 敵機へのダメージ
                    e_HP[i] = e_HP[i] - 1

                    if e_HP[i] == 0:

                        # 敵機爆発のエフェクト座標
                        effect(px,py)

                        # 敵機爆発エフェクトフラグ
                        effect_flg = 2

                        # ステージ１～３の場合
                        if stage == 1 or stage == 2 or stage == 3:
                        
                            # 効果音
                            bom_enemy_sound = mixer.Sound('sound/hit_enemy.wav')
                            bom_enemy_sound.set_volume(sound_volume)
                            bom_enemy_sound.play()                              

                            # スコア加算
                            if stage == 1:
                                score = score + 10
                            if stage == 2:
                                score = score + 20
                            if stage == 3:
                                score = score + 30                            

                        # ボス戦の場合
                        if stage == 4:

                            # 効果音
                            bom_boss_sound = mixer.Sound('sound/hit_boss.wav')
                            bom_boss_sound.set_volume(sound_volume)
                            bom_boss_sound.play()                              

                            # スコア加算
                            score = score + 100

                        # 自機の撃墜数を加算
                        shot_enemy = shot_enemy + 1                        
                        
                        # 敵機,敵機弾を消去
                        ebull_f[i] = False
                        ebull_f2[i] = False
            
    screen.blit(img_player,[px-16,py-16])


# 敵機の表示
def set_enemy(x,y,a,enemy,speed,HP,etimer):

    global ebull_n

    etimer = 0
    
    while True:
        if ebull_f[ebull_n] == False:
            ebull_f[ebull_n] = True
            ebull_x[ebull_n] = x
            ebull_y[ebull_n] = y
            ebull_a[ebull_n] = a
            e_list[ebull_n] = enemy
            e_speed[ebull_n] = speed
            e_HP[ebull_n] = HP
            e_timer[ebull_n] = etimer
            break
        ebull_n = (ebull_n+1)%ENEMY_MAX

# 敵機の動き
def move_enemy(screen):

    global score,idx,timer,shot_enemy,HP,etimer,i,switch_timer,img_explode,\
        effect_flg,start,sum,px,py,eship_flg,enemy_bullet_speed_1,enemy_bullet_speed_2,\
        enemy_bullet_speed_3,boss_bullet_speed,sound_volume

    for i in range(ENEMY_MAX):

        if ebull_f[i] == True:

            png = e_list[i]

            ebull_x[i] = ebull_x[i] + e_speed[i]*math.cos(math.radians(ebull_a[i]))
            ebull_y[i] = ebull_y[i] + e_speed[i]*math.sin(math.radians(ebull_a[i]))

            # ジグザグ飛行（ステージ１～３）
            if stage == 1 or stage == 2 or stage == 3:

                move_list = [80, 100]

                if stage == 1:
                    switch_timer = 35

                if stage == 2:
                    switch_timer = 40

                if stage == 3:
                    switch_timer = 45
                
                e_timer[i] += 1

                if e_timer[i] > switch_timer:

                    w = img_enemy[e_list[i]].get_width()
                    h = img_enemy[e_list[i]].get_height()

                    eship_flg = 0

                    if w > 100:
                        eship_flg = 1
                    
                    if eship_flg == 1:                        

                        ebull_a[i] = random.choice(move_list)

                        # 敵発動の条件
                        if ebull_y[i] < 560:

                            # 弾セット
                            radian = math.atan2( py - ebull_y[i], px - ebull_x[i] )
                            degree = radian * (180 / math.pi)

                            if stage == 1:
                                set_enemy(ebull_x[i],ebull_y[i],degree,1,enemy_bullet_speed_1,HP,etimer)
                            if stage == 2:
                                set_enemy(ebull_x[i],ebull_y[i],degree,1,enemy_bullet_speed_2,HP,etimer)
                            if stage == 3:
                                set_enemy(ebull_x[i],ebull_y[i],degree,1,enemy_bullet_speed_3,HP,etimer)

                            # 弾発射
                            ebull_f2[i] = True

                            e_timer[i] = 0

                        e_timer[i] = 0

            # ジグザグ飛行（ボス戦）                    
            if stage == 4:

                w = img_enemy[e_list[i]].get_width()
                h = img_enemy[e_list[i]].get_height()                
                
                eship_flg = 0

                if h < 300:
                    eship_flg = 1
                
                if eship_flg == 1:

                    if ebull_x[i] < 190:
                        ebull_x[i] = 190

                    if ebull_x[i] > 570:
                        ebull_x[i] = 570

                move_list = [30, 45, 60, 120, 135, 150]                
                e_timer[i] += 1

                if e_timer[i] > 80:

                    ebull_a[i] = random.choice(move_list)

                    # 弾道音
                    shot_boss_sound = mixer.Sound('sound/shot_boss.wav')
                    shot_boss_sound.set_volume(sound_volume)
                    shot_boss_sound.play()                      

                    # 弾セット
                    radian = math.atan2( py - ebull_y[i], px - ebull_x[i] )
                    degree = radian * (180 / math.pi)
                    set_enemy(ebull_x[i],ebull_y[i],degree,1,boss_bullet_speed,HP,etimer)

                    degree1 = degree -23
                    set_enemy(ebull_x[i],ebull_y[i],degree1,1,boss_bullet_speed,HP,etimer)

                    degree2 = degree +23
                    set_enemy(ebull_x[i],ebull_y[i],degree2,1,boss_bullet_speed,HP,etimer)                    
                    
                    ebull_f2[i] = True                                                            
                    
                    e_timer[i] = 0

                    if ebull_y[i] > 300:

                        move_list = [210, 225, 240, 300, 315, 330]                
                        e_timer[i] += 1
                        ebull_a[i] = random.choice(move_list)

                        if e_timer[i] > 80:

                            # 弾セット
                            radian = math.atan2( py - ebull_y[i], px - ebull_x[i] )
                            degree = radian * (180 / math.pi)
                            set_enemy(ebull_x[i],ebull_y[i],degree,1,boss_bullet_speed,HP,etimer)
                            
                            # 弾発射
                            ebull_f2[i] = True
                            
                            e_timer[i] = 0
                                
                    if ebull_y[i] < 0:

                        move_list = [45, 135]                
                        e_timer[i] += 1
                        ebull_a[i] = random.choice(move_list)

                        if e_timer[i] > 80:

                            # 弾セット
                            radian = math.atan2( py - ebull_y[i], px - ebull_x[i] )
                            degree = radian * (180 / math.pi)
                            set_enemy(ebull_x[i],ebull_y[i],degree,1,boss_bullet_speed,HP,etimer)                            
                            
                            # 弾発射
                            ebull_f2[i] = True
                            
                            e_timer[i] = 0

            # 画面外に敵が消える
            if ebull_x[i] < 20 or \
                ebull_x[i] > 740 or \
                ebull_y[i] < -20 or \
                ebull_y[i] > 840:

                # 敵機,敵機弾を消去
                ebull_f[i] = False
                ebull_f2[i] = False
                
            # 敵機弾以外（自機弾が命中した時）
            if e_list[i] != ENEMY_BULLET:

                w = img_enemy[e_list[i]].get_width()
                h = img_enemy[e_list[i]].get_height()
                r = int((w+h)/4)+8
                
                for n in range(BULLET_MAX):

                    # 敵機への当たり判定
                    if bull_f[n] == True and distance(ebull_x[i]-16,ebull_y[i]-16,bull_x[n],bull_y[n]) < r*r:
                        
                        # 自機弾を消去
                        bull_f[n] = False

                        # 敵機ダメージ
                        e_HP[i] = e_HP[i] - 1

                        if e_HP[i] == 0:
                       
                            # エフェクト発生
                            effect(ebull_x[i],ebull_y[i])

                            # 敵機爆発エフェクトフラグ
                            effect_flg = 2

                            # ステージ１～３
                            if stage == 1 or stage == 2 or stage == 3:
                                
                                # 爆発音
                                bom_enemy_sound = mixer.Sound('sound/hit_enemy.wav')
                                bom_enemy_sound.set_volume(sound_volume)
                                bom_enemy_sound.play()                                 
                                # mixer.Sound('sound/hit_enemy.wav').play()

                                # スコア加算
                                if stage == 1:
                                    score = score + 10
                                if stage == 2:
                                    score = score + 20
                                if stage == 3:
                                    score = score + 30

                            # ボス戦
                            if stage == 4:

                                # 爆発音
                                bom_boss_sound = mixer.Sound('sound/hit_boss.wav')
                                bom_boss_sound.set_volume(sound_volume)
                                bom_boss_sound.play()                                 
                                # mixer.Sound('sound/hit_boss.wav').play()

                                # スコア加算
                                score = score + 100

                            # スコア加算
                            # score = score + 10

                            # 自機の撃墜数を加算
                            shot_enemy = shot_enemy + 1

                            # 敵機,敵機弾を消去
                            ebull_f[i] = False
                            ebull_f2[i] = False

                            # ボス戦
                            if stage == 4:

                                # time.sleep(0.7)

                                # エンディングへ
                                idx = 7

                                # BGM出力
                                pygame.mixer.music.load("sound/ending.mp3")
                                pygame.mixer.music.play(-1)

                                timer = 0
                                start = time.time()           # 開始時間

            rz = pygame.transform.rotozoom(img_enemy[png],-180,1.0)
            screen.blit(rz,[ebull_x[i]-rz.get_width()/2,ebull_y[i]-rz.get_height()/2])


# エフェクトを描画する準備を行う関数
def effect(x,y):

    global e_n

    e_l[e_n] = 1
    e_x[e_n] = x
    e_y[e_n] = y
    e_n = (e_n+1)%EFFECT_MAX

# エフェクトを描画する関数（自機、敵機の爆発）
def draw_effect(screen):

    global effect_flg

    for i in range(EFFECT_MAX):

        if e_l[i] > 0:

            # ステージ１～３
            if stage == 1 or stage == 2 or stage == 3:

                # 自機、敵機爆発のエフェクト画像
                zoom = 0.25
                images = 8
                reduce = 50
                rz = pygame.transform.rotozoom(img_explode[e_l[i]],0,0.25)
                    
            # ボス戦
            if stage == 4:
        
                # 自機爆発のエフェクト画像
                if effect_flg == 1:  
                    zoom = 0.25
                    images = 8
                    reduce = 50
                    rz = pygame.transform.rotozoom(img_explode[e_l[i]],0,zoom)

                # ラスボス爆発のエフェクト画像  
                if effect_flg == 2:
                    zoom = 1.00
                    images = 46
                    reduce = 120
                    rz = pygame.transform.rotozoom(img_explode_boss[e_l[i]],0,zoom)
                    
            # エフェクト処理
            screen.blit(rz,[e_x[i]-reduce,e_y[i]-reduce])
            e_l[i] = e_l[i] + 1

            if e_l[i] == images:
                e_l[i] = 0


# 距離を定義する関数
def distance(x1,y1,x2,y2):
    return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

# 文字表示の関数
def draw_text(screen,x,y,text,size,col):
    
    font = pygame.font.Font(None,size)
    s = font.render(text,True,col)
    x = x - s.get_width()/2
    y = y - s.get_height()/2
    screen.blit(s,[x,y])


########### メイン処理 ###########

def main():

    global t,bg_y,idx,score,rest,p_invincible,px,py,timer,stage,rest,shot_enemy,start,\
            HP,enemy_ship,img_enemy,etimer,enemy_bullet,img_explode,zoom,images,end_flg,\
            music_set_volume,limit_stage,limit_boss,rate_stage1,rate_stage2,rate_stage3,\
            rate_boss,game_revel,easy,normal,hard,menu,Menu,Cursor,cursor,x,y,color,\
            keyup_menudoun_flg,keyup_menuup_flg,menu_down_flg,menu_up_flg

    # 初期化
    pygame.init()

    # タイトル表示
    pygame.display.set_caption("シューティングゲーム")

    # BGM音量
    # pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.set_volume(music_set_volume)

    # BGM出力
    pygame.mixer.music.load("sound/bgm.mp3")
    pygame.mixer.music.play(-1)

    # 全画面の範囲
    screen = pygame.display.set_mode((wide,hight))
    
    clock = pygame.time.Clock()
    
    # カーソルクラス（レベル選択）
    class Cursor():

        MOVE_RANGE = 10
        speed = 1

        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color
            self.left = self.x
            self.right = self.x + self.MOVE_RANGE

        def cursor_update(self):
            self.x += self.speed
            if self.x < self.left or self.x > self.right:
                self.speed = -self.speed

        def cursor_draw(self, screen):
            pygame.draw.polygon(screen, (255, 255, 255), ([self.x, self.y], [self.x, self.y + 20], [self.x + 20, self.y + 10]))            

    # メニュークラス（レベル選択）
    class Menu():

        def __init__(self):
            self.frame = 0
            self.select = 0
            
            self.cursor = Cursor(310, 230, (255, 255, 255))

        def menu_update(self):
            self.frame += 1
            if self.select == 0:
                self.cursor.y = 593
            elif self.select == 1:
                self.cursor.y = 636
            elif self.select == 2:
                self.cursor.y = 676
            elif self.select == 3:
                self.cursor.y = 717                

        def menu_draw(self, screen):
            draw_text(screen,410,603,"normal",40,WHITE)
            draw_text(screen,392,645,"easy",40,WHITE)
            draw_text(screen,395,687,"hard",40,WHITE)
            draw_text(screen,403,727,"super",40,WHITE)
            
            self.cursor.cursor_draw(screen)

    menu = Menu()

    menu_down_flg = 0
    menu_up_flg = 0
    keyup_menudown_flg = 0
    keyup_menuup_flg = 0    
    

    #########################
    # ループ処理
    #########################

    while True:

        timer=timer+1
                
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        bg_y = (bg_y+16)%860

        screen.blit(img_bg,[0,bg_y-860])
        screen.blit(img_bg,[0,bg_y])

        key = pygame.key.get_pressed()


        #########################
        # タイトル画面
        #########################

        if idx == 0:

            screen.blit(img_title,[85,185])

            draw_text(screen,390,530,"PRESS ENTER START",60,WHITE)
            draw_text(screen,270,797,"move: cross key",35,WHITE)
            draw_text(screen,510,797,"shot : space key",35,WHITE)

            menu.menu_update()
            menu.menu_draw(screen)

            # 上十字キー押下
            if key[pygame.K_UP] == 1:

                if menu.select == 3 and menu.select != 2:

                    menu.select -= 1
                    menu_up_flg = 1
                    keyup_menuup_flg = 0

                if menu.select == 2 and keyup_menuup_flg == 1:

                    menu.select -= 1
                    menu_up_flg = 1
                    keyup_menuup_flg = 0

                if menu.select == 1 and keyup_menuup_flg == 1:

                    menu.select -= 1
                    menu_up_flg = 1
                    keyup_menuup_flg = 0                    

            # 下十字キー押下
            if key[pygame.K_DOWN] == 1:

                if menu.select == 0 and menu.select != 1:

                    menu.select += 1
                    menu_down_flg = 1
                    keyup_menudown_flg = 0

                if menu.select == 1 and keyup_menudown_flg == 1:

                    menu.select += 1
                    menu_down_flg = 1
                    keyup_menudown_flg = 0

                if menu.select == 2 and keyup_menudown_flg == 1:

                    menu.select += 1
                    menu_down_flg = 1
                    keyup_menudown_flg = 0                  
                   
            # キーアップ判定
            if event.type == pygame.KEYUP:

                if menu_down_flg == 1:

                    keyup_menudown_flg = 1
                    keyup_menuup_flg = 1
                    menu_down_flg = 0

                if menu_up_flg == 1:

                    keyup_menuup_flg = 1
                    menu_up_flg = 0

            # 選択レベルでパラメータ変更
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:

                if menu.select == 0:

                    # レベル＝normal
                    rate_stage1 = rate_stage1_normal                    
                    rate_stage2 = rate_stage2_normal 
                    rate_stage3 = rate_stage3_normal

                elif menu.select == 1:

                    # レベル＝easy
                    rate_stage1 = rate_stage1_easy
                    rate_stage2 = rate_stage2_easy
                    rate_stage3 = rate_stage3_easy

                elif menu.select == 2:

                    # レベル＝hard
                    rate_stage1 = rate_stage1_hard
                    rate_stage2 = rate_stage2_hard
                    rate_stage3 = rate_stage3_hard

                elif menu.select == 3:

                    # レベル＝super
                    rate_stage1 = rate_stage1_super
                    rate_stage2 = rate_stage2_super
                    rate_stage3 = rate_stage3_super
           
                # ゲームプレイ画面へ（ステージ１）
                idx = 3

                timer = 0                
                # score = 0
                shot_enemy = 0 
                
                px = 380
                py = 740
                rest = 5
                p_invincible = 0

                for i in range(BULLET_MAX):
                    bull_f[i] = False

                for i in range(ENEMY_MAX):
                    ebull_f[i] = False

                HP = 1
                etimer = 0

                enemy_ship = enemy_ship_1
                enemy_bullet = enemy_bullet_1

                # 敵機（配列化）
                img_enemy = [    
                    enemy_ship,   # 敵キャラ画像
                    enemy_bullet  # 敵キャラの弾の画像
                ]
            
                time.sleep(0.7)

                start = time.time()  # 開始時間

                # BGM出力
                pygame.mixer.music.load("sound/bgm.mp3")
                pygame.mixer.music.play(-1)
                

        #########################
        # ゲームオーバー
        #########################
                
        if idx == 1:

            screen.blit(img_endtitle,[65,200])

            draw_text(screen,390,600,"PRESS ENTER RESTART",60,WHITE)
            
            if key[pygame.K_RETURN] == 1:

                # idx = stage + 2 
                idx = 3
                stage = 1
                timer = 0
                score = 0
                shot_enemy = 0
                px = 380
                py = 740
                rest = 5
                HP = 1
                p_invincible = 0

                enemy_ship = enemy_ship_1
                enemy_bullet = enemy_bullet_1

                # 敵機（配列化）
                img_enemy = [    
                    enemy_ship,   # 敵キャラ画像
                    enemy_bullet  # 敵キャラの弾の画像
                ]

                for i in range(BULLET_MAX):
                    bull_f[i] = False

                for i in range(ENEMY_MAX):
                    ebull_f[i] = False
                
                time.sleep(0.7)

                start = time.time()   # 開始時間

                # BGM出力
                pygame.mixer.music.load("sound/bgm.mp3")
                pygame.mixer.music.play(-1)
            

        #########################
        # ステージクリア
        #########################
                
        if idx == 2:

            draw_text(screen,400,400,"STAGE  " + str(stage) + "  CLEAR",100,WHITE)

            # 次のステージへ
            if timer == 200:

                stage = stage + 1                
                idx = stage + 2                

                timer = 0                
                shot_enemy = 0

                px = 380
                py = 740

                p_invincible = 0

                if stage == 2:
                    enemy_ship = enemy_ship_2
                    enemy_bullet = enemy_bullet_2

                if stage == 3:
                    enemy_ship = enemy_ship_3
                    enemy_bullet = enemy_bullet_3

                if stage == 4:
                    enemy_ship = boss
                    enemy_bullet = enemy_bullet_4

                # 敵機（配列化）
                img_enemy = [    
                    enemy_ship,   # 敵キャラ画像
                    enemy_bullet  # 敵キャラの弾の画像
                ]

                for i in range(BULLET_MAX):
                    bull_f[i] = False

                for i in range(ENEMY_MAX):
                    ebull_f[i] = False                    

                    if stage == 2:
                        HP = 2

                    if stage == 3:
                        HP = 3

                    if stage == 4:
                        HP = 50
                
                time.sleep(0.7)

                start = time.time() # 開始時間

                # ボス戦へ
                if idx == 6:

                    # BGM出力
                    pygame.mixer.music.load("sound/bgm1.mp3")
                    pygame.mixer.music.play(-1)

       
        #########################
        # ゲームプレイ（ステージ１）
        #########################
                
        if idx == 3:

            move_player(screen,key)
            move_bullet(screen)

            # xxフレームにつき敵1体出現
            if timer%rate_stage1 == 0:

                set_enemy(random.randint(35,720),-10,80,0,6,HP,etimer)
            
            move_enemy(screen)

            # タイマーセット
            end = time.time()             # 終了時間
            sum = math.floor(end - start) # 合計時間

            # ステージクリアへ
            if sum == limit_stage:

                idx = 2
                timer = 0


        #########################
        # ゲームプレイ（ステージ２）
        #########################
                
        if idx == 4:

            move_player(screen,key)
            move_bullet(screen)

            # xxフレームにつき敵1体出現
            if timer%rate_stage2 == 0:
                         
               set_enemy(random.randint(35,720),-10,80,0,5,HP,etimer)
            
            move_enemy(screen)

            # タイマーセット
            end = time.time()             # 終了時間
            sum = math.floor(end - start) # 合計時間

            # if sum == 25:
            if sum == limit_stage:

                idx = 2
                timer = 0


        #########################
        # ゲームプレイ（ステージ３）
        #########################
                
        if idx == 5:

            move_player(screen,key)
            move_bullet(screen)

            # xxフレームにつき敵1体出現
            if timer%rate_stage3 == 0:
                         
               set_enemy(random.randint(35,720),-10,80,0,4,HP,etimer)
            
            move_enemy(screen)

            # タイマーセット
            end = time.time()             # 終了時間
            sum = math.floor(end - start) # 合計時間

            if sum == limit_stage:

                idx = 2
                timer = 0


        #########################
        # ゲームプレイ（ラスボス）
        #########################
                
        if idx == 6:

            move_player(screen,key)
            move_bullet(screen)

            # xxフレームにつき敵1体出現
            if timer%rate_boss == 0:
                         
               set_enemy(400,-10,80,0,2,HP,etimer)
            
            move_enemy(screen)

            # タイマーセット
            end = time.time()             # 終了時間
            sum = math.floor(end - start) # 合計時間

            if sum == limit_boss:

                idx = 1
                timer = 0

        
        #########################
        # エンディング
        #########################
                
        if idx == 7:

            end = time.time()             # 終了時間
            sum = math.floor(end - start) # 合計時間

            if sum == 4:
                end_flg = 1
            
            # エンディング画面を表示
            if end_flg == 1:
                screen.blit(img_cleartitle,[62,170])
                screen.blit(img_cleartitle_1,[135,430])
                draw_text(screen, 400, 700, "SCORE  " + str(score), 60, WHITE)

            # タイトル画面へ
            if timer == 2000:
                
                idx = 0

                stage = 1
                timer = 0                
                rest = 5
                score = 0
                shot_enemy = 0
                px = 380
                py = 740
                end_flg = 0

                enemy_ship = enemy_ship_1
                enemy_bullet = enemy_bullet_1

                # 敵機（配列化）
                img_enemy = [    
                    enemy_ship,   # 敵キャラ画像
                    enemy_bullet  # 敵キャラの弾の画像
                ]

                p_invincible = 0

                for i in range(BULLET_MAX):
                    bull_f[i] = False

                for i in range(ENEMY_MAX):
                    ebull_f[i] = False
                
                time.sleep(0.7)

       
        #########################
        # 全体処理                
        #########################
                
        draw_effect(screen)

        # ゲームプレイ中のみ体力ゲージとスコアを表示する
        if idx == 3 or idx == 4 or idx == 5 or idx == 6:

            screen.blit(player_rest,(15,15))                                      # 機体表示
            draw_text(screen, 50, 30, str(rest), 30, WHITE)                       # 残機数表示
            draw_text(screen, 230, 30, "STAGE " + str(stage), 30, WHITE)          # ステージ表示
            draw_text(screen, 460, 30, "SCORE " + str(score), 30, WHITE)          # スコア表示
            # draw_text(screen, 680, 30, "SHOOT " + str(shot_enemy), 30, WHITE)   # 撃墜数表示
            draw_text(screen, 680, 30, "TIME " + str(sum), 30, WHITE)             # タイマー表示

        # アップデート
        pygame.display.update()

        # 画面読み込み間隔（増えるほど動きが早くなる）
        clock.tick(50)

if __name__ == "__main__":
    main()