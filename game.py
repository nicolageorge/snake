import sys, pygame, time, random
from snake import Snake
from berry import BerryFactory

class Game:
    """the main game running class"""

    def __init__(self):
        pygame.init()
        self.size_window = [800, 600]
        self.screen = pygame.display.set_mode(self.size_window)
        self.initial_berries_no = 5

        # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
        self.myfont = pygame.font.SysFont("monospace", 20)

        self.snake = Snake()
        self.berries = []
        for x in range(self.initial_berries_no):
            self.berries.append(BerryFactory.spawn_random_berry())


    def add_berry(self):
        self.berries.append(BerryFactory.spawn_random_berry())


    def remove_death(self):
        for i, x in enumerate(self.berries):
            if x.type == 'death':
                self.berries.remove(x)
                print "DEATH REMOVED!!!"
                break


    def draw_snake(self):
        for i, x in enumerate(self.snake.data):
            pygame.draw.rect(self.screen, self.snake.color_head if i == 0 else self.snake.color_body, x + self.snake.size)


    def draw_berries(self):
        for i, x in enumerate(self.berries):
            pygame.draw.rect(self.screen, x.color, x.position + x.size)

        
    def draw_score(self):
        txt = "Score : " + str(self.snake.collected_berries)
        label = self.myfont.render(txt, 1, (255,255,255))
        self.screen.blit(label, (30, 30))


    def render(self):
        pygame.draw.rect(self.screen, 0x0, (0, 0, self.size_window[0], self.size_window[1]))
        
        self.draw_score()
        self.draw_snake()
        self.draw_berries()


    def colide_berry(self):
        for i, x in enumerate(self.berries):
            if x.position == self.snake.data[0]:
                self.snake.eat(x)
                self.berries.remove(x)


    def colide_wall(self):
        if self.snake.data[0][0] > self.size_window[0]:
            self.snake.wall_reset('left')
        elif self.snake.data[0][0] < 0:
            self.snake.wall_reset('right')
        elif self.snake.data[0][1] > self.size_window[1]:
            self.snake.wall_reset('top')
        elif self.snake.data[0][1] < 0:
            self.snake.wall_reset('bottom')
        # if self.snake.data
        # print self.snake.data[0]


    def check_collisions(self):
        self.colide_berry()
        self.colide_wall()


    def check_for_victory(self):
        if self.snake.collected_berries >= 10:
            img = pygame.image.load("winscreen.png")
            self.screen.blit(img, (0,0))
            return True
        return False


    def run(self):
        while True and not self.check_for_victory():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.turn_left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn_right()
                    elif event.key == pygame.K_UP:
                        self.snake.turn_up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn_down()

            self.check_for_victory()
            self.snake.move()
            self.check_collisions()
            self.render()
            
            pygame.display.update()

            if random.random() > 0.99:
                self.add_berry()
            if random.random() > 0.999:
                self.remove_death()

            # print (1.0/self.snake.speed)
            time.sleep(1.0/self.snake.speed)


thread = Game()
thread.run()

