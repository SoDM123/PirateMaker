import pygame
from saveAndLoadMap import SaveLoadMap
pygame.init()

display = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()


entities = []
saveloadmanager = SaveLoadMap(".save", "save_map")

#saveloadmanager.load_data("map")

while True:
    display.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            saveloadmanager.save_data(entity,"map")
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                entities.append(mouse_pos)

            if event.button == 3:
                number = 3


    for entity in entities:
        pygame.draw.circle(display, (255,0,0), (entity[0], entity[1]), 10)


    pygame.display.update()
    clock.tick(60)