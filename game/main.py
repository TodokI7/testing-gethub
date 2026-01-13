import pygame

version = 'Alpha-0.0'
print("-----------------------------------------------")
print("Запуск")
print(version)

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Oink")
screen = pygame.display.set_mode((1920, 1080))

big_label = pygame.font.Font('fonts/floyd.TTF', 200)
label = pygame.font.Font('fonts/floyd.TTF', 100)
mini_label = pygame.font.Font('fonts/floyd.TTF', 50)

cursor = pygame.image.load("images/cursor.png").convert_alpha()
level_1_bg = pygame.image.load("images/cursor.png").convert_alpha()
level_2_bg = pygame.image.load("images/cursor.png").convert_alpha()
level_3_bg = pygame.image.load("images/cursor.png").convert_alpha()
level_4_bg = pygame.image.load("images/cursor.png").convert_alpha()
level_5_bg = pygame.image.load("images/cursor.png").convert_alpha()
n_0 = pygame.image.load("images/n0.png").convert_alpha()
n_1 = pygame.image.load("images/n1.png").convert_alpha()
n_2 = pygame.image.load("images/n2.png").convert_alpha()
n_l = pygame.image.load("images/nl.png").convert_alpha()
k_0 = pygame.image.load("images/k0.png").convert_alpha()
k_1 = pygame.image.load("images/k1.png").convert_alpha()
hit0 = pygame.image.load("images/mania-hit0.png").convert_alpha()
hit50 = pygame.image.load("images/mania-hit50.png").convert_alpha()
hit100 = pygame.image.load("images/mania-hit100.png").convert_alpha()
hit200 = pygame.image.load("images/mania-hit200.png").convert_alpha()
hit300 = pygame.image.load("images/mania-hit300.png").convert_alpha()
o = pygame.image.load("images/0.png").convert_alpha()
win = pygame.image.load("images/win.jpg").convert()

menu_sound = pygame.mixer.Sound("sounds/menu.mp3")
start_sound = pygame.mixer.Sound("sounds/start.mp3")
back_sound = pygame.mixer.Sound("sounds/back.mp3")
click_sound = pygame.mixer.Sound("sounds/click.mp3")
level_1_sound = pygame.mixer.Sound("sounds/menu.mp3")
level_2_sound = pygame.mixer.Sound("sounds/menu.mp3")
level_3_sound = pygame.mixer.Sound("sounds/menu.mp3")
level_4_sound = pygame.mixer.Sound("sounds/menu.mp3")
level_5_sound = pygame.mixer.Sound("sounds/menu.mp3")
win_sound = pygame.mixer.Sound("sounds/win.mp3")

pygame.display.set_icon(cursor)

level_1_rect = level_1_bg.get_rect()
level_2_rect = level_1_bg.get_rect()
level_3_rect = level_1_bg.get_rect()
level_4_rect = level_1_bg.get_rect()
level_5_rect = level_1_bg.get_rect()

isRun = True
isMenu = False
isAnimation = True
isAnimationToMapset1 = False
isAnimationToMapset2 = False
isAnimationToMapsFromMenu = False
isAnimationToMapsFromMapset = False
isAnimationToMenu = False
isA2 = False
isReverse = False
isMaps = False
isDownload = False
isForGame = False
islevel_1 = False
islevel_2 = False
islevel_3 = False
islevel_4 = False
islevel_5 = False
click = False
click_back = False
click_list1 = False
click_list2 = False
click_list3 = False
click_level1 = False
click_level2 = False
click_level3 = False
click_level4 = False
click_level5 = False
islist_1 = False
islist_2 = False
islist_3 = False
escape = False
back_clicked = False
level1_clicked = False
level2_clicked = False
level3_clicked = False
level4_clicked = False
level5_clicked = False
isMapset = False
admin = False
level_1_exist = False
level_2_exist = False
level_3_exist = False
level_4_exist = False
level_5_exist = False
isGame = False
n1clicked = False
n2clicked = False
n3clicked = False
n4clicked = False
n1clickedd = False
n2clickedd = False
n3clickedd = False
n4clickedd = False
n1clicking = False
n2clicking = False
n3clicking = False
n4clicking = False
isDefault = False
isWin = False

f = open("data.txt", "r")
q = f.readlines()
pas = q[0]
pas = pas[16:20]
if pas == "1258":
    print("Привет, Админ >_<")
    admin = True
f.close()

main_color = 0
a1 = 2
a2 = 5
a3 = 2
a4 = 3
fps = 120
la = 0
y = [1, 2, 3]
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data = []
w_i = []
w_c = []
w_default = []
w = 0
count = 0
im = o

combo = 0
count300 = 0
count200 = 0
count100 = 0
count50 = 0
countmisses = 0
highest = 0
score = 0
acc = 0
level = 0

x_start = 800
y_start = 800
x_back = 20
y_back = 900
x_oink = 750
y_oink = 100
x_version = 0
y_version = 0
x_list1 = 750
y_list1 = 200
x_list2 = 750
y_list2 = 400
x_list3 = 750
y_list3 = 600

x_level1 = 50
y_level1 = 0
x_level2 = 50
y_level2 = 150
x_level3 = 50
y_level3 = 300
x_level4 = 50
y_level4 = 450
x_level5 = 50
y_level5 = 600

x1 = 560
x2 = 760
x3 = 960
x4 = 1160
y1 = 800
y2 = 600
y3 = 400
y4 = 200
y5 = 0
y6 = -200
a = 0

size_start = 100
size_back = 100
size_list1 = 100
size_list2 = 100
size_list3 = 100
size_level1 = 100
size_level2 = 100
size_level3 = 100
size_level4 = 100
size_level5 = 100

level_1 = 0
level_2 = 0
level_3 = 0
level_4 = 0
level_5 = 0

while isRun:
    mouse = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    mouse_cords = (mouse[0] - 120, mouse[1] - 120)
    keys = pygame.key.get_pressed()
    clock.tick(fps)
    label_start = pygame.font.Font('fonts/floyd.TTF', size_start)
    label_back = pygame.font.Font('fonts/floyd.TTF', size_back)
    label_list1 = pygame.font.Font('fonts/floyd.TTF', size_list1)
    label_list2 = pygame.font.Font('fonts/floyd.TTF', size_list2)
    label_list3 = pygame.font.Font('fonts/floyd.TTF', size_list3)
    label_level1 = pygame.font.Font('fonts/floyd.TTF', size_level1)
    label_level2 = pygame.font.Font('fonts/floyd.TTF', size_level2)
    label_level3 = pygame.font.Font('fonts/floyd.TTF', size_level3)
    label_level4 = pygame.font.Font('fonts/floyd.TTF', size_level4)
    label_level5 = pygame.font.Font('fonts/floyd.TTF', size_level5)

    Om = big_label.render('Oink', False, (0, 0, 0))
    welcome_label = big_label.render('Welcome to...', False, (0, 0, 0))
    back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
    start_label = label_start.render('Start', False, (0, 0, 0))
    version_label = mini_label.render(version, False, (0, 0, 0))
    list_1 = label_list1.render('1mapset', False, (0, 0, 0))
    list_2 = label_list2.render('2mapset', False, (0, 0, 0))
    list_3 = label_list3.render('3mapset', False, (0, 0, 0))
    combo_label = label_start.render(str(combo), False, (255, 255, 255))
    highest_label = label_start.render(str(highest), False, (255, 255, 255))
    score_label = label_start.render(str(score), False, (255, 255, 255))
    acc_label = label_start.render(str(acc * 100) + "%", False, (255, 255, 255))

    if isAnimation:
        screen.fill((main_color, main_color, main_color))
        if not isA2:
            if main_color == 0 and isReverse:
                isA2 = True
            if main_color == 100:
                isReverse = True
            if isReverse:
                main_color = main_color - a3
            else:
                main_color = main_color + a1
            if main_color == 0 and isReverse:
                isA2 = True
        else:
            main_color = main_color + a2
            if main_color == 255:
                isReverse = False
                isAnimation = False
                isMenu = True
                menu_sound.play()
            screen.blit(Om, (x_oink, y_oink))
            screen.blit(start_label, (x_start, y_start))
            screen.blit(version_label, (x_version, y_version))
        if keys[pygame.K_SPACE]:
            isReverse = False
            isAnimation = False
            isMenu = True
            menu_sound.play()
            main_color = 255

    if isAnimationToMapsFromMenu:
        screen.fill((main_color, main_color, main_color))
        if not isReverse:
            if main_color != 0:
                main_color = main_color - a2
            if main_color == 0:
                isReverse = True
            screen.blit(start_label, (x_start, y_start))
            screen.blit(version_label, (x_version, y_version))
            screen.blit(Om, (x_oink, y_oink))
        if isReverse:
            if main_color != 255:
                main_color = main_color + a2
            if main_color == 255:
                isAnimationToMapsFromMenu = False
                isReverse = False
                isMenu = False
                isMaps = True
            screen.blit(back_to_menu_label, (x_back, y_back))
            screen.blit(list_1, (x_list1, y_list1))
            screen.blit(list_2, (x_list2, y_list2))
            screen.blit(list_3, (x_list3, y_list3))

    if isAnimationToMenu:
        screen.fill((main_color, main_color, main_color))
        if not isReverse:
            if main_color != 0:
                main_color = main_color - a2
            if main_color == 0:
                isReverse = True
            screen.blit(back_to_menu_label, (x_back, y_back))
            screen.blit(list_1, (x_list1, y_list1))
            screen.blit(list_2, (x_list2, y_list2))
            screen.blit(list_3, (x_list3, y_list3))
        if isReverse:
            x_back = 20
            y_back = 900
            size_back = 100
            if main_color != 255:
                main_color = main_color + a2
            if main_color == 255:
                isAnimationToMenu = False
                isReverse = False
                isMenu = True
                isMaps = False
            screen.blit(start_label, (x_start, y_start))
            screen.blit(version_label, (x_version, y_version))
            screen.blit(Om, (x_oink, y_oink))

    if isMenu:
        screen.fill((255, 255, 255))
        screen.blit(start_label, (x_start, y_start))
        screen.blit(version_label, (x_version, y_version))
        start_label_rect = start_label.get_rect(topleft=(x_start, y_start))
        if start_label_rect.collidepoint(mouse):
            if not click:
                click_sound.play()
                click = True
            if size_start != 120:
                size_start = size_start + a1
                x_start = x_start - a1
                y_start = y_start - a1
            start_label = label_start.render('Start', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                isMenu = False
                isAnimationToMapsFromMenu = True
                x_start = 800
                y_start = 800
                size_start = 100
                start_sound.play()
        if not start_label_rect.collidepoint(mouse):
            click = False
        if size_start != 100 and not start_label_rect.collidepoint(mouse):
            size_start = size_start - a1
            x_start = x_start + a1
            y_start = y_start + a1
            start_label = label_start.render('Start', False, (0, 0, 0))
        screen.blit(Om, (x_oink, y_oink))
        if keys[pygame.K_ESCAPE] and not escape:
            print("-----------------------------------------------")
            pygame.quit()
        if not keys[pygame.K_ESCAPE]:
            escape = False

    if isMaps:
        screen.fill((255, 255, 255))
        screen.blit(back_to_menu_label, (x_back, y_back))
        back_to_menu_label_rect = back_to_menu_label.get_rect(topleft=(x_back, y_back))
        if back_to_menu_label_rect.collidepoint(mouse):
            if not click_back:
                click_sound.play()
                click_back = True
            if size_back != 120:
                size_back = size_back + a1
                x_back = x_back - a1
                y_back = y_back - a1
            back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0] and not back_clicked:
                isMaps = False
                isAnimationToMenu = True
                back_sound.play()
                start_sound.stop()
        if not back_to_menu_label_rect.collidepoint(mouse):
            click_back = False
        if size_back != 100 and not back_to_menu_label_rect.collidepoint(mouse):
            size_back = size_back - a1
            x_back = x_back + a1
            y_back = y_back + a1
            back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
        if keys[pygame.K_ESCAPE] and not escape and not back_clicked:
            isMaps = False
            isAnimationToMenu = True
            x_back = 20
            y_back = 900
            size_back = 100
            start_sound.stop()
            back_sound.play()
            escape = True
        if not keys[pygame.K_ESCAPE]:
            escape = False
        if not pygame.mouse.get_pressed()[0]:
            back_clicked = False
        screen.blit(list_1, (x_list1, y_list1))
        screen.blit(list_2, (x_list2, y_list2))
        screen.blit(list_3, (x_list3, y_list3))
        list_1_rect = list_1.get_rect(topleft=(x_list1, y_list1))
        list_2_rect = list_2.get_rect(topleft=(x_list2, y_list2))
        list_3_rect = list_3.get_rect(topleft=(x_list3, y_list3))
        if list_1_rect.collidepoint(mouse):
            if not click_list1:
                click_sound.play()
                click_list1 = True
            if size_list1 != 120:
                size_list1 = size_list1 + a1
                x_list1 = x_list1 - a4
                y_list1 = y_list1 - a1
            list_1 = label_list1.render('1mapset', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                la = 1
                isAnimationToMapset1 = True
                isMaps = False
                start_sound.play()
        if not list_1_rect.collidepoint(mouse):
            click_list1 = False
        if size_list1 != 100 and not list_1_rect.collidepoint(mouse):
            size_list1 = size_list1 - a1
            x_list1 = x_list1 + a4
            y_list1 = y_list1 + a1
            list_1 = label_list1.render('1mapset', False, (0, 0, 0))
        if list_2_rect.collidepoint(mouse):
            if not click_list2:
                click_sound.play()
                click_list2 = True
            if size_list2 != 120:
                size_list2 = size_list2 + a1
                x_list2 = x_list2 - a4
                y_list2 = y_list2 - a1
            list_2 = label_list2.render('2mapset', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                la = 2
                isAnimationToMapset1 = True
                isMaps = False
                start_sound.play()
        if not list_2_rect.collidepoint(mouse):
            click_list2 = False
        if size_list2 != 100 and not list_2_rect.collidepoint(mouse):
            size_list2 = size_list2 - a1
            x_list2 = x_list2 + a4
            y_list2 = y_list2 + a1
            list_2 = label_list2.render('2mapset', False, (0, 0, 0))
        if list_3_rect.collidepoint(mouse):
            if not click_list3:
                click_sound.play()
                click_list3 = True
            if size_list3 != 120:
                size_list3 = size_list3 + a1
                x_list3 = x_list3 - a4
                y_list3 = y_list3 - a1
            list_3 = label_list3.render('3mapset', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                la = 3
                isAnimationToMapset1 = True
                isMaps = False
                start_sound.play()
        if not list_3_rect.collidepoint(mouse):
            click_list3 = False
        if size_list3 != 100 and not list_3_rect.collidepoint(mouse):
            size_list3 = size_list3 - a1
            x_list3 = x_list3 + a4
            y_list3 = y_list3 + a1
            list_3 = label_list3.render('3mapset', False, (0, 0, 0))

    if islist_1:
        menu_sound.stop()
        start_sound.stop()
        click_sound.stop()
        back_sound.stop()
        level_1_exist = False
        level_2_exist = False
        level_3_exist = False
        level_4_exist = False
        level_5_exist = False
        if q[2] != "-\n":
            data1 = q[3]
            level_1 = label_level1.render(q[2][:-1], False, (0, 0, 0))
            level_1_bg = pygame.image.load(q[4][:-1]).convert()
            level_1_sound = pygame.mixer.Sound(q[5][:-1])
            level_1_exist = True
        if q[6] != "-\n":
            data2 = q[7]
            level_2 = label_level2.render(q[6][:-1], False, (0, 0, 0))
            level_2_bg = pygame.image.load(q[8][:-1]).convert()
            level_2_sound = pygame.mixer.Sound(q[9][:-1])
            level_2_exist = True
        if q[10] != "-\n":
            data3 = q[11]
            level_3 = label_level3.render(q[10][:-1], False, (0, 0, 0))
            level_3_bg = pygame.image.load(q[12][:-1]).convert()
            level_3_sound = pygame.mixer.Sound(q[13][:-1])
            level_3_exist = True
        if q[14] != "-\n":
            data4 = q[15]
            level_4 = label_level4.render(q[14][:-1], False, (0, 0, 0))
            level_4_bg = pygame.image.load(q[16][:-1]).convert()
            level_4_sound = pygame.mixer.Sound(q[17][:-1])
            level_4_exist = True
        if q[18] != "-\n":
            data5 = q[19]
            level_5 = label_level5.render(q[18][:-1], False, (0, 0, 0))
            level_5_bg = pygame.image.load(q[20][:-1]).convert()
            level_5_sound = pygame.mixer.Sound(q[21][:-1])
            level_5_exist = True
        isAnimationToMapset2 = True
        islist_1 = False

    if islist_2:
        menu_sound.stop()
        start_sound.stop()
        click_sound.stop()
        back_sound.stop()
        level_1_exist = False
        level_2_exist = False
        level_3_exist = False
        level_4_exist = False
        level_5_exist = False
        if q[22] != "-\n":
            data1 = q[23]
            level_1 = label.render(q[22][:-1], False, (0, 0, 0))
            level_1_bg = pygame.image.load(q[24][:-1]).convert
            level_1_sound = pygame.mixer.Sound(q[25][:-1])
            level_1_exist = True
        if q[26] != "-\n":
            data2 = q[27]
            level_2 = label.render(q[26][:-1], False, (0, 0, 0))
            level_2_bg = pygame.image.load(q[28][:-1]).convert
            level_2_sound = pygame.mixer.Sound(q[29][:-1])
            level_2_exist = True
        if q[30] != "-\n":
            data3 = q[31]
            level_3 = label.render(q[30][:-1], False, (0, 0, 0))
            level_3_bg = pygame.image.load(q[32][:-1]).convert
            level_3_sound = pygame.mixer.Sound(q[33][:-1])
            level_3_exist = True
        if q[34] != "-\n":
            data4 = q[35]
            level_4 = label.render(q[34][:-1], False, (0, 0, 0))
            level_4_bg = pygame.image.load(q[36][:-1]).convert
            level_4_sound = pygame.mixer.Sound(q[37][:-1])
            level_4_exist = True
        if q[38] != "-\n":
            data5 = q[39]
            level_5 = label.render(q[38][:-1], False, (0, 0, 0))
            level_5_bg = pygame.image.load(q[40][:-1]).convert
            level_5_sound = pygame.mixer.Sound(q[41][:-1])
            level_5_exist = True
        islist_2 = False
        isAnimationToMapset2 = True

    if islist_3:
        menu_sound.stop()
        start_sound.stop()
        click_sound.stop()
        back_sound.stop()
        level_1_exist = False
        level_2_exist = False
        level_3_exist = False
        level_4_exist = False
        level_5_exist = False
        if q[42] != "-\n":
            data1 = q[43]
            level_1 = label.render(q[42][:-1], False, (0, 0, 0))
            level_1_bg = pygame.image.load(q[44][:-1]).convert
            level_1_sound = pygame.mixer.Sound(q[45][:-1])
            level_1_exist = True
        if q[46] != "-\n":
            data2 = q[47]
            level_2 = label.render(q[46][:-1], False, (0, 0, 0))
            level_2_bg = pygame.image.load(q[48][:-1]).convert
            level_2_sound = pygame.mixer.Sound(q[49][:-1])
            level_2_exist = True
        if q[50] != "-\n":
            data3 = q[51]
            level_3 = label.render(q[50][:-1], False, (0, 0, 0))
            level_3_bg = pygame.image.load(q[52][:-1]).convert
            level_3_sound = pygame.mixer.Sound(q[53][:-1])
            level_3_exist = True
        if q[54] != "-\n":
            data4 = q[55]
            level_4 = label.render(q[54][:-1], False, (0, 0, 0))
            level_4_bg = pygame.image.load(q[56][:-1]).convert
            level_4_sound = pygame.mixer.Sound(q[57][:-1])
            level_4_exist = True
        if q[58] != "-\n":
            data5 = q[59]
            level_5 = label.render(q[58][:-1], False, (0, 0, 0))
            level_5_bg = pygame.image.load(q[60][:-1]).convert
            level_5_sound = pygame.mixer.Sound(q[61][:-1])
            level_5_exist = True
        islist_3 = False
        isAnimationToMapset2 = True

    if isMapset:
        screen.fill((255, 255, 255))
        if level1_clicked:
            screen.fill((255, 255, 255))
            screen.blit(level_1_bg, (0, 0))
        if islevel_1:
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            level_1_sound.play()
            level2_clicked = False
            level3_clicked = False
            level4_clicked = False
            level5_clicked = False
            islevel_1 = False
        if level2_clicked:
            screen.fill((255, 255, 255))
            screen.blit(level_2_bg, (0, 0))
        if islevel_2:
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            level_2_sound.play()
            level1_clicked = False
            level3_clicked = False
            level4_clicked = False
            level5_clicked = False
            islevel_2 = False
        if level3_clicked:
            screen.fill((255, 255, 255))
            screen.blit(level_3_bg, (0, 0))
        if islevel_3:
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            level_3_sound.play()
            level1_clicked = False
            level2_clicked = False
            level4_clicked = False
            level5_clicked = False
            islevel_3 = False
        if level4_clicked:
            screen.fill((255, 255, 255))
            screen.blit(level_4_bg, (0, 0))
        if islevel_4:
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            level_4_sound.play()
            level1_clicked = False
            level2_clicked = False
            level3_clicked = False
            level5_clicked = False
            islevel_4 = False
        if level5_clicked:
            screen.fill((255, 255, 255))
            screen.blit(level_5_bg, (0, 0))
        if islevel_5:
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            level_5_sound.play()
            level1_clicked = False
            level2_clicked = False
            level3_clicked = False
            level4_clicked = False
            islevel_5 = False
        if level_1_exist:
            level_1_rect = level_1.get_rect(topleft=(x_level1, y_level1))
            if la == 1:
                level_1 = label_level1.render(q[2][:-1], False, (0, 0, 0))
            elif la == 2:
                level_1 = label_level1.render(q[22][:-1], False, (0, 0, 0))
            elif la == 3:
                level_1 = label_level1.render(q[42][:-1], False, (0, 0, 0))
            screen.blit(level_1, (x_level1, y_level1))
            if level_1_rect.collidepoint(mouse):
                if not click_level1 and not level1_clicked:
                    click_sound.play()
                    click_level1 = True
                if size_level1 != 120:
                    size_level1 = size_level1 + a1
                    x_level1 = x_level1 - a1
                    y_level1 = y_level1 - a1
                if pygame.mouse.get_pressed()[0]:
                    if not level1_clicked:
                        level1_clicked = True
                        click_level1 = True
                        islevel_1 = True
                    if level1_clicked and not click_level1:
                        level = 1
                        print("Игра началась)")
                        with open(data1[:-1] + "/info.txt", "r") as f:
                            y = f.readlines()
                        isForGame = True
                        level_1_sound.stop()
                        level_2_sound.stop()
                        level_3_sound.stop()
                        level_4_sound.stop()
                        level_5_sound.stop()
                        level_1_sound.play()
            if not level_1_rect.collidepoint(mouse):
                click_level1 = False
            if size_level1 != 100 and not level_1_rect.collidepoint(mouse) and not level1_clicked:
                size_level1 = size_level1 - a1
                x_level1 = x_level1 + a1
                y_level1 = y_level1 + a1
        if level_2_exist:
            level_2_rect = level_2.get_rect(topleft=(x_level2, y_level2))
            if la == 1:
                level_2 = label_level2.render(q[6][:-1], False, (0, 0, 0))
            elif la == 2:
                level_2 = label_level2.render(q[26][:-1], False, (0, 0, 0))
            elif la == 3:
                level_2 = label_level2.render(q[46][:-1], False, (0, 0, 0))
            screen.blit(level_2, (x_level2, y_level2))
            if level_2_rect.collidepoint(mouse):
                if not click_level2 and not level2_clicked:
                    click_sound.play()
                    click_level2 = True
                if size_level2 != 120:
                    size_level2 = size_level2 + a1
                    x_level2 = x_level2 - a1
                    y_level2 = y_level2 - a1
                if pygame.mouse.get_pressed()[0]:
                    if not level2_clicked:
                        level2_clicked = True
                        click_level2 = True
                        islevel_2 = True
                    if level2_clicked and not click_level2:
                        print("Игра началась)")
                        level = 2
                        with open(data2[:-1] + "/info.txt", "r") as f:
                            y = f.readlines()
                        isForGame = True
                        level_1_sound.stop()
                        level_2_sound.stop()
                        level_3_sound.stop()
                        level_4_sound.stop()
                        level_5_sound.stop()
                        level_2_sound.play()
            if not level_2_rect.collidepoint(mouse):
                click_level2 = False
            if size_level2 != 100 and not level_2_rect.collidepoint(mouse) and not level2_clicked:
                size_level2 = size_level2 - a1
                x_level2 = x_level2 + a1
                y_level2 = y_level2 + a1
        if level_3_exist:
            level_3_rect = level_3.get_rect(topleft=(x_level3, y_level3))
            if la == 1:
                level_3 = label_level3.render(q[10][:-1], False, (0, 0, 0))
            elif la == 2:
                level_3 = label_level3.render(q[30][:-1], False, (0, 0, 0))
            elif la == 3:
                level_3 = label_level3.render(q[50][:-1], False, (0, 0, 0))
            screen.blit(level_3, (x_level3, y_level3))
            if level_3_rect.collidepoint(mouse):
                if not click_level3 and not level3_clicked:
                    click_sound.play()
                    click_level3 = True
                if size_level3 != 120:
                    size_level3 = size_level3 + a1
                    x_level3 = x_level3 - a1
                    y_level3 = y_level3 - a1
                if pygame.mouse.get_pressed()[0]:
                    if not level3_clicked:
                        level3_clicked = True
                        click_level3 = True
                        islevel_3 = True
                    if level3_clicked and not click_level3:
                        print("Игра началась)")
                        level = 3
                        with open(data3[:-1] + "/info.txt", "r") as f:
                            y = f.readlines()
                        isForGame = True
                        level_1_sound.stop()
                        level_2_sound.stop()
                        level_3_sound.stop()
                        level_4_sound.stop()
                        level_5_sound.stop()
                        level_3_sound.play()
            if not level_3_rect.collidepoint(mouse):
                click_level3 = False
            if size_level3 != 100 and not level_3_rect.collidepoint(mouse) and not level3_clicked:
                size_level3 = size_level3 - a1
                x_level3 = x_level3 + a1
                y_level3 = y_level3 + a1
        if level_4_exist:
            level_4_rect = level_4.get_rect(topleft=(x_level4, y_level4))
            if la == 1:
                level_4 = label_level4.render(q[14][:-1], False, (0, 0, 0))
            elif la == 2:
                level_4 = label_level4.render(q[34][:-1], False, (0, 0, 0))
            elif la == 3:
                level_4 = label_level4.render(q[54][:-1], False, (0, 0, 0))
            screen.blit(level_4, (x_level4, y_level4))
            if level_4_rect.collidepoint(mouse):
                if not click_level4 and not level4_clicked:
                    click_sound.play()
                    click_level4 = True
                if size_level4 != 120:
                    size_level4 = size_level4 + a1
                    x_level4 = x_level4 - a1
                    y_level4 = y_level4 - a1
                if pygame.mouse.get_pressed()[0]:
                    if not level4_clicked:
                        level4_clicked = True
                        click_level4 = True
                        islevel_4 = True
                    if level4_clicked and not click_level4:
                        print("Игра началась)")
                        level = 4
                        with open(data4[:-1] + "/info.txt", "r") as f:
                            y = f.readlines()
                        isForGame = True
                        level_1_sound.stop()
                        level_2_sound.stop()
                        level_3_sound.stop()
                        level_4_sound.stop()
                        level_5_sound.stop()
                        level_4_sound.play()
            if not level_4_rect.collidepoint(mouse):
                click_level4 = False
            if size_level4 != 100 and not level_4_rect.collidepoint(mouse) and not level4_clicked:
                size_level4 = size_level4 - a1
                x_level4 = x_level4 + a1
                y_level4 = y_level4 + a1
        if level_5_exist:
            level_5_rect = level_5.get_rect(topleft=(x_level5, y_level5))
            if la == 1:
                level_5 = label_level5.render(q[18][:-1], False, (0, 0, 0))
            elif la == 2:
                level_5 = label_level5.render(q[38][:-1], False, (0, 0, 0))
            elif la == 3:
                level_5 = label_level5.render(q[58][:-1], False, (0, 0, 0))
            screen.blit(level_5, (x_level5, y_level5))
            if level_5_rect.collidepoint(mouse):
                if not click_level5 and not level5_clicked:
                    click_sound.play()
                    click_level5 = True
                if size_level5 != 120:
                    size_level5 = size_level5 + a1
                    x_level5 = x_level5 - a1
                    y_level5 = y_level5 - a1
                if pygame.mouse.get_pressed()[0]:
                    if not level5_clicked:
                        level5_clicked = True
                        click_level5 = True
                        islevel_5 = True
                    if level5_clicked and not click_level5:
                        print("Игра началась)")
                        level = 5
                        with open(data5[:-1] + "/info.txt", "r") as f:
                            y = f.readlines()
                        isForGame = True
                        level_1_sound.stop()
                        level_2_sound.stop()
                        level_3_sound.stop()
                        level_4_sound.stop()
                        level_5_sound.stop()
                        level_5_sound.play()
            if not level_5_rect.collidepoint(mouse):
                click_level5 = False
            if size_level5 != 100 and not level_5_rect.collidepoint(mouse) and not level5_clicked:
                size_level5 = size_level5 - a1
                x_level5 = x_level5 + a1
                y_level5 = y_level5 + a1

        back_to_menu_label_rect = back_to_menu_label.get_rect(topleft=(x_back, y_back))
        if back_to_menu_label_rect.collidepoint(mouse):
            if not click_back:
                click_sound.play()
                click_back = True
            if size_back != 120:
                size_back = size_back + a1
                x_back = x_back - a1
                y_back = y_back - a1
            back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0] and not back_clicked:
                isMapset = False
                start_sound.stop()
                level_1_sound.stop()
                level_2_sound.stop()
                level_3_sound.stop()
                level_4_sound.stop()
                level_5_sound.stop()
                level1_clicked = False
                level2_clicked = False
                level3_clicked = False
                level4_clicked = False
                level5_clicked = False
                back_sound.play()
                back_clicked = True
                isAnimationToMapsFromMapset = True
        if not back_to_menu_label_rect.collidepoint(mouse):
            click_back = False
        if not keys[pygame.K_ESCAPE]:
            escape = False
        if not pygame.mouse.get_pressed()[0]:
            back_clicked = False
        if size_back != 100 and not back_to_menu_label_rect.collidepoint(mouse):
            size_back = size_back - a1
            x_back = x_back + a1
            y_back = y_back + a1
            back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
        if keys[pygame.K_ESCAPE] and not escape and not back_clicked:
            isMapset = False
            start_sound.stop()
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            level1_clicked = False
            level2_clicked = False
            level3_clicked = False
            level4_clicked = False
            level5_clicked = False
            back_sound.play()
            escape = True
            isAnimationToMapsFromMapset = True
        screen.blit(back_to_menu_label, (x_back, y_back))

    if isAnimationToMapset1:
        isDownload = True
        menu_sound.stop()
        screen.fill((main_color, main_color, main_color))
        if main_color != 0:
            main_color = main_color - a2
        screen.fill((main_color, main_color, main_color))
        if main_color == 0:
            if la == 1:
                islist_1 = True
            elif la == 2:
                islist_2 = True
            elif la == 3:
                islist_3 = True
            else:
                print("ERROR")
                pygame.quit()
            isAnimationToMapset1 = False
        screen.blit(back_to_menu_label, (x_back, y_back))
        screen.blit(list_1, (x_list1, y_list1))
        screen.blit(list_2, (x_list2, y_list2))
        screen.blit(list_3, (x_list3, y_list3))

    if isAnimationToMapset2:
        isDownload = False
        x_list1 = 750
        y_list1 = 200
        x_list2 = 750
        y_list2 = 400
        x_list3 = 750
        y_list3 = 600
        size_list1 = 100
        size_list2 = 100
        size_list3 = 100
        screen.fill((main_color, main_color, main_color))
        if main_color != 255:
            main_color = main_color + a2
        if main_color == 255:
            isAnimationToMapset2 = False
            isReverse = False
            isMapset = True
            isMaps = False
        if level_1_exist:
            screen.blit(level_1, (x_level1, y_level1))
        if level_2_exist:
            screen.blit(level_2, (x_level2, y_level2))
        if level_3_exist:
            screen.blit(level_3, (x_level3, y_level3))
        if level_4_exist:
            screen.blit(level_4, (x_level4, y_level4))
        if level_5_exist:
            screen.blit(level_5, (x_level5, y_level5))
        screen.blit(back_to_menu_label, (x_back, y_back))

    if isAnimationToMapsFromMapset:
        screen.fill((main_color, main_color, main_color))
        if not isReverse:
            if main_color != 0:
                main_color = main_color - a2
            if main_color == 0:
                isReverse = True
            if level_1_exist:
                screen.blit(level_1, (x_level1, y_level1))
            if level_2_exist:
                screen.blit(level_2, (x_level2, y_level2))
            if level_3_exist:
                screen.blit(level_3, (x_level3, y_level3))
            if level_4_exist:
                screen.blit(level_4, (x_level4, y_level4))
            if level_5_exist:
                screen.blit(level_5, (x_level5, y_level5))
            screen.blit(back_to_menu_label, (x_back, y_back))
        if isReverse:
            x_back = 20
            y_back = 900
            size_back = 100
            if main_color != 255:
                main_color = main_color + a2
            if main_color == 255:
                isAnimationToMapsFromMapset = False
                isReverse = False
                isMaps = True
                isMapset = False
            screen.blit(back_to_menu_label, (x_back, y_back))
            screen.blit(list_1, (x_list1, y_list1))
            screen.blit(list_2, (x_list2, y_list2))
            screen.blit(list_3, (x_list3, y_list3))

    if isGame:
        screen.fill((0, 0, 0))
        screen.blit(k_0, (x1, 800))
        screen.blit(k_0, (x2, 800))
        screen.blit(k_0, (x3, 800))
        screen.blit(k_0, (x4, 800))
        screen.blit(combo_label, (1500, 800))
        screen.blit(score_label, (0, 0))
        if keys[pygame.K_d]:
            screen.blit(k_1, (560, 800))
            if w_i[count][0] == "1" and not n1clicked and not n1clicking:
                w_i[count][0] = "0"
                m = y1 - 800
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n1clicked = True
                combo = combo + 1
            elif w_i[count + 1][0] == "1" and not n1clickedd and not n1clicking:
                w_i[count + 1][0] = "0"
                m = 800 - y2
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n1clickedd = True
                combo = combo + 1
            elif w_i[count + 1][0] == "0" and not n1clicking:
                im = hit0
                countmisses = countmisses + 1
                if combo > highest:
                    highest = combo
                combo = 0
            n1clicking = True
        if not keys[pygame.K_d]:
            n1clicking = False
        if keys[pygame.K_f]:
            screen.blit(k_1, (760, 800))
            if w_i[count][1] == "1" and not n2clicked and not n2clicking:
                w_i[count][1] = "0"
                m = y1 - 800
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n2clicked = True
                combo = combo + 1
            elif w_i[count + 1][1] == "1" and not n2clickedd and not n2clicking:
                w_i[count + 1][1] = "0"
                m = 800 - y2
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n2clickedd = True
                combo = combo + 1
            elif w_i[count + 1][1] == "0" and not n2clicking:
                im = hit0
                countmisses = countmisses + 1
                if combo > highest:
                    highest = combo
                combo = 0
            n2clicking = True
        if not keys[pygame.K_f]:
            n2clicking = False
        if keys[pygame.K_k]:
            screen.blit(k_1, (960, 800))
            if w_i[count][2] == "1" and not n3clicked and not n3clicking:
                w_i[count][2] = "0"
                m = y1 - 800
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n3clicked = True
                combo = combo + 1
            elif w_i[count + 1][2] == "1" and not n3clickedd and not n3clicking:
                w_i[count + 1][2] = "0"
                m = 800 - y2
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n3clickedd = True
                combo = combo + 1
            elif w_i[count + 1][2] == "0" and not n3clicking:
                im = hit0
                countmisses = countmisses + 1
                if combo > highest:
                    highest = combo
                combo = 0
            n3clicking = True
        if not keys[pygame.K_k]:
            n3clicking = False
        if keys[pygame.K_l]:
            screen.blit(k_1, (1160, 800))
            if w_i[count][3] == "1" and not n4clicked and not n4clicking:
                w_i[count][3] = "0"
                m = y1 - 800
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n4clicked = True
                combo = combo + 1
            elif w_i[count + 1][3] == "1" and not n4clickedd and not n4clicking:
                w_i[count + 1][3] = "0"
                m = 800 - y2
                if m < 50:
                    im = hit300
                    count300 = count300 + 1
                    score = score + 300 * combo
                elif 50 <= m < 100:
                    im = hit200
                    count200 = count200 + 1
                    score = score + 200 * combo
                elif 100 <= m < 150:
                    im = hit100
                    count100 = count100 + 1
                    score = score + 100 * combo
                elif 150 <= m < 200:
                    im = hit50
                    count50 = count50 + 1
                    score = score + 50 * combo
                n4clickedd = True
                combo = combo + 1
            elif w_i[count + 1][3] == "0" and not n4clicking:
                im = hit0
                countmisses = countmisses + 1
                if combo > highest:
                    highest = combo
                combo = 0
            n4clicking = True
        if not keys[pygame.K_l]:
            n4clicking = False
        y1 = y1 + a
        y2 = y2 + a
        y3 = y3 + a
        y4 = y4 + a
        y5 = y5 + a
        y6 = y6 + a
        for i in range(count, count + 6):
            cords = w_c[i - count]
            for k in range(0, 4):
                if w_i[i][k] == '1':
                    if k == 0 or k == 3:
                        screen.blit(n_1, (cords[k][0], cords[k][1]))
                    else:
                        screen.blit(n_2, (cords[k][0], cords[k][1]))
        if w == 200:
            im = o
            w = 0
            if w_i[count] != ['0', '0', '0', '0']:
                im = hit0
                countmisses = countmisses + 1
                if combo > highest:
                    highest = combo
                combo = 0
            count = count + 1
            if count == len(w_i) - 6:
                isGame = False
                if combo > highest:
                    highest = combo
                isWin = True
                win_sound.play()
                level_1_sound.stop()
                level_2_sound.stop()
                level_3_sound.stop()
                level_4_sound.stop()
                level_5_sound.stop()
            x1 = 560
            x2 = 760
            x3 = 960
            x4 = 1160
            y1 = 800
            y2 = 600
            y3 = 400
            y4 = 200
            y5 = 0
            y6 = -200
            n1clicked = False
            n2clicked = False
            n3clicked = False
            n4clicked = False
            n1clickedd = False
            n2clickedd = False
            n3clickedd = False
            n4clickedd = False
        w_c = [[[x1, y1], [x2, y1], [x3, y1], [x4, y1]], [[x1, y2], [x2, y2], [x3, y2], [x4, y2]], [[x1, y3], [x2, y3],
                                                                                                    [x3, y3], [x4, y3]],
               [[x1, y4], [x2, y4], [x3, y4], [x4, y4]], [[x1, y5], [x2, y5], [x3, y5], [x4, y5]], [[x1, y6], [x2, y6],
                                                                                                    [x3, y6], [x4, y6]]]
        w = w + a
        screen.blit(im, (900, 1000))
        ac300 = count300 * 1
        ac200 = count200 * 0.75
        ac100 = count100 * 0.5
        ac50 = count50 * 0.25
        if (count300 + count200 + count100 + count50 + countmisses) != 0:
            acc = round((ac300 + ac200 + ac100 + ac50) / (count300 + count200 + count100 + count50 + countmisses), 4)
        screen.blit(acc_label, (1450, 0))

    if isForGame:
        isMapset = False
        t = []
        for i in y:
            t.append(i[:-1])
        y = t
        a = int(y[0])
        w = 0
        y.remove(y[0])
        w_default = [[x1, y1], [x2, y1], [x3, y1], [x4, y1]]
        w_c = [[[x1, y1], [x2, y1], [x3, y1], [x4, y1]], [[x1, y2], [x2, y2], [x3, y2], [x4, y2]], [[x1, y3], [x2, y3],
                                                                                                    [x3, y3], [x4, y3]],
               [[x1, y4], [x2, y4], [x3, y4], [x4, y4]], [[x1, y5], [x2, y5], [x3, y5], [x4, y5]], [[x1, y6], [x2, y6],
                                                                                                    [x3, y6], [x4, y6]]]
        w_i = []
        count = 0
        combo = 0
        count300 = 0
        count200 = 0
        count100 = 0
        count50 = 0
        countmisses = 0
        highest = 0
        acc = 0
        for i in y:
            w_i.append(list(i))
        isForGame = False
        isGame = True

    if isWin:
        count300_label = label_start.render(str(count300), False, (255, 255, 255))
        count200_label = label_start.render(str(count200), False, (255, 255, 255))
        count100_label = label_start.render(str(count100), False, (255, 255, 255))
        count50_label = label_start.render(str(count50), False, (255, 255, 255))
        countmisses_label = label_start.render(str(countmisses), False, (255, 255, 255))
        screen.blit(win, (0, 0))
        screen.blit(hit300, (200, 225))
        screen.blit(count300_label, (500, 175))
        screen.blit(hit200, (75, 380))
        screen.blit(count200_label, (250, 330))
        screen.blit(hit100, (500, 380))
        screen.blit(count100_label, (650, 330))
        screen.blit(hit50, (75, 535))
        screen.blit(count50_label, (200, 485))
        screen.blit(hit0, (500, 535))
        screen.blit(countmisses_label, (650, 485))
        screen.blit(highest_label, (50, 670))
        screen.blit(acc_label, (450, 670))
        screen.blit(score_label, (200, 10))
        screen.blit(back_to_menu_label, (x_back, y_back))
        back_to_menu_label_rect = back_to_menu_label.get_rect(topleft=(x_back, y_back))
        if back_to_menu_label_rect.collidepoint(mouse):
            if not click_back:
                click_sound.play()
                click_back = True
            if size_back != 120:
                size_back = size_back + a1
                x_back = x_back - a1
                y_back = y_back - a1
            back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
            if pygame.mouse.get_pressed()[0] and not back_clicked:
                isWin = False
                isMapset = True
                back_sound.play()
                start_sound.stop()
                back_clicked = True
                level_1_sound.stop()
                level_2_sound.stop()
                level_3_sound.stop()
                level_4_sound.stop()
                level_5_sound.stop()
                win_sound.stop()
                if level == 1:
                    level_1_sound.play()
                if level == 2:
                    level_2_sound.play()
                if level == 3:
                    level_3_sound.play()
                if level == 4:
                    level_4_sound.play()
                if level == 5:
                    level_5_sound.play()

        if not back_to_menu_label_rect.collidepoint(mouse):
            click_back = False
        if size_back != 100 and not back_to_menu_label_rect.collidepoint(mouse):
            size_back = size_back - a1
            x_back = x_back + a1
            y_back = y_back + a1
            back_to_menu_label = label_back.render('Back', False, (0, 0, 0))
        if keys[pygame.K_ESCAPE] and not escape and not back_clicked:
            isWin = False
            isMapset = True
            x_back = 20
            y_back = 900
            size_back = 100
            start_sound.stop()
            back_sound.play()
            escape = True
            level_1_sound.stop()
            level_2_sound.stop()
            level_3_sound.stop()
            level_4_sound.stop()
            level_5_sound.stop()
            win_sound.stop()
            if level == 1:
                level_1_sound.play()
            if level == 2:
                level_2_sound.play()
            if level == 3:
                level_3_sound.play()
            if level == 4:
                level_4_sound.play()
            if level == 5:
                level_5_sound.play()
        if not keys[pygame.K_ESCAPE]:
            escape = False
        if not pygame.mouse.get_pressed()[0]:
            back_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
            print("-----------------------------------------------")
            pygame.quit()

    if keys[pygame.K_w] and admin:
        print("Программа завершена по воли Админа")
        print("-----------------------------------------------")
        pygame.quit()

    if not isDownload:
        screen.blit(cursor, mouse_cords)

    pygame.display.update()
