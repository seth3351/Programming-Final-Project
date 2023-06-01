import pygame
pygame.init()
dis=pygame.display.set_mode((700,600))
pygame.display.update()
pygame.display.set_caption('Big Seths Snake Game')





CRAZY_BLUE = (50,192,203)
GRAY = (128, 128, 128)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = WHITE
dis.fill(BACKGROUND_COLOR)

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            pygame.quit
            SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -5
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 5
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(CRAZY_BLUE)
    pygame.draw.rect(dis, WHITE, [x1, y1, 10, 10])
    pygame.display.update()
 
    clock.tick(30)
    pygame.draw.rect(dis, WHITE, [200,150,10,10])
    pygame.display.update()
pygame.quit()
quit()