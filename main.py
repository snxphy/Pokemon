import pygame
import button
import os 
import subprocess
from pygame import mixer

width, height = 800, 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pokemon Showdown!")

pygame.init()
clock = pygame.time.Clock()

bg = pygame.image.load("image/pokemon.jpg")

start_img = pygame.image.load("image/button/start_btn.png").convert_alpha()
exit_img = pygame.image.load("image/button/exit_btn.png").convert_alpha()

start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

mixer.init()
mixer.music.load("pkmon.mp3")
mixer.music.play(-1)
mixer.music.set_volume(1)
exit_sound = pygame.mixer.Sound("mario-scream.wav")
start_sound = pygame.mixer.Sound("Pikaaaa.mp3")


run = True
while run:

    screen.blit(bg, (0, 0))

    if start_button.draw(screen):
        pygame.mixer.Sound.play(start_sound)
        pygame.time.delay(50)
        subprocess.Popen('C:\\Program Files (x86)\\Pokemon Showdown\\pokemonshowdown.exe')

    if exit_button.draw(screen):
        run = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.time.delay(50)
            pygame.mixer.Sound.play(exit_sound)
            pygame.time.delay(50)
            run = False
        
    pygame.display.update()

pygame.quit()
