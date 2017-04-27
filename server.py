# http://www.binarytides.com/code-chat-application-server-client-sockets-python/

import socket, select, random, time, json

CONNECTION_LIST = []
RECV_BUFFER = 4096  # Advisable to keep it as an exponent of 2
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)

CONNECTION_LIST.append(server_socket)

print "Chat server started on port " + str(PORT)



players = {}

def create_player(key):
    global players
    player_x = random.randint(0, 608)
    player_y = random.randint(0, 448)
    player_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    players[key] = {
        "x": player_x,
        "y": player_y,
        "color": player_color
    }


def broadcast_data(event, message, sock=None):
    for socket in CONNECTION_LIST:
        if socket != server_socket and (socket != sock or sock is None):
            try :
                socket.send(json.dumps({
                    'event': event,
                    'message': message
                }))
            except Exception as e:
                print 'socket emit error', e
                socket.close()
                CONNECTION_LIST.remove(socket)

while 1:
    # Get the list sockets which are ready to be read through select
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

    for sock in read_sockets:
        if sock == server_socket:
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)

            create_player(addr[1])

            print "Client (%s, %s) connected" % addr

            print players

            broadcast_data('draw-players', players)

            for i in range(100):
                broadcast_data('draw-players', players)
                time.sleep(1)



        # Some incoming message from a client
        else:
            # Data recieved from client, process it
            try:
                # In Windows, sometimes when a TCP program closes abruptly,
                # a "Connection reset by peer" exception will be thrown
                data = sock.recv(RECV_BUFFER)
                if data:
                    print '---', data
                    pass
                    # broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)

            except:
                # broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                print "Client (%s, %s) is offline" % addr
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue

server_socket.close()
