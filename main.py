import sys, pygame
pygame.init()

size=width,height=1280,720
speed=[1,1]

skin=0
counter=100
scene=0

right=True
walking=False
jumping=False

inv=[0,0,0,0,0]

room_bg=90,90,90
sky_bg=0,255,255

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Breaking Bad Simulator")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("heisenberg_r.png").convert_alpha()
        self.rect = self.image.get_rect()

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("table.png").convert_alpha()
        self.rect = self.image.get_rect()

sprite_list = pygame.sprite.Group()
#warstwy wedlug kolejnosci zdefiniowania
floor=Object()
floor.image=pygame.image.load("floor.png").convert_alpha()
floor.rect.x=0
floor.rect.y=500
sprite_list.add(floor)

closet=Object()
closet.image=pygame.image.load("closet.png").convert_alpha()
closet.rect.x=800
closet.rect.y=100
sprite_list.add(closet)

cooker=Object()
cooker.image=pygame.image.load("cooker.png").convert_alpha()
cooker.rect.x=450
cooker.rect.y=125
sprite_list.add(cooker)

table=Object()
table.image=pygame.image.load("table.png").convert_alpha()
table.rect.x=400
table.rect.y=300
sprite_list.add(table)

inventory=Object()
inventory.image=pygame.image.load("inventory.png").convert_alpha()
inventory.rect.x=440
inventory.rect.y=640
sprite_list.add(inventory)

jesse=Object()
jesse.image=pygame.image.load("jesse.png").convert_alpha()
jesse.rect.x=1000
jesse.rect.y=101

meth=Object()
meth.image=pygame.image.load("meth.png").convert_alpha()
meth.rect.x=550
meth.rect.y=233

player=Player()
player.rect.x=100
player.rect.y=101
sprite_list.add(player)

pressed_keys = {"left": False, "right": False}

while True:

    walking = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed_keys["left"] = True
            if event.key == pygame.K_RIGHT:
                pressed_keys["right"] = True
            if event.key == pygame.K_UP:
                print("jump")
                #jump

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_keys["left"] = False
            if event.key == pygame.K_RIGHT:
                pressed_keys["right"] = False

        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if cooker.rect.collidepoint(pos):
                sprite_list.add(meth)
            if meth.rect.collidepoint(pos):
                meth.rect.x=445
                meth.rect.y=645
            if jesse.rect.collidepoint(pos):
                if meth.rect.x==445 and meth.rect.y==645:
                    meth.rect.x=950
                    meth.rect.y=250

    if pressed_keys["left"]:
        walking=True
        right=False
        player.rect.x=player.rect.x-2
        if counter%50==0:
            if skin==0:
                player.image=pygame.image.load("heisenberg_lw.png").convert_alpha()
                skin+=1
            elif skin==1:
                player.image = pygame.image.load("heisenberg_l.png").convert_alpha()
                skin += 1
            elif skin==2:
                player.image = pygame.image.load("heisenberg_lw2.png").convert_alpha()
                skin += 1
            elif skin==3:
                player.image = pygame.image.load("heisenberg_l.png").convert_alpha()
                skin = 0
        counter=counter+1
    if pressed_keys["right"]:
        walking=True
        right=True
        player.rect.x = player.rect.x + 2
        if counter%50==0:
            if skin==0:
                player.image=pygame.image.load("heisenberg_rw.png").convert_alpha()
                skin+=1
            elif skin==1:
                player.image = pygame.image.load("heisenberg_r.png").convert_alpha()
                skin += 1
            elif skin==2:
                player.image = pygame.image.load("heisenberg_rw2.png").convert_alpha()
                skin += 1
            elif skin==3:
                player.image = pygame.image.load("heisenberg_r.png").convert_alpha()
                skin = 0
        counter=counter+1

    if player.rect.x > 1130:
        if scene==0:
            scene=1
            player.rect.x=0
            sprite_list.remove(closet,table,cooker,player)
            sprite_list.add(jesse,player)
            floor.image=pygame.image.load("floor_sand.png").convert_alpha()
            if meth.rect.x!=445 and meth.rect.y!=645:
                sprite_list.remove(meth)
        else:
            player.rect.x=player.rect.x-2

    elif player.rect.x < 0:
        if scene==1:
            scene = 0
            player.rect.x = 1130
            sprite_list.remove(jesse, player)
            sprite_list.add(closet, table, cooker, player)
            floor.image = pygame.image.load("floor.png").convert_alpha()
        else:
            player.rect.x=player.rect.x+2

    if player.rect.y > width:
        player.rect.y = player.rect.y - 2

    if walking == False:
        if right==True:
            player.image=pygame.image.load("heisenberg_r.png").convert_alpha()
        else:
            player.image = pygame.image.load("heisenberg_l.png").convert_alpha()

    if scene==0:
        screen.fill(room_bg)
    if scene==1:
        screen.fill(sky_bg)
    player.update()
    sprite_list.draw(screen)
    pygame.display.flip()