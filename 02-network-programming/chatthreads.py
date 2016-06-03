from threading import Thread, Event


class ConversThread(Thread):
    def __init__(self, socket, stop_event):
        Thread.__init__(self)
        self._sckt = socket
        self._stop_event = stop_event
        self.daemon = True
        self.buffsize = 1024
        self.encoding = 'utf-8'

    def not_stopped(self):
        return not self._stop_event.is_set()

    def stop(self):
        self._stop_event.set()


class ReceiverThread(ConversThread):
    def run(self):
        while self.not_stopped():
            recvd_data = self._sckt.recv(self.buffsize).decode(self.encoding)
            if not recvd_data:
                self.stop()
                break
            print('\nReceived message:', recvd_data)

class SenderThread(ConversThread):
    def run(self):
        while self.not_stopped():
            data_to_send = input('Enter a message: ')
            self._sckt.sendall(bytes(data_to_send, self.encoding))
