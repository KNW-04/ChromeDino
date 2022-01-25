import pygame
import os

pygame.init()

assets = os.path.join(os.path.dirname(__file__), "Assets")

screen_size = (screen_width, screen_height) = (1280, 720)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
fps = 120

bg = pygame.image.load(os.path.join(assets, "IMG_15.png"))

ground = 700

stage_a = pygame.image.load(os.path.join(assets, "stage.png"))
stage_a_x = 0

stage_b = stage_a
stage_b_x = screen_width

stage_spd = 2


running = True

spacebaridx = 0
gamestart = False
tick_on_start = 0

def move_stage(gamestat:bool, stage_a_x:int, stage_b_x:int, dt:int) -> tuple: 
    if gamestat == True:
        if stage_b_x <= 0:
            stage_b_x = screen_width
            stage_a_x = 0
        stage_a_x += stage_spd * dt * -1
        stage_b_x += stage_spd * dt * -1

    return stage_a_x, stage_b_x


while running:
    dt = clock.tick(fps)

    if gamestart == True:
        game_ticks = pygame.time.get_ticks() - tick_on_start
    else:
        game_ticks = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if spacebaridx == 0: # Press space to start / to tell whether it's the first press
                    spacebaridx += 1
                    gamestart = True
                    tick_on_start = pygame.time.get_ticks()
                else:
                    pass # Jump


    stage_a_x, stage_b_x = move_stage(gamestart, stage_a_x, stage_b_x, dt)

    screen.blit(bg, (0, 0))
    screen.blit(stage_a, (stage_a_x, ground))
    screen.blit(stage_b, (stage_b_x, ground))
    pygame.display.update()

pygame.quit()