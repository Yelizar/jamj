import pygame
pygame.init()

window = pygame.display.set_mode((400, 650))  # screen object(width,height)
pygame.display.set_caption('jamj')

run = True

while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_ESCAPE]:
        run = False
# created by Fral
