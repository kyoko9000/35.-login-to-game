
#Game betting race by Pygame
#animation's images: gameart2D.com
#buff's images : flaticon.com, iconfider.com
#racer's images : printest.com, opengameart.org
import pygame
import time
import random
from pygame.locals import *
#------------------MINIGAME IMPORT------------------------#
from sys import exit
from pygame.locals import *
from gameRole import *
import random
#------------------MINIGAME IMPORT------------------------#

pygame.init()
screen_height = 800                         #size of game's screen
screen_width = 1300                         #size of game's screen
start_money = 100                           #every player starts with start_money
velocity = 5
background_x = 0
background_y = 0
winner = -1                                 #save the only winner
file_rank_read = open("rank.txt", "r")       #open file rank
rank_list = []*6                            #list to save top 3 highscore(0, 2, 4:Name; 1, 3, 5: Score)
for f in file_rank_read:                    #read file rank
    f = f[:-1]
    rank_list.append(f)
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Fish Race Tournament")
game_icon = pygame.image.load("fish.png")
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
#Sound Effect
button_sound = pygame.mixer.Sound('game_button.mp3')


#Image
racerImg1 = list([pygame.image.load("tank ({}).png".format(i)) for i in range(1,6)])                  #icon character (racer)
racerImg2 = list([pygame.image.load("bulldozer ({}).png".format(i)) for i in range(1,6)]) 
racerImg3 = list([pygame.image.load("car ({}).png".format(i)) for i in range(1,6)]) 
racerImg4 = list([pygame.image.load("char ({}).png".format(i)) for i in range(1,6)]) 
game_title = pygame.image.load("Game_Title.png")
cup = pygame.image.load("cup.png")
cup = pygame.transform.scale(cup,(int(screen_width/20),int(screen_height/13)))
rank1 = pygame.image.load("rank1.png")
rank1 = pygame.transform.scale(rank1,(200, 200))
rank2 = pygame.image.load("rank2.png")
rank2 = pygame.transform.scale(rank2,(200, 200))
rank3 = pygame.image.load("rank3.png")
rank3 = pygame.transform.scale(rank3,(200, 200))
rank_leader = [rank1,rank2,rank3]
cup_posY = 0
start_menu_reverse = pygame.image.load("start_menu_reverse.png")
guide_img = pygame.image.load("guide.png")
game_screen = pygame.image.load("Game_Screen.png")
game_button = pygame.image.load("Game Button.png")
game_button_scale = pygame.transform.scale(game_button,(200, 120))
game_button_click = pygame.transform.scale(game_button, (210, 130))
menu = pygame.image.load("start_menu.png")             #background's list_player, leader_board, start_menu functions
menu = pygame.transform.scale(menu,(screen_width,screen_height))
inputBG = pygame.image.load("input.jpg")
inputBG = pygame.transform.scale(inputBG,(screen_width,screen_height))
leaderBoard = pygame.image.load("leader_board.png")
leaderBoard = pygame.transform.scale(leaderBoard,(screen_width,screen_height))
listPlayer = pygame.image.load("list_player.jpg")
listPlayer = pygame.transform.scale(listPlayer,(screen_width,screen_height))
racerImg = pygame.image.load("racecar.png")
hell_map = pygame.image.load("hellmap.png")
snow_map = pygame.image.load("snowmap.png")
desert_map = pygame.image.load("desertmap.png")
desert_map_icon = pygame.image.load("desertmap_icon.png")
hell_map_icon = pygame.image.load("hellmap_icon.png")
snow_map_icon = pygame.image.load("snowmap_icon.png")
galaxy_map_icon = pygame.image.load("galaxymap_icon.png")
desert_map_icon = pygame.transform.scale(desert_map_icon,(screen_width//3,screen_height//4))
hell_map_icon = pygame.transform.scale(hell_map_icon,(screen_width//3,screen_height//4))
galaxy_map_icon = pygame.transform.scale(galaxy_map_icon,(screen_width//3,screen_height//4))
snow_map_icon = pygame.transform.scale(snow_map_icon,(screen_width//3,screen_height//4))
galaxy_map = pygame.image.load("galaxymap.png")
startImg = pygame.image.load("start.png")
fastImg= pygame.image.load("fast.png")
slowImg= pygame.image.load("slow.png")
endImg= pygame.image.load("end.png")
garden_map = pygame.image.load("garden.png")
garden_map = pygame.transform.scale(garden_map,(screen_width//3,screen_height//4))
ocean_map = pygame.image.load("ocean.png")
ocean_map = pygame.transform.scale(ocean_map,(screen_width//3,screen_height//4))
hell_map = pygame.transform.scale(hell_map,(screen_width//3,screen_height//4))
snow_map = pygame.transform.scale(snow_map,(screen_width//3,screen_height//4))
desert_map = pygame.transform.scale(desert_map,(screen_width//3,screen_height//4))
galaxy_map = pygame.transform.scale(galaxy_map,(screen_width//3,screen_height//4))
#Animation images map 1
ninja = list([pygame.image.load("ninja{}.png".format(i)) for i in range(1,10)])
ninja_count = 9
fninja = list([pygame.image.load("fninja{}.png".format(i)) for i in range(1,11)])
fninja_count = 10
ftemple = list([pygame.image.load("ftemple{}.png".format(i)) for i in range(1,9)])
ftemple_count = 8
temple = list([pygame.image.load("temple{}.png".format(i)) for i in range(1,10)])
temple_count = 9
knight = list([pygame.image.load("knight{}.png".format(i)) for i in range(1,11)])
knight_count = 10
ninja_die = list([pygame.image.load("ninja_die{}.png".format(i)) for i in range(1,11)])
ninja_die_count = 10
fninja_die = list([pygame.image.load("fninja_die{}.png".format(i)) for i in range(1,11)])
fninja_die_count = 10
ftemple_die = list([pygame.image.load("ftemple_die{}.png".format(i)) for i in range(1,11)])
ftemple_die_count = 10
temple_die = list([pygame.image.load("temple_die{}.png".format(i)) for i in range(1,11)])
temple_die_count = 10
knight_die = list([pygame.image.load("knight_die{}.png".format(i)) for i in range(1,11)])
knight_die_count = 10
listAni1 = list([ninja,fninja,temple,ftemple,knight])
maxCount1 = list([ninja_count,fninja_count,temple_count,ftemple_count,knight_count])
stand_img1 = list([pygame.image.load("ninja_stand.png"),pygame.image.load("fninja_stand.png"),pygame.image.load("temple_stand.png"),pygame.image.load("ftemple_stand.png"),pygame.image.load("knight_stand.png")])
die_img1 =list([ninja_die,fninja_die,temple_die,ftemple_die,knight_die])
maxCountDie1 = list([ninja_die_count,fninja_die_count,temple_die_count,ftemple_die_count,knight_die_count])
#Animation images map 2
dino = list([pygame.image.load("dino_run{}.png".format(i)) for i in range(1,9)])
dino_count = 8
noel = list([pygame.image.load("noel_run ({}).png".format(i)) for i in range(1,12)])
noel_count = 11
pump = list([pygame.image.load("pump_run{}.png".format(i)) for i in range(1,9)])
pump_count = 8
robot = list([pygame.image.load("robot_run{}.png".format(i)) for i in range(1,9)])
robot_count = 8
zombie = list([pygame.image.load("zombie_run ({}).png".format(i)) for i in range(1,11)])
zombie_count = 10
dino_die = list([pygame.image.load("dino_die{}.png".format(i)) for i in range(1,9)])
dino_die_count = 8
noel_die = list([pygame.image.load("noel_die{}.png".format(i)) for i in range(1,18)])
noel_die_count = 17
pump_die = list([pygame.image.load("pump_die{}.png".format(i)) for i in range(1,11)])
pump_die_count = 10
robot_die = list([pygame.image.load("robot_die{}.png".format(i)) for i in range(1,11)])
robot_die_count = 10
zombie_die = list([pygame.image.load("zombie_die ({}).png".format(i)) for i in range(1,13)])
zombie_die_count = 12
listAni2 = list([dino,noel,pump,robot,zombie])
maxCount2 = list([dino_count,noel_count,pump_count,robot_count,zombie_count])
stand_img2 = list([pygame.image.load("dino_stand.png"),pygame.image.load("noel_stand.png"),pygame.image.load("pump_stand.png"),pygame.image.load("robot_stand.png"),pygame.image.load("zombie_stand.png")])
die_img2 =list([dino_die,noel_die,pump_die,robot_die,zombie_die])
maxCountDie2 = list([dino_die_count,noel_die_count,pump_die_count,robot_die_count,zombie_die_count])

#-----------------------------------------------------------------------------------
COUNT = [0]*5
COUNT_DIE = [0]*5
die = [0]*5
end = 0
#Animation images
CURVE_X = [int(screen_width/3.75),int(screen_width/1.74),int(screen_width/1.2)]
curve_index = [0]*5
i_speedY = [[1,-1,1],
            [1,-1,1],
            [1,-1,1],
            [1,-1,1],
            [1,-1,1]]
rotate_index = [-1]*5
i_rotate = [[-1,1,1,-1,-1,1],
            [-1,1,1,-1,-1,1],
            [-1,1,1,-1,-1,1],
            [-1,1,1,-1,-1,1],
            [-1,1,1,-1,-1,1]]
start_curve = [0]*5
step = [0]*5
#--------------------------------------
#Kunai
kunai = pygame.image.load("Kunai.png")
fire = pygame.image.load("fire.png")
kunai_pos = [[0,-600,0]]
kunai_pos[0][0] = random.randrange(0,int(4*screen_width/5))
kunai_pos[0][2] = random.randrange(screen_height//300,screen_height//200)
# color

black = (0,0,0)
red = (200,0,0)
green = (16, 171, 38)
blue = (249, 181, 19) # Actually, it's yellow ... LOL !!!
bright_blue = (255, 115, 30)
bright_green = (0,255,0)
bright_red = (255,0,0)
bright_magenta = (200,0,200)
yellow = (249, 181, 19)
magenta = (255,0,255)
white = (255,255,255)
list_color = [bright_red,bright_green,bright_blue,yellow,magenta]
bright_yellow = (200,200,0)

#color
infoPlayer = [['',start_money,0,True],   #initialize players's information (col 1:Name, col 2: money, col 3: chose racer's number, col 4: to consider that players chose their racer or not
              ['',start_money,0,True],
              ['',start_money,0,True],
              ['',start_money,0,True],
              ['',start_money,0,True]]
price = [0]*5                             #init racer's price (max: 5 racer == 5 player)

#random price
for i in range(0,5):                        
    price[i] = random.randrange(30,50)
#random price

inputName = [True,True,True,True,True]   #to consider that players inputted their name or not
inputNumplayer = True                    #to consider that players inputted the number of players or not
numplayer = 0                            # variable to save the number of players
Exit = False                        
leaderboard = False                      #to run leader_board function or not
pause = False                            #to pause when racing or not
def ansRight():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #text here is yours
            screen.blit(menu,(0,0))
            display_text("Right! Here is your ticket","freesansbold.ttf",screen_width//40,white,screen_width/2,screen_height/8)
            #button continue
            button("PLAY AGAIN",screen_width/10,3*screen_height/4,screen_width/6,screen_height/12,bright_green,green,play_again)
            pygame.display.flip()
            clock.tick(60)
   
def ansWrong():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            screen.blit(menu,(0,0))
            display_text("Oh it's wrong! We will meet tomorrow","freesansbold.ttf",screen_width//40,white,screen_width/2,screen_height/8)
            #button quit
            button("See ya!",screen_width/10,3*screen_height/4,screen_width/8,screen_height/12,bright_green,green,quit)
            pygame.display.flip()
            clock.tick(60)

#Can be loaded from Question database
def QuestionForTicket():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #text
            screen.blit(menu,(0,0))
            display_text("Here is your lucky question:","freesansbold.ttf",screen_width//40,white,screen_width/2,screen_height/8)
            display_text("2 + 2 x 2 = ?","freesansbold.ttf",screen_width//40,white,screen_width/2 ,screen_height/8 + 100)

            #MODIFY size of button according to the length of the given string
            button("6",screen_width/10,3*screen_height/4,screen_width/8 +50,screen_height/12,bright_green,green,ansRight)
            button("8",3*screen_width/4,3*screen_height/4,screen_width/8,screen_height/12,bright_blue,blue,ansWrong)
            pygame.display.flip()
            clock.tick(60)
          
def FreeTicket():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #text
            screen.blit(menu,(0,0))
            display_text("You all have run out of money. Do you want to get a free one?","freesansbold.ttf",screen_width//40,white,screen_width/2,screen_height/8)
            #button yes
            button("Why not?",screen_width/10,3*screen_height/4,screen_width/8,screen_height/12,bright_green,green,QuestionForTicket)
            #button i want to quit
            button("Quit now",3*screen_width/4,3*screen_height/4,screen_width/8,screen_height/12,bright_blue,blue,quit)
            pygame.display.flip()
            clock.tick(60)
# function to print name's player to screen after inputting
def change_all():
    global garden_map, hell_map, snow_map, desert_map, galaxy_map, CURVE_X, inputBG,menu,ocean_map,leaderBoard,listPlayer,cup,rank1,rank3,rank_leader,rank2
    '''
    rank2 = pygame.transform.scale(rank2,(int(screen_width/10),int(screen_height/8)))
    rank1 = pygame.transform.scale(rank1,(int(screen_width/10),int(screen_height/8)))
    rank3 = pygame.transform.scale(rank3,(int(screen_width/10),int(screen_height/8)))
    rank_leader = [rank1,rank2,rank3]
    '''
    cup = pygame.transform.scale(cup,(int(screen_width/20),int(screen_height/13)))
    ocean_map = pygame.transform.scale(ocean_map,(screen_width//3,screen_height//4))
    inputBG = pygame.transform.scale(inputBG,(screen_width,screen_height))
    menu = pygame.transform.scale(menu,(screen_width,screen_height))
    leaderBoard = pygame.transform.scale(leaderBoard,(screen_width,screen_height))
    listPlayer = pygame.transform.scale(listPlayer,(screen_width,screen_height))
    CURVE_X = [int(screen_width/3.75),int(screen_width/1.74),int(screen_width/1.2)]
    garden_map = pygame.transform.scale(garden_map,(screen_width//3,screen_height//4))
    hell_map = pygame.transform.scale(hell_map,(screen_width//3,screen_height//4))
    snow_map = pygame.transform.scale(snow_map,(screen_width//3,screen_height//4))
    desert_map = pygame.transform.scale(desert_map,(screen_width//3,screen_height//4))
    galaxy_map = pygame.transform.scale(galaxy_map,(screen_width//3,screen_height//4))
    kunai_pos[0][0] = random.randrange(0,int(4*screen_width/5))
    kunai_pos[0][2] = random.randrange(screen_height//300,screen_height//200)
def guide():
    global menu
    background_x = 0
    background_y = 0
    velocity = 5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            screen.blit(menu,(background_x, background_y))
            screen.blit(start_menu_reverse, (background_x + 1300, background_y - 75))
            screen.blit(menu, (background_x + 2600, background_y))
            if background_x + 2600 <= 0:
                background_x = 0
            background_x -= velocity
            screen.blit(guide_img, (0, 0))
            
        button(" BACK",20,720,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
        pygame.display.flip()   
        clock.tick(60)
def minigame():
    global menu
    # -------------------------------------MINIGAME--------------------------------------------------------#
    screen = pygame.display.set_mode((480, 800))
    # Game Sound
    bullet_sound = pygame.mixer.Sound('resources/sound/bullet.wav')
    enemy1_down_sound = pygame.mixer.Sound('resources/sound/enemy1_down.wav')
    game_over_sound = pygame.mixer.Sound('resources/sound/game_over.wav')
    bullet_sound.set_volume(0.3)
    enemy1_down_sound.set_volume(0.3)
    game_over_sound.set_volume(0.3)
    pygame.mixer.music.load('resources/sound/game_music.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    # Resource
    background = pygame.image.load('resources/image/background.png').convert()
    game_over = pygame.image.load('resources/image/gameover.png')

    filename = 'resources/image/shoot.png'
    plane_img = pygame.image.load(filename)

    # 设置玩家相关参数
    player_rect = []
    player_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家精灵图片区域
    player_rect.append(pygame.Rect(165, 360, 102, 126))
    player_rect.append(pygame.Rect(165, 234, 102, 126))     # 玩家爆炸精灵图片区域
    player_rect.append(pygame.Rect(330, 624, 102, 126))
    player_rect.append(pygame.Rect(330, 498, 102, 126))
    player_rect.append(pygame.Rect(432, 624, 102, 126))
    player_pos = [200, 600]
    player = Player(plane_img, player_rect, player_pos)

    # 定义子弹对象使用的surface相关参数
    bullet_rect = pygame.Rect(1004, 987, 9, 21)
    bullet_img = plane_img.subsurface(bullet_rect)

    # 定义敌机对象使用的surface相关参数
    enemy1_rect = pygame.Rect(534, 612, 57, 43)
    enemy1_img = plane_img.subsurface(enemy1_rect)
    enemy1_down_imgs = []
    enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
    enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
    enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
    enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

    enemies1 = pygame.sprite.Group()

    # 存储被击毁的飞机，用来渲染击毁精灵动画
    enemies_down = pygame.sprite.Group()

    shoot_frequency = 0
    enemy_frequency = 0

    player_down_index = 16

    score = 0

    clock = pygame.time.Clock()

    running = True

    # -------------------------------------MINIGAME--------------------------------------------------------#
    running = True
    while running:
        # 控制游戏最大帧率为60
        clock.tick(45)

        # 控制发射子弹频率,并发射子弹
        if not player.is_hit:
            if shoot_frequency % 15 == 0:
                bullet_sound.play()
                player.shoot(bullet_img)
            shoot_frequency += 1
            if shoot_frequency >= 15:
                shoot_frequency = 0

        # 生成敌机
        if enemy_frequency % 50 == 0:
            enemy1_pos = [random.randint(0, 480 - enemy1_rect.width), 0]
            enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
            enemies1.add(enemy1)
        enemy_frequency += 2
        if enemy_frequency >= 100:
            enemy_frequency = 0

        # 移动子弹，若超出窗口范围则删除
        for bullet in player.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                player.bullets.remove(bullet)

        # 移动敌机，若超出窗口范围则删除
        for enemy in enemies1:
            enemy.move()
            # 判断玩家是否被击中
            if pygame.sprite.collide_circle(enemy, player):
                enemies_down.add(enemy)
                enemies1.remove(enemy)
                player.is_hit = True
                game_over_sound.play()
                break
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies1.remove(enemy)

        # 将被击中的敌机对象添加到击毁敌机Group中，用来渲染击毁动画
        enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
        for enemy_down in enemies1_down:
            enemies_down.add(enemy_down)

        # 绘制背景
        screen.fill(0)
        screen.blit(background, (0, 0))

        # 绘制玩家飞机
        if not player.is_hit:
            screen.blit(player.image[player.img_index], player.rect)
            # 更换图片索引使飞机有动画效果
            player.img_index = shoot_frequency // 8
        else:
            player.img_index = player_down_index // 8
            screen.blit(player.image[player.img_index], player.rect)
            player_down_index += 1
            if player_down_index > 47:
                running = False

        # 绘制击毁动画
        for enemy_down in enemies_down:
            if enemy_down.down_index == 0:
                enemy1_down_sound.play()
            if enemy_down.down_index > 7:
                enemies_down.remove(enemy_down)
                score += 1
                continue
            screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
            enemy_down.down_index += 1

        # 绘制子弹和敌机
        player.bullets.draw(screen)
        enemies1.draw(screen)

        # Score Display
        score_font = pygame.font.Font(None, 50)
        score_text = score_font.render(str(score), True, (255, 255, 255))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(score_text, text_rect)

        # 更新屏幕
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        # 监听键盘事件
        key_pressed = pygame.key.get_pressed()
        # Player Control
        if not player.is_hit:
            if key_pressed[K_w] or key_pressed[K_UP]:
                player.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                player.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                player.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                player.moveRight()

    # End Game - Total Score Display
    i = 0
    while i < numplayer:
            display_text("{} remains {} $!".format(infoPlayer[i][0],infoPlayer[i][1]),"freesansbold.ttf",(screen_width+screen_height)//60,blue,screen_width/2,(i+1)*screen_height/100)
            pygame.display.flip()
            i += 1
    font = pygame.font.Font(None, 40)
    text = font.render('SCORE: '+ str(score), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    screen.blit(game_over, (0, 0))
    screen.blit(text, text_rect)
   
    #info_player[] start_money += score

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        button(" BACK",155,470,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
        pygame.display.update()


def minScreen():
    global screen_height, screen_width
    screen_height = 400
    screen_width = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    change_all()
    start_menu()
def mediumScreen():
    global screen_height, screen_width
    screen_height = 600
    screen_width = 800
    screen = pygame.display.set_mode((screen_width,screen_height))
    change_all()
    start_menu()
def maxScreen():
    global screen_height, screen_width
    screen_height = 800
    screen_width = 1300
    screen = pygame.display.set_mode((screen_width,screen_height))
    change_all()
    start_menu()
''' def screen_setting():
    global menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(menu,(0,0))
        button("1300x800",3*screen_width/4,screen_height/2,screen_width/8,screen_height/12,bright_red,red,maxScreen)
        button("800x600",3*screen_width/8,screen_height/2,screen_width/4,screen_height/12,bright_red,red,mediumScreen)
        button("600x400",screen_width/10,screen_height/2,screen_width/8,screen_height/12,bright_green,green,minScreen)
        pygame.display.flip()
        clock.tick(60)
'''        
def print_name(text):
    font = pygame.font.SysFont(None,screen_width//30)
    Text = font.render(text,True,white)
    screen.blit(Text,(screen_width/2.5,35*screen_height/40))
# function print text to screen
def display_text(text, type, size, color, x, y):
    font = pygame.font.Font(type, size)
    textSuft = font.render(text, True, color)
    textRect = textSuft.get_rect()
    textRect.center = ((x,y))
    screen.blit(textSuft,textRect)
# function to draw a button to screen with the link to the next function when click
def button(msg,x,y,w,h,ac,iac,action = None):   # x, y coordinate, w: width, h: height, ac: active when mouse's position inside button, iac: inactive when mouse's position outside button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        screen.blit(game_button_click, (x - 23, y - 30))
        #pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] != 0:
            pygame.mixer.Sound.play(button_sound)
            action()
    else :
        screen.blit(game_button_scale, (x - 16, y - 25))
        #pygame.draw.rect(screen,iac,(x,y,w,h))
    display_text(msg,"freesansbold.ttf",screen_width//40,black,x + w//2, y+ h//2)
#Continue function: start when the racing ended 
def Continue():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1)
    global numplayer, winner,COUNT,curve_index, rotate_index,step,start_curve,end,COUNT_DIE,die,cup_posY
    cup_posY = 0
    COUNT_DIE = [0]*5
    die = [0]*5
    end =5
    COUNT = [0]*5
    curve_index = [0]*5
    rotate_index = [-1]*5
    start_curve = [0]*5
    step = [0]*5
    for i in range(0,numplayer):    #to reset players's chose racer
        infoPlayer[i][3] = True
    winner = -1                    # reset the winner
    #update file rank
    file_rank_write =open("rank.txt","w")
    for i in range(0,6):
        file_rank_write.write(str(rank_list[i])+"\n")
    file_rank_write.close()
    #update file rank
    input_and_map()             #and continue choosing racer and playing
#arrange infoPlayer following with money they have (from large to small)
def arrangeFLTS():
    global infoPlayer,numplayer
    for i in range(0,numplayer-1):
        for j in range(i+1,numplayer):
            if infoPlayer[i][1] < infoPlayer[j][1]:
                infoPlayer[i],infoPlayer[j]=infoPlayer[j],infoPlayer[i]
#Remove players who lost all their money
def remove_gameover(x):
    global numplayer, infoPlayer
    for j in range(x,numplayer-1):
        infoPlayer[j] = infoPlayer[j+1]
    numplayer -=1
#function starts when racing ended
def play_again():
    global numplayer, winner,COUNT,curve_index, rotate_index,step,start_curve,end,COUNT_DIE,die,cup_posY, inputName,infoPlayer, inputNumplayer
    cup_posY = 0
    COUNT_DIE = [0]*5
    die = [0]*5
    end =5
    COUNT = [0]*5
    curve_index = [0]*5
    rotate_index = [-1]*5
    start_curve = [0]*5
    step = [0]*5
    infoPlayer = [['',start_money,0,True],   #initialize players's information (col 1:Name, col 2: money, col 3: chose racer's number, col 4: to consider that players chose their racer or not
              ['',start_money,0,True],
              ['',start_money,0,True],
              ['',start_money,0,True],
              ['',start_money,0,True]]
    inputName = [True,True,True,True,True]   #to consider that players inputted their name or not
    inputNumplayer = True                    #to consider that players inputted the number of players or not
    input_and_map()
def list_player():
    global numplayer,infoPlayer,price,listPlayer
    arrangeFLTS()
    #re-random racer's price
    for i in range(0,5):    
        price[i] = random.randrange(30,50)                                                        
    i = 0   #just var index
    count = 0   #just to align
    screen.blit(listPlayer,(0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        while i < numplayer:
            check = 1
            # update rank_list, consider new highscore or gameover, and print list's players after the race
            for j in range(0,3):
                if infoPlayer[i][1] > int(rank_list[2*j+1]):
                    display_text("{} remains {} $!TOP {} in LEADERBOARD".format(infoPlayer[i][0],infoPlayer[i][1],j+1),"freesansbold.ttf",(screen_width+screen_height)//60,blue,screen_width/2,(i+1)*screen_height/8)
                    check = 0
                    rank_list[2*j] = infoPlayer[i][0]
                    rank_list[2*j+1] = infoPlayer[i][1]
                    pygame.display.flip()
                    break
            if check == 1:
                if infoPlayer[i][1] == 0:
                    display_text("{} remains {} $! - GAMEOVER".format(infoPlayer[i][0],infoPlayer[i][1]),"freesansbold.ttf",(screen_width+screen_height)//60,blue,screen_width/2,(i+count+1)*screen_height/8)
                    remove_gameover(i)
                    i-=1
                    count +=1
                    pygame.display.flip()
                else:
                    display_text("{} remains {} $!".format(infoPlayer[i][0],infoPlayer[i][1]),"freesansbold.ttf",(screen_width+screen_height)//60,blue,screen_width/2,(i+1)*screen_height/8)
                    pygame.display.flip()
            i+=1
        button("CONTINUE",screen_width/10,3*screen_height/4,screen_width/7,screen_height/12,bright_green,green,Continue)    # button choose Continue function
        button("QUIT",3*screen_width/4,3*screen_height/4,screen_width/8,screen_height/12,(255, 115, 30),blue,quit)               # button choose quit
        if numplayer == 0:
            display_text("GAME OVER !!!","freesansbold.ttf",int(screen_width/20),bright_red,int(screen_width/2),int(screen_height/2))
            FreeTicket()
        pygame.display.flip()
        clock.tick(60)
#function to show the leaderboard 
def leader_board():
    global leaderBoard,rank_leader
    background_x = 0
    background_y = 0
    velocity = 5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            screen.blit(menu,(background_x, background_y))
            screen.blit(start_menu_reverse, (background_x + 1300, background_y - 75))
            screen.blit(menu, (background_x + 2600, background_y))
            if background_x + 2600 <= 0:
                background_x = 0
            background_x -= velocity
            screen.blit(game_screen, (0, 0))
            rank = 1
            ''''''
            screen.blit(rank1, (200, 200))
            screen.blit(rank2, (200, 350))
            screen.blit(rank3, (200, 500))
            display_text("TOP {}: ".format(rank)+rank_list[0], "freesansbold.ttf", 35,black, 650, 300) 
            display_text(" - Money: " + rank_list[1],"freesansbold.ttf", 35,black, 1000, 300)
            display_text("TOP {}: ".format(rank + 1)+rank_list[2], "freesansbold.ttf", 35,black, 650, 450)
            display_text(" - Money: " + rank_list[3],"freesansbold.ttf", 35,black, 1000,  450)
            display_text("TOP {}: ".format(rank + 2)+rank_list[4], "freesansbold.ttf", 35,black, 650, 600)
            display_text(" - Money: " + rank_list[5],"freesansbold.ttf", 35,black, 1000,  600)
            #for i in range(0,5,2):
                #screen.blit(rank_leader[i//2],(screen_width//10,int((i+1)*screen_height/8)))
                #display_text("TOP {}: ".format(rank)+rank_list[i]+ " - Money: " + rank_list[i+1],"freesansbold.ttf",(screen_height+screen_width)//(40+i*5),black,screen_width/2,  (i+1)*50)
                #rank +=1
        button(" BACK",20,720,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
        pygame.display.flip()   
        clock.tick(60)
#function to choose racer (1 - 5)
def choose_racer(i):
    global infoPlayer
    num =""
    background_x = 0
    background_y = 0
    velocity = 5
    while infoPlayer[i][3]:
        screen.blit(menu, (background_x, background_y))
        screen.blit(start_menu_reverse, (background_x + 1300, background_y - 75))
        screen.blit(menu, (background_x + 2600, background_y))
        if background_x + 2600 <= 0:
            background_x = 0
        background_x -= velocity
        screen.blit(game_screen, (0, 0))
        button(" BACK",20,720,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
        display_text("Racer 1 - Price: {}$".format(price[0]),"freesansbold.ttf",(screen_width+screen_height)//60,black,screen_width/2,250)
        display_text("Racer 2 - Price: {}$".format(price[1]),"freesansbold.ttf",(screen_width+screen_height)//60,black,screen_width/2,320)
        display_text("Racer 3 - Price: {}$".format(price[2]),"freesansbold.ttf",(screen_width+screen_height)//60,black,screen_width/2,390)
        display_text("Racer 4 - Price: {}$".format(price[3]),"freesansbold.ttf",(screen_width+screen_height)//60,black,screen_width/2,460)
        display_text("Racer 5 - Price: {}$".format(price[4]),"freesansbold.ttf",(screen_width+screen_height)//60,black,screen_width/2,530)
        display_text("Please choose your racer, {}!".format(infoPlayer[i][0]),"freesansbold.ttf",40,black,screen_width/2,3*screen_height/4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    num +=  '0'
                elif event.key == pygame.K_1:
                    num +=  '1'
                elif event.key == pygame.K_2:
                    num +=  '2'
                elif event.key == pygame.K_3:
                    num +=  '3'
                elif event.key == pygame.K_4:
                    num +=  '4'
                elif event.key == pygame.K_5:
                    num +=  '5'
                elif event.key == pygame.K_6:
                    num +=  '6'
                elif event.key == pygame.K_7:
                    num +=  '7'
                elif event.key == pygame.K_8:
                    num +=  '8'
                elif event.key == pygame.K_9:
                    num +=  '9'
                elif event.key == pygame.K_BACKSPACE:
                    num = num[:-1]
                elif event.key == pygame.K_RETURN:      #press Enter
                    if(int(num)<=5):
                        infoPlayer[i][2] = int(num)
                        infoPlayer[i][3] = False
        display_text(num,"freesansbold.ttf",40,black,screen_width/2,680)
        pygame.display.update()
        clock.tick(60)
        if not infoPlayer[i][3]:    #when press Enter, call input_and_map function
            input_and_map()
#function to input the number of player
def input_numplayer():
    global numplayer,inputNumplayer,inputBG
    num =""
    while inputNumplayer:
        screen.blit(inputBG,(0,0))
        button(" BACK",20,720,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
        display_text("How many players? (1-5)","freesansbold.ttf",40,blue,screen_width/2,3*screen_height/4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    num +=  '0'
                elif event.key == pygame.K_1:
                    num +=  '1'
                elif event.key == pygame.K_2:
                    num +=  '2'
                elif event.key == pygame.K_3:
                    num +=  '3'
                elif event.key == pygame.K_4:
                    num +=  '4'
                elif event.key == pygame.K_5:
                    num +=  '5'
                elif event.key == pygame.K_6:
                    num +=  '6'
                elif event.key == pygame.K_7:
                    num +=  '7'
                elif event.key == pygame.K_8:
                    num +=  '8'
                elif event.key == pygame.K_9:
                    num +=  '9'
                elif event.key == pygame.K_BACKSPACE:
                    num = num[:-1]
                elif event.key == pygame.K_RETURN:      # Enter == Return
                    if(int(num)<=5):
                        numplayer = int(num)
                        inputNumplayer = False
        display_text(num,"freesansbold.ttf",35,blue,screen_width/2,35*screen_height/40)
        pygame.display.update()
        clock.tick(60)
        if not inputNumplayer:          #when press Enter, call input_and_map function
            input_and_map()
#function to input name of players
def input_name(i):
    global inputName,numplayer, inputBG
    str =""
    while inputName[i]:
        screen.blit(inputBG,(0,0))
        button(" BACK",20,720,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
        display_text("Player_{}'s Name?".format(i+1),"freesansbold.ttf",screen_width//40,blue,screen_width/2,3*screen_height/4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    str +=  '0'
                elif event.key == pygame.K_1:
                    str +=  '1'
                elif event.key == pygame.K_2:
                    str +=  '2'
                elif event.key == pygame.K_3:
                    str +=  '3'
                elif event.key == pygame.K_4:
                    str +=  '4'
                elif event.key == pygame.K_5:
                    str +=  '5'
                elif event.key == pygame.K_6:
                    str +=  '6'
                elif event.key == pygame.K_7:
                    str +=  '7'
                elif event.key == pygame.K_8:
                    str +=  '8'
                elif event.key == pygame.K_9:
                    str +=  '9'
                elif event.key == pygame.K_a:
                    str +=  'a'
                elif event.key == pygame.K_b:
                    str +=  'b'
                elif event.key == pygame.K_c:
                    str +=  'c'
                elif event.key == pygame.K_d:
                    str +=  'd'
                elif event.key == pygame.K_e:
                    str +=  'e'
                elif event.key == pygame.K_f:
                    str +=  'f'
                elif event.key == pygame.K_g:
                    str +=  'g'
                elif event.key == pygame.K_h:
                    str +=  'h'
                elif event.key == pygame.K_i:
                    str +=  'i'
                elif event.key == pygame.K_j:
                    str +=  'j'
                elif event.key == pygame.K_k:
                    str +=  'k'
                elif event.key == pygame.K_l:
                    str +=  'l'
                elif event.key == pygame.K_m:
                    str +=  'm'
                elif event.key == pygame.K_n:
                    str +=  'n'
                elif event.key == pygame.K_o:
                    str +=  'o'
                elif event.key == pygame.K_p:
                    str +=  'p'
                elif event.key == pygame.K_q:
                    str +=  'q'
                elif event.key == pygame.K_r:
                    str +=  'r'
                elif event.key == pygame.K_s:
                    str +=  's'
                elif event.key == pygame.K_t:
                    str +=  't'
                elif event.key == pygame.K_u:
                    str +=  'u'
                elif event.key == pygame.K_v:
                    str +=  'v'
                elif event.key == pygame.K_w:
                    str +=  'w'
                elif event.key == pygame.K_x:
                    str +=  'x'
                elif event.key == pygame.K_y:
                    str +=  'y'
                elif event.key == pygame.K_z:
                    str +=  'z'
                elif event.key == pygame.K_SPACE:
                    str += ' '
                elif event.key == pygame.K_BACKSPACE:
                    str = str[:-1]
                elif event.key == pygame.K_RETURN:      # Enter == Return
                    infoPlayer[i][0] = str
                    inputName[i] = False
        #print_name(str) 
        display_text(str,"freesansbold.ttf",35,blue,screen_width/2,35*screen_height/40)
        pygame.display.flip()
        clock.tick(60)
        if not inputName[i]:                # when Return, call input_and_map function
            input_and_map()
# buff icon for racer
# finish = screen_width - posx_object (x coordinate), posx_object: x coordinate's racer
def magic(Images,Type,finish,speed,posx_object,posx_magic,posy_magic):      # posx_magi : x coordinate's racer, posy_magic: y coordinate's racer
    if posx_object < posx_magic:                                            # if racer does not cross over the buff, show the buff to screen           
        if Type>=0 and Type <=3 :
            screen.blit(Images[2],(posx_magic,posy_magic))
        elif Type>=4 and Type <=17 :
            screen.blit(Images[3],(posx_magic,posy_magic))
        elif Type == 18 :
            screen.blit(Images[0],(posx_magic,posy_magic))
        elif Type == 19 :
            screen.blit(Images[1],(posx_magic,posy_magic))
    else:                                                                   # if racer crosses over the buff, change its speed and position x coodinate
        if Type>=0 and Type <=3:
            return (speed/1.5), posx_object
        elif Type>=4 and Type <= 17:
            return speed*1.3, posx_object
        elif Type == 18 :
            return speed, 0
        elif Type == 19 :
            return speed, finish
# blit racer image to screen
def racer(Racer,x,y,w,h):       #w: width, h: height, Racer : racer's image
     Racer = pygame.transform.scale(Racer,(w,h))
     screen.blit(Racer,(x,y))
#function to continue the race
def unpaused() :
    global pause
    pause = False
#pause the race
def paused():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display_text("PAUSE","freesansbold.ttf",(screen_height+screen_width)//8,black,screen_width/2,screen_height/3)
        button("CONTINUE",560, 430,150,screen_height/12,(255, 115, 30),(249, 181, 19),unpaused) #Unpause the race 
        if pause:
            button("QUIT",560, 670,screen_width/8,screen_height/12,bright_green,(16, 171, 38),quit)       #quit the game when click the button
        pygame.display.flip()
        clock.tick(60)
def game_loop(Map,Racer,fisrt_lane,lane_height,row_space): # Map: map's background, Racer: racer's image, first_lane: y coordinate to print first Racer thorough the race, row_space: the space between two lane
    pygame.mixer.music.load("racing.wav")
    pygame.mixer.music.play(0)
    #background_x = 0
    #background_y = 0
    #velocity = 0.7
    global winner, pause, numplayer, startImg, fastImg, slowImg, endImg,cup_posY,cup
    object_width = screen_width//15         # Racer Image's width
    magic_width = object_width//1           # Buff Image's width
    finish = screen_width - object_width    # x coordinate at that all Racer Image stops
    start = 0                               # variable to run if statement to stop 1 sec before the race
    #Load Buff's images and scale them 
    startImg = pygame.transform.scale(startImg,(magic_width,lane_height))
    endImg = pygame.transform.scale(endImg,(magic_width,lane_height))
    fastImg = pygame.transform.scale(fastImg,(magic_width,lane_height))
    slowImg = pygame.transform.scale(slowImg,(magic_width,lane_height))
    Images = [startImg,endImg,slowImg,fastImg]
    #Load Buff's images and scale them
    posY_space = lane_height + row_space        #space between two Racer Images's y coordinate
    pos = [0]*5                                 #Position (x coordinate) of Racer Image
    speed = [0]*5                               # Speed of Racer
    matrix = [[0,0,0,0,0,0,0],                  # five rows == 5 racer, column 1: the number of buff for racer 1..., col 2->4: type of buff (1-10), col 5->7: position_x of each buff
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]
    for i in range(0,5):
        matrix[i][0] = random.randrange(1,3)    #number of buff of each lane
        for k in range(1,matrix[i][0]+1,1):                #type buff 
            matrix[i][k] = random.randrange(0,20)
        for k in range(1,matrix[i][0]+1,1):
            matrix[i][k+3] = random.randrange(object_width,finish) # postion_x of each buff
    for i in range(0,5):                                                    #Random speed for Racer
        speed[i] = random.randrange(1, 2)
    Map = pygame.transform.scale(Map,(screen_width,screen_height))
    #The race loop
    while not pause:
        count = 0       #count the number of racer who has finished the race
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    pause = True
                    paused()
        screen.blit(Map,(background_x,background_y))
        #screen.blit(Map,(background_x + 1300,background_y))
        #if background_x + 1300 <= 0:
        #    background_x = 0
        # background_x -= velocity
        for i in range(0,5):
            if pos[i] >= finish:
                if winner == -1:
                    cup_posY =fisrt_lane+i*posY_space
                    pygame.mixer.music.load("win.mp3")
                    pygame.mixer.music.play(0)
                    winner = i + 1          # save the first Racer has finished the race
                speed[i] = 0
                racer(Racer[i],finish,fisrt_lane+i*posY_space,object_width,lane_height)
                count += 1                      
            else:
                racer(Racer[i],pos[i],fisrt_lane+i*posY_space,object_width,lane_height)
                pos[i]+=speed[i]
                if pos[i]>= finish:
                    if winner == -1:
                        cup_posY =fisrt_lane+i*posY_space
                        pygame.mixer.music.load("win.mp3")
                        pygame.mixer.music.play(0)
                        winner = i + 1          # save the first Racer has finished the race
                #To show buff to screen and return speed, position of racer
                if matrix[i][0] != 0:
                    if pos[i] < matrix[i][matrix[i][0]+3]:      #if position's racer < position's buff (x coordinate), show the buff images
                        magic(Images,matrix[i][matrix[i][0]],finish,speed[i],pos[i],matrix[i][matrix[i][0]+3],fisrt_lane+i*posY_space)
                    else:                                       #else return speed, position of racer which buff gave
                        speed[i],pos[i] = magic(Images,matrix[i][matrix[i][0]],finish,speed[i],pos[i],matrix[i][matrix[i][0]+3],fisrt_lane+i*posY_space)
                        matrix[i][0] -= 1
        if cup_posY != 0:
            screen.blit(cup,(finish-screen_width/20,cup_posY))
        if start == 0: 
               start +=1
               time.sleep(1)
        # if 5 Racer all completed the race, consider who won the game after the race
        if count == 5:
            i=0
            while i < numplayer:
                if infoPlayer[i][2] == winner:
                    infoPlayer[i][1] += price[winner-1]
                else:
                    infoPlayer[i][1] -= price[infoPlayer[i][2]-1]
                    if infoPlayer[i][1] < 0:
                        infoPlayer[i][1] = 0
                i+=1
            time.sleep(1)
            # call list_player function when the race ended
            list_player()
            break
        pygame.display.flip()
        clock.tick(60)
def animation_racer(Images, count, x, y, w, h):
    Images[count] = pygame.transform.scale(Images[count],(w,h))
    screen.blit(Images[count],(x,y))
'''
def game_loop_curve(Map,char,FRAMES_COUNT,die_img,stand_img,kunai,maxCountDie):
    copy1 = list(char[0])
    copy2 = list(char[1])
    copy3 = list(char[2])
    copy4 = list(char[3])
    copy5 = list(char[4])
    copy = list([copy1,copy2,copy3,copy4,copy5])
    pygame.mixer.music.load("racing.wav")
    pygame.mixer.music.play(-1)
    global winner, pause, numplayer, startImg, fastImg, slowImg, endImg, COUNT,end,kunai_pos,COUNT_DIE,die,cup,cup_posY
    start = 0                               # variable to run if statement to stop 1 sec before the race
    Map = pygame.transform.scale(Map,(screen_width,screen_height))
    #pygame.mixer.music.load("bb.mp3")
    #pygame.mixer.music.play(0)
    object_width = screen_width//15         # Racer Image's width
    magic_width = object_width            # Buff Image's width
    finish = screen_width - object_width    # x coordinate at that all Racer Image stops2
    #Load Buff's images and scale them 
    startImg = pygame.transform.scale(startImg,(magic_width,int(screen_height/18.75)))
    endImg = pygame.transform.scale(endImg,(magic_width,int(screen_height/18.75)))
    fastImg = pygame.transform.scale(fastImg,(magic_width,int(screen_height/18.75)))
    slowImg = pygame.transform.scale(slowImg,(magic_width,int(screen_height/18.75)))
    Images = [startImg,endImg,slowImg,fastImg]
    #Load Buff's images and scale them
    posX = [0]*5                                 #Position (x coordinate) of Racer Image
    posY = [0]*5
    for i in range(0,5):
        posY[i] = int(screen_height*(1/18+i/5.37))
    speed = [0]*5                               # Speed of Racer
    matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0],                  # five rows == 5 racer, column 1: the number of buff for racer 1..., col 2->4: type of buff (1-10), col 5->7: position_x of each buff
              [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for i in range(0,5):
        matrix[i][0] = 4    #number of buff of each lane
        for k in range(1,5):                #type buff 
            matrix[i][k] = random.randrange(0,18)
        matrix[i][8] = random.randrange(object_width*3,int(screen_width*0.28)) # postion_x of each buff
        matrix[i][7] = random.randrange(int(screen_width*0.29),int(screen_width*0.57)) # postion_x of each buff
        matrix[i][6] = random.randrange(int(screen_width*0.6),int(screen_width*0.8)) # postion_x of each buff
        matrix[i][5] = random.randrange(int(screen_width*0.83),int(screen_width*0.9)) # postion_x of each buff
        matrix[i][12] = int(screen_height*(1/16+i/5.2))   # postion_y of each buff
        matrix[i][11] = int(screen_height*(1/8+i/5.2)) # postion_y of each buff
        matrix[i][10] = int(screen_height*(1/16+i/5.2)) # postion_y of each buff
        matrix[i][9] = int(screen_height*(1/8+i/5.2)) # postion_y of each buff
    for i in range(0,5):                                                    #Random speed for Racer
        speed[i] = random.randrange(screen_width//300,screen_width//200)
    #The race loop
    while not pause:
        count = 0       #count the number of racer who has finished the race
        end = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    pause = True
                    paused()
        screen.blit(Map,(0,0))
#        CURVE_X = [350,710,1020]
#curve_index = [0]*5
#i_speedY = [[1,-1,1],
#            [1,-1,1],
#            [1,-1,1],
#            [1,-1,1],
#            [1,-1,1]]
#rotate_index = []*5
#i_rotate = [[1,-1,-1,1,1,-1],
#            [1,-1,-1,1,1,-1],
#            [1,-1,-1,1,1,-1],
#            [1,-1,-1,1,1,-1],
#            [1,-1,-1,1,1,-1]]
#start_curve = [0]*5
#step = [0]*5
        for i in range(0,5):
            if die[i] == 1:
                end+=1
                animation_racer(die_img[i],COUNT_DIE[i],posX[i],posY[i],object_width,int(screen_height/13))
                if COUNT_DIE[i] < maxCountDie[i] - 1:
                    COUNT_DIE[i]+=1
            else:
                if curve_index[i] < 3 and posX[i]>=CURVE_X[curve_index[i]]:
                    if(start_curve[i] == 0):
                        rotate_index[i] +=1
                        for k in range(FRAMES_COUNT[i]):
                            copy[i][k] = pygame.transform.rotate(copy[i][k],90*i_rotate[i][rotate_index[i]])
                        start_curve[i] = 1
                    if step[i] <= 28:
                        posY[i]+=(screen_height//300)*i_speedY[i][curve_index[i]]
                        animation_racer(copy[i],COUNT[i],posX[i],posY[i],object_width,int(screen_height/13))
                        step[i] += 1
                    else:
                        step[i] = 0
                        rotate_index[i] +=1
                        start_curve[i] = 0
                        for k in range(FRAMES_COUNT[i]):
                            copy[i][k] = pygame.transform.rotate(copy[i][k],90*i_rotate[i][rotate_index[i]])
                        curve_index[i]+=1
                    magic(Images,matrix[i][matrix[i][0]],finish,speed[i],posX[i],matrix[i][matrix[i][0]+4],matrix[i][matrix[i][0]+8])
                else:
                    if posX[i] >= finish:
                        if winner == -1:
                            cup_posY =posY[i]
                            pygame.mixer.music.load("win.mp3")
                            pygame.mixer.music.play(0)
                        winner = i + 1          # save the first Racer has finished the race
                        speed[i] = 0
                        racer(stand_img[i],finish,posY[i],object_width,int(screen_height/13))
                        count += 1                      
                    else:
                        animation_racer(copy[i],COUNT[i],posX[i],posY[i],object_width,int(screen_height/13))
                        posX[i]+=speed[i]
                        if posX[i]>= finish:
                            if winner == -1:
                                cup_posY = posY[i]
                                pygame.mixer.music.load("win.mp3")
                                pygame.mixer.music.play(0)
                                winner = i + 1          # save the first Racer has finished the race
                #To show buff to screen and return speed, position of racer
                        if matrix[i][0] != 0:
                            if posX[i] < matrix[i][matrix[i][0]+4]:      #if position's racer < position's buff (x coordinate), show the buff images
                                magic(Images,matrix[i][matrix[i][0]],finish,speed[i],posX[i],matrix[i][matrix[i][0]+4],matrix[i][matrix[i][0]+8])
                            else:                                       #else return speed, position of racer which buff gave
                                speed[i],posX[i] = magic(Images,matrix[i][matrix[i][0]],finish,speed[i],posX[i],matrix[i][matrix[i][0]+4],matrix[i][matrix[i][0]+8])
                                matrix[i][0] -= 1
                COUNT[i]+=1
                if COUNT[i] > (FRAMES_COUNT[i] - 1):
                    COUNT[i] = 0
            for k in range(0,1):
                racer(kunai,kunai_pos[k][0],kunai_pos[k][1],screen_width//50,int(screen_height/10))
                if posX[i] - screen_width//50 <= kunai_pos[k][0] <= posX[i]+object_width and posY[i] - screen_height//10 <= kunai_pos[k][1] <= posY[i]+screen_height//13:
                    die[i] = 1
                kunai_pos[k][1]+=kunai_pos[k][2]
                if kunai_pos[k][1]>screen_height:
                    kunai_pos[k][0] = random.randrange(0,9*screen_height//10)
                    kunai_pos[k][2] = random.randrange(screen_height//200,screen_height//100)
                    kunai_pos[k][1] = -1600
        if cup_posY != 0:
            screen.blit(cup,(finish-screen_width/20,cup_posY))
        if start == 0: 
            start +=1
            time.sleep(1)
        # if 5 Racer all completed the race, consider who won the game after the race
        if count == 5-end:
            i=0
            while i < numplayer:
                if infoPlayer[i][2] == winner:
                    infoPlayer[i][1] += price[winner-1]
                else:
                    infoPlayer[i][1] -= price[infoPlayer[i][2]-1]
                    if infoPlayer[i][1] < 0:
                        infoPlayer[i][1] = 0
                i+=1
            time.sleep(1)
            # call list_player function when the race ended
            list_player()
            break
        pygame.display.flip()
        clock.tick(30)
    #while True:
    #    screen.blit(Map,(0,0))
    #    screen.blit(char[count],(screen_width/2,screen_height/2))
    #    count +=1
    #    if count > FRAMES_COUNT - 1:
    #        count = 0
    #    pygame.display.flip()
    #    clock.tick(60)
'''
def input_and_map():
    global numplayer,infoPlayer,inputNumplayer, hell_map, desert_map, galaxy_map, snow_map, garden_map, ocean_map, inputBG, racerImg1, racerImg2, racerImg3, racerImg4
    # Load Map background's images, scale them and get their position
    hell_map_pos = pygame.Rect(19*screen_width/30,screen_height/20,screen_width//3,screen_height//4)
    snow_map_pos = pygame.Rect(screen_width/30,7*screen_height/20,screen_width//3,screen_height//4)
    desert_map_pos = pygame.Rect(screen_width/30,screen_height/20,screen_width//3,screen_height//4)
    galaxy_map_pos = pygame.Rect(19*screen_width/30,7*screen_height/20,screen_width//3,screen_height//4)
    #garden_map_pos = pygame.Rect(screen_width/10,3.2*screen_height/5,screen_width//3,screen_height//4)
    #ocean_map_pos =  pygame.Rect(17*screen_width/30,3.2*screen_height/5,screen_width//3,screen_height//4)
    # Load Map background's images, scale them and get their position
    screen.blit(inputBG,(0,0))
    # Show the price of racers
    # input the number of player
    input_numplayer()
    # input players's name
    for i in range(0,numplayer):
        if inputName[i]:
            input_name(i)
    # choose the racer
    if not inputName[numplayer-1]:
        for i in range(0,numplayer):
            if infoPlayer[i][3]:
                    choose_racer(i)
    # choose map for the race
    if not infoPlayer[numplayer-1][3]:
        while True:
            button(" BACK",20,720,160,65,bright_blue,blue,start_menu)         #function to back to start_menu function
            screen.blit(desert_map_icon,(screen_width/30,screen_height/20))
            screen.blit(hell_map_icon,(19*screen_width/30,screen_height/20))
            screen.blit(snow_map_icon,(screen_width/30,7*screen_height/20))
            screen.blit(galaxy_map_icon,(19*screen_width/30,7*screen_height/20))
            #screen.blit(garden_map,(screen_width/10,3.2*screen_height/5))
            #screen.blit(ocean_map,(17*screen_width/30,3.2*screen_height/5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if hell_map_pos.collidepoint(mouse_pos):
                        game_loop(hell_map,racerImg1,int(screen_height/8.9),int(screen_height/10.8),int(screen_height/12.3))
                    elif snow_map_pos.collidepoint(mouse_pos):
                        game_loop(snow_map,racerImg2,int(screen_height/8.9),int(screen_height/10.8),int(screen_height/12.3))
                    elif desert_map_pos.collidepoint(mouse_pos):
                        game_loop(desert_map,racerImg3,int(screen_height/8.9),int(screen_height/10.8),int(screen_height/12.3))
                    elif galaxy_map_pos.collidepoint(mouse_pos):
                        game_loop(galaxy_map,racerImg4,int(screen_height/8.9),int(screen_height/10.8),int(screen_height/12.3))
                    #elif garden_map_pos.collidepoint(mouse_pos):
                        #game_loop_curve(garden_map,listAni1,maxCount1,die_img1,stand_img1,kunai,maxCountDie1)
                    #elif ocean_map_pos.collidepoint(mouse_pos):
                        #game_loop_curve(ocean_map,listAni2,maxCount2,die_img2,stand_img2,fire,maxCountDie2)
            pygame.display.flip()
            clock.tick(15)

# function for the start game interface
def start_menu():
    global menu
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1)
    background_x = 0
    background_y = 0
    velocity = 5
    while True:
        pygame.display.set_mode((1300, 800))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(menu, (background_x, background_y))
        screen.blit(start_menu_reverse, (background_x + 1300, background_y - 75))
        screen.blit(menu, (background_x + 2600, background_y))
        if background_x + 2600 <= 0:
            background_x = 0
        background_x -= velocity
        screen.blit(game_title,(screen_width/60,screen_height/10))
        button("PLAY", 560, 350,screen_width/8,screen_height/12,bright_green,(16, 171, 38),input_and_map)
        button("RANK",560, 510,screen_width/8,screen_height/12,bright_green,(16, 171, 38),leader_board)
        button("QUIT",560, 670,screen_width/8,screen_height/12,bright_green,(16, 171, 38),quit)
        #button("SCREENSETTING",screen_width/5,3.5*screen_height/4,screen_width/4,screen_height/12,yellow,bright_yellow,screen_setting)
        button("GUIDE", 560, 590,screen_width/8,screen_height/12,(255, 115, 30),(249, 181, 19),guide)
        button("MINIGAME", 560, 430,165,screen_height/12,(255, 115, 30),(249, 181, 19),minigame)
        display_text("Version 1.0", "freesansbold.ttf", 30, white, 85, 780)
        pygame.display.update()
        clock.tick(60)
#curveMap_1 = pygame.transform.scale(curveMap_1,(screen_width,screen_height))
#screen.blit(curveMap_1,(0,0))

#while True:
#    for event in pygame.event.get():
#        print(event)
#    pygame.display.flip()
start_menu()
# file_rank_read.close()
# pygame.quit()
# quit()

