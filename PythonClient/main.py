from UdpSocket import UdpSocket
from Message import Message
import time

if __name__ == "__main__":
    # server = UdpSocket()
    # server.start_socket("127.0.0.1", 50000, "test")
    # for i in range(5):
    #     time.sleep(1)
    #     server.send_to(('127.0.0.1', 27000), str(Message(1, Message.creat_connection_message(server.hash_password, verbose=1))))
    #     print("Attente")
    # time.sleep(1)

    # server = UdpSocket()
    # server.start_socket("192.168.43.100", 50000, "test")
    # for i in range(5):
    #     time.sleep(1)
    #     server.send_to(('192.168.43.81', 50000), str(Message(1, Message.creat_connection_message(server.hash_password, verbose=1))))
    #     print("Attente")
    # time.sleep(1)

    server = UdpSocket()
    address_robot = ("192.168.50.1", 50056)

    server.start_socket("192.168.50.85", 50000, "test")

    for i in range(5):
        time.sleep(.2)
        server.old_connection(address_robot, "test")
        print("Attente")
    time.sleep(1)
    # server.send_old_commands(address_robot)
    server.send_animation(address_robot, r"./Default_Clovis_routine.xlsx")
    server.stop_socket()
