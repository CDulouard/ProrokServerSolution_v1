from UdpSocket import UdpSocket
from Message import Message
import time

if __name__ == "__main__":
    server = UdpSocket()
    server.start_socket("127.0.0.1", 50000, "test")
    for i in range(5):
        time.sleep(1)
        server.send_to(('127.0.0.1', 27000), str(Message(1, Message.creat_connection_message(server.hash_password, verbose=1))))
        # server.send_to(('127.0.0.1', 27000),  str(Message(1, '{"password": "' + str(server.hash_password) + '" , "verbose": 1}') ))
        # server.send_to(('127.0.0.1', 27000), "ping")
        print("Attente")
    server.send_to(('127.0.0.1', 27000), str(Message(2, "test")))
    time.sleep(1)
    server.stop_socket()
