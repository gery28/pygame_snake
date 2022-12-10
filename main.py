import pygame

WIDTH, HEIGHT = 800, 400
BG_COLOR = (140, 137, 246)
BIRD_SPEED = 1
SIZE=100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_surf_1 = pygame.image.load('robot/robot/Run_1.png').convert_alpha()
bird_surf_2 = pygame.image.load('robot/robot/Run_2.png').convert_alpha()
bird_surf_3 = pygame.image.load('robot/robot/Run_3.png').convert_alpha()
bird_surf_4 = pygame.image.load('robot/robot/Run_4.png').convert_alpha()
bird_surf = [pygame.transform.scale(bird_surf_1,(SIZE,SIZE)), pygame.transform.scale(bird_surf_2,(SIZE,SIZE)), pygame.transform.scale(bird_surf_3,(SIZE,SIZE)), pygame.transform.scale(bird_surf_4,(SIZE,SIZE))]
bird_surf_reverse = [pygame. transform. flip(pygame.transform.scale(bird_surf_1,(SIZE,SIZE)),True,False),pygame. transform. flip(pygame.transform.scale(bird_surf_2,(SIZE,SIZE)),True,False),pygame. transform. flip(pygame.transform.scale(bird_surf_3,(SIZE,SIZE)),True,False),pygame. transform. flip(pygame.transform.scale(bird_surf_4,(SIZE,SIZE)),True,False)]

'''
Képek tárolása egyszerűbben:
bird_surf = []
for index in range(1, 5):
    bird_surf.append((pygame.image.load(f'img/bird{index}.png')).convert_alpha())
'''

bird_index = 0
bird_rect = bird_surf[bird_index].get_rect(midleft=(270, HEIGHT / 2))
game_font = pygame.font.SysFont('arial', 60)
counter = 0
running = True
bird_foward=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type== pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         if BIRD_SPEED>0:
        #             BIRD_SPEED-=1
        #     if event.key == pygame.K_RIGHT:
        #         BIRD_SPEED+=1
    screen.fill(BG_COLOR)
    counter += 1
    if counter % 7 == 0:
        bird_index += 1
    if bird_index > len(bird_surf) - 1:
        bird_index = 0
    if bird_rect.right < 534 and bird_foward:
        bird_rect.left += BIRD_SPEED
    elif not bird_rect.right < 534 and bird_foward:
        bird_foward = False
        BIRD_SPEED+=1
        bird_rect = bird_surf[0].get_rect(midright=(533, HEIGHT / 2))
    elif bird_rect.left > 266 and not bird_foward:
        bird_rect.right -= BIRD_SPEED
    elif not bird_rect.left > 266 and not bird_foward:
        bird_foward = True
        BIRD_SPEED+=1
        bird_rect = bird_surf[0].get_rect(midleft=(267, HEIGHT / 2))
    if bird_foward:
        screen.blit(bird_surf[bird_index], bird_rect)
    else:
        screen.blit(bird_surf_reverse[bird_index], bird_rect)
    score_surf = game_font.render('Speed: ' + str(BIRD_SPEED), True, (255, 0, 0))
    screen.blit(score_surf,(0,0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()