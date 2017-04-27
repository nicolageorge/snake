import random

class Snake:
    def __init__(self):
        self.size_window = [800,600]
        self.size = [10, 10]
        self.color_head = (255, 0, 255)
        self.color_body = (0, 204, 102)
        self.initial_size = 20
        self.speed = 20
        
        self.dx = 1 #
        self.dy = 0

        self.start_pos = [x/2 for x in self.size_window]
        self.data = [[self.start_pos[0], self.start_pos[1]]]
        self.collected_berries = 0
        
        for x in range(self.initial_size):
            """fill the snake"""
            self.data.append([self.data[x][0]-self.size[0], self.start_pos[1]])


    def move(self):
        for i in range(len(self.data)-1, 0, -1):
            self.data[i][0] = self.data[i-1][0]
            self.data[i][1] = self.data[i-1][1]

        self.data[0][0] += self.size[0] * self.dx
        self.data[0][1] += self.size[1] * self.dy


    def drink(self):
        if random.random() > 0.6:
            self.move_in_random_direction()
        else:
            self.puke()


    def puke(self):
        remaining = int(0.7 * len(self.data))

        for i in range(remaining, len(self.data), 1):
            pass
            # self.data[i][0] = self.data[i][0]+20
            # self.data[i][1] = self.data[i][1]+20

        print "PUKING!!!!"


    def move_in_random_direction(self):
        direction = random.randint(0, 4)
        if direction == 0:
            self.dx = -1
            self.dy = 0
        elif direction == 1:
            self.dx = 0
            self.dy = 1
        elif direction == 2:
            self.dx = 0
            self.dy = -1
        elif direction == 3:
            self.dx = 1
            self.dy = 0                



    def wall_reset(self, wall):
        if wall == 'left':
            self.data[0][0] = 0
        elif wall == 'right':
            self.data[0][0] = self.size_window[0]
        elif wall == 'top':
            self.data[0][1] = 0
        elif wall == 'bottom':
            self.data[0][1] = self.size_window[1]


    def modify_speed(self, modifier):
        self.speed = self.speed + modifier


    def modify_collected_berries(self, modifier):
        self.collected_berries = self.collected_berries + modifier

    def eat(self, berry):
        if berry.type == 'death':
            self.modify_speed(-10)
            self.modify_collected_berries(-10)
        else:
            x = self.data[len(self.data)-1][0]
            y = self.data[len(self.data)-1][1]
            # y = 0
            self.data.append([x, y])
            self.modify_speed(+1)
            self.modify_collected_berries(+1)

            if random.random() > 0.7:
                self.drink()
            # print self.data

            if berry.type == 'mushroom':
                if random.random() > 0.2:
                    self.eat(berry)
                else:
                    berry.reset_to_normal()
                    self.eat(berry)
            

    def turn_left(self):
        if self.dx is not 1:
            self.dx = -1
            self.dy = 0


    def turn_right(self):
        if self.dx is not -1:
            self.dx = 1
            self.dy = 0


    def turn_up(self):
        if self.dy is not 1:
            self.dx = 0
            self.dy = -1


    def turn_down(self):
        if self.dy is not -1:
            self.dx = 0
            self.dy = 1