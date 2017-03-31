import sys, pygame, time, random
pygame.init()

# set up all variables
size_window = [800, 600]
snake_start_pos = [x/2 for x in size_window]
snake_size = [10, 10]
c_snake_head = (255, 0, 255)
c_snake_body = (255, 0, 0)
# here we will store the Rama
snake_data = [[snake_start_pos[0], snake_start_pos[1]]]
dx = 1 #
dy = 0


# initial setup
screen = pygame.display.set_mode(size_window)

def render_snake():
    pygame.draw.rect(screen, 0x0, (0, 0, size_window[0], size_window[1]))
    for i, x in enumerate(snake_data):
        pygame.draw.rect(screen, c_snake_head if i == 0 else c_snake_body, x + snake_size)


def move_snake():
    for i in range(len(snake_data)-1, 0, -1):
        snake_data[i][0] = snake_data[i-1][0]
        snake_data[i][0] = snake_data[i-1][0]

    snake_data[0][0] += snake_size[0] * dx
    snake_data[0][1] += snake_size[1] * dy


def grow_snake():
    x = snake_data[len(snake_data)-1][0]
    y = snake_data[len(snake_data)-1][0]
    snake_data.append([x, y])


for x in range(5):
    """fill the snake"""
    snake_data.append([snake_data[x][0]-snake_size[0], snake_start_pos[1]])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass


    move_snake()
    render_snake()

    # check colisions 

    pygame.display.update()

    if random.random() > 0.7:
        grow_snake()

    time.sleep(0.16)
