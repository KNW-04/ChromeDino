from smtplib import SMTPNotSupportedError
import pygame
import os

pygame.init()

title: str = "JUMP"
pygame.display.set_caption(title)

source_path = os.path.join(os.path.dirname(__file__), "Assets")

screen_size = (screen_width, screen_height) = (1280, 720)
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
fps = 60

ground = 700

spr_img = pygame.image.load(os.path.join(source_path, "IMG_11_small.png"))
spr_ratio = 1.1
spr_size = (spr_width, spr_height) = (124*spr_ratio, 240*spr_ratio)
spr = pygame.transform.scale(spr_img, spr_size)
spr_info = {"x":screen_width / 2 - spr_width / 2, "y":ground - spr_height, "to_x":0, "to_y":0, "spd":2}
spr_pos:tuple = (spr_info["x"], spr_info["y"])
spr_jumped = {"tick":0, "stat":False, "idx":0}

bg = pygame.transform.scale(pygame.image.load(os.path.join(source_path, "IMG_15.png")), (screen_width, screen_height))

jump = lambda t, v: 9.8*(t/1000) - v

running = True
init_ticks = pygame.time.get_ticks()

while running:
    dt = clock.tick(fps)
    game_ticks = pygame.time.get_ticks() - init_ticks

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if spr_jumped["idx"] <= 1:
                    spr_jumped["stat"] = True
                    spr_jumped["tick"] = game_ticks
                    spr_jumped["idx"] += 1
                else:
                    pass

            if event.key == pygame.K_w:
                spr_info["to_y"] = -1*spr_info["spd"]
            if event.key == pygame.K_a:
                spr_info["to_x"] = -1*spr_info["spd"]
            if event.key == pygame.K_d:
                spr_info["to_x"] = spr_info["spd"]
            if event.key == pygame.K_s:
                spr_info["to_y"] = spr_info["spd"]

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                spr_info["to_y"] = 0
            if event.key == pygame.K_a:
                spr_info["to_x"] = 0
            if event.key == pygame.K_d:
                spr_info["to_x"] = 0
            if event.key == pygame.K_s:
                spr_info["to_y"] = 0
            

    if spr_jumped["stat"] == True:
        if spr_info["y"] >= ground - spr_height and spr_jumped["tick"] != game_ticks:
            spr_jumped["stat"] = False
            spr_jumped["tick"] = 0
            spr_jumped["idx"] = 0
        else:
            spr_info["to_y"] = jump(game_ticks - spr_jumped["tick"], spr_info["spd"])
            

    spr_info["x"] += spr_info["to_x"] * dt
    spr_info["y"] += spr_info["to_y"] * dt

    if spr_info["x"] >= screen_width - spr_width: spr_info["x"] = screen_width - spr_width
    elif spr_info["x"] <= 0: spr_info["x"] = 0

    if spr_info["y"] >= ground - spr_height: spr_info["y"] = ground - spr_height
    elif spr_info["y"] <= 0: spr_info["y"] = 0

    screen.blit(bg, (0, 0))
    screen.blit(spr, (spr_info["x"], spr_info["y"]))

    pygame.display.update()


pygame.quit()