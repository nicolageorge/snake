# http://www.binarytides.com/code-chat-application-server-client-sockets-python/
import threading, time

class ReadMessage(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self._stop = threading.Event()
        self.socket = socket

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            try:
                data = self.socket.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    self.stop()
                    break
                else:
                    # print data
                    print 'received message', data
            except:
                pass

            time.sleep(0.032)
