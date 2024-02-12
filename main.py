import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Side-Scrolling Game')
clock = pygame.time.Clock()
FPS = 60

player = [100, 450, 0, 0]
isOnGround = False
offset = 0

platforms = [(600, 500, (100, 300))]


def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10),
                         (platforms[i][0] + offset, platforms[i][1], 100, 30))


def move_player():
    global isOnGround
    global offset

    for i in range(len(platforms)):
        if player[0]+50 > platforms[i][0] + offset and player[0] < platforms[i][0] + 100 + offset and player[i] + 50 > platforms[i][1] and player[1] + 50 < platforms[i][1] + 50:
            isOnGround = True
            player[1] = platforms[i][1] - 50
            player[3] = 0

    if keys[pygame.K_LEFT]:
        if offset > 260 and player[0] > 0:
            player[2] = -5

        elif player[0] > 400 and offset < -1500:
            player[2] = -5

        elif player[0] > 0:
            offset += 5
            player[2] = 0

        else:
            player[2] = 0

    elif keys[pygame.K_RIGHT]:
        player[2] = 5
        offset -= 5
    else:
        player[2] = 0

    if isOnGround == True and keys[pygame.K_UP]:
        player[3] = -15
        isOnGround = False

    if isOnGround == False:
        player[3] += 1

    if player[1] > 535:
        player[1] = 535
        isOnGround = True

    player[0] += player[2]
    player[1] += player[3]


def draw_clouds():
    for x in range(100, 800, 300):
        for i in range(3):
            pygame.draw.circle(screen, (255, 255, 255), (x + offset, 100), 40)
            pygame.draw.circle(screen, (255, 255, 255),
                               (x-50 + offset, 125), 40)
            pygame.draw.circle(screen, (255, 255, 255),
                               (x+50 + offset, 125), 40)
        pygame.draw.rect(screen, (255, 255, 255),
                         (x-50 + offset, 100, 100, 65))


def draw_rect():
    pygame.draw.rect(screen, (56, 78, 29), (0, 540, 800, 100))


def draw_tree():
    for x in range(75, 375, 675):
        for i in range(3):
            pygame.draw.rect(screen, (165, 42, 42), (x + offset, 300, 50, 300))
            pygame.draw.rect(screen, (165, 42, 42),
                             (x + 300 + offset, 300, 50, 300))
            pygame.draw.rect(screen, (165, 42, 42),
                             (x + 600 + offset, 300, 50, 300))
    for x in range(100, 800, 300):
        for i in range(3):
            pygame.draw.circle(screen, (42, 126, 25), (x + offset, 300), 40)
            pygame.draw.circle(screen, (42, 126, 25), (x-50 + offset, 300), 40)
            pygame.draw.circle(screen, (42, 126, 25), (x+50 + offset, 300), 40)


running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # physics
    move_player()

    # render
    screen.fill((135, 206, 235))
    draw_clouds()
    draw_rect()
    draw_tree()
    draw_platforms()
    pygame.draw.rect(screen, (255, 0, 255), (player[0], player[1], 50, 50))
    pygame.display.flip()
pygame.quit()
