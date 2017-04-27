# http://www.binarytides.com/code-chat-application-server-client-sockets-python/

# telnet program example
import socket, select, string, sys, pygame, time, json, random
from read_message import *


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

if (len(sys.argv) < 3):
    print 'Usage : python telnet.py hostname port'
    sys.exit()

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

# connect to remote host
try:
    s.connect((host, port))
except:
    print 'Unable to connect'
    sys.exit()

print 'Connected to remote host. Start sending messages'





class Player(pygame.sprite.Sprite):
    def __init__(self, id, color, x, y, width=32, height=32):
        super(Player, self).__init__()

        self.id = id

        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test1")

all_sprites_list = pygame.sprite.Group()



# p = Player('p1', (255, 0, 0), 100, 100)
# all_sprites_list.add(p)

screen.fill((0, 0, 0))
all_sprites_list.update()
all_sprites_list.draw(screen)
pygame.display.flip()


s.send('==============')
s.settimeout(1)

def draw_players(players):
    print 'draw players', players
    global all_sprites_list, screen

    all_sprites_list = pygame.sprite.Group()

    for player_key in players:
        player = players[player_key]
        p = Player('p1', player['color'], player['x'], player['y'])
        all_sprites_list.add(p)

    screen.fill((0, 0, 0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()

def handle_event(data):
    event = data['event']
    message = data['message']

    print 'handle event', event, message
    if event == 'draw-players':
        draw_players(message)



# r = ReadMessage(s)
# r.start()

while True:
    screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.display.flip()
    time.sleep(0.016)
