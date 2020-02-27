import socket
from threading import Thread
from typing import Optional
import hashlib
import time
from Message import Message
from robotDataOld import RobotDataOld
import pandas as pd


class UdpSocket(Thread):

    def __init__(self, buffer_size: Optional[int] = 1024) -> None:
        """
        Default constructor for UdpSocket object
        :param buffer_size: The size of the buffer used for communication
        """
        Thread.__init__(self)
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.buffer_size: int = buffer_size
        self.hash_password: str = ""
        self.is_running: bool = False
        self.port = None
        self.ip_address = None

    def start_socket(self, ip_address_server: str, port_server: int, password: Optional[str] = "") -> None:
        """
        The method used to start a UdpSocket object. It will creat a new Thread to allow asynchronous process.
        :param ip_address_server: The host used by the socket
        :param port_server: The port used by the socket
        :param password: The password used to connect to the socket
        :return: None
        """
        self.port = port_server
        self.ip_address = ip_address_server
        self.socket.bind((ip_address_server, port_server))
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.hash_password = hashlib.sha1(bytes(password, "utf8")).hexdigest()
        self.start()

    def stop_socket(self) -> None:
        """
        The method to stop the socket and stop the associated Thread.
        :return: None
        """
        self.is_running = False
        self.socket.shutdown(socket.SHUT_RD)
        self.socket.close()
        self.join()

    def run(self) -> None:
        """
        This method start the socket's Thread
        :return:
        """
        self.is_running = True
        self.receive()

    def receive(self) -> None:
        """
        This method manage the receive process. It call handler method to manage the different jobs to do when a new
        message is received.
        :return:
        """
        while self.is_running:
            try:
                data, address = self.socket.recvfrom(1024)  # buffer size is 1024 bytes
                self.handler(data, address)

            except OSError:
                pass
            except:
                print("Receive error")

    def handler(self, data: bytes, address) -> None:
        """
        This method codes the socket's behaviour when a new message is received.
        :param data: The data in bytes that were received.
        :param address: The address and port of the remote machine that send the message
        :return: None
        """
        print(f"From : \nip address : {address[0]}\nport : {address[1]}")
        print("received message:", data)

    def send_to(self, address_port, message: str) -> None:
        """
        This method allow the socket to send a message to a remote machine.
        :param address_port: A tuple containing the address and port of the destination ex: (127.0.0.1, 50000)
        :param message: A string message to send
        :return: None
        """
        self.socket.sendto(str.encode(message, 'utf8'), address_port)

    def old_connection(self, address_port, password: str, hash_pass: Optional[bool] = True) -> None:
        """
        This method send a connection request to a remote machine using old Prorok's communication protocol.
        :param address_port: A tuple containing the address and port of the destination ex: (127.0.0.1, 50000)
        :param password: The password to send to ask for connection. It can be hashed or not.
        :param hash_pass: If the given password isn't hashed then this must be true to hash the password before sending
        it.
        :return: None
        """
        if hash_pass:
            hash_password = hashlib.sha1(bytes(password, "utf8")).hexdigest()
        else:
            hash_password = password
        self.send_to(address_port,
                     str(Message(1, Message.spe_creat_connection_message(hash_password, port=self.port))))

    def send_old_commands(self, address_port, pos_list: Optional[list] = None,
                          torque_list: Optional[list] = None) -> None:
        """
        This method send to the robot CLOVIS MINI the new position and torque using old Prorok's communication protocol.
        :param address_port: A tuple containing the address and port of the destination ex: (127.0.0.1, 50000)
        :param pos_list: The list of position to send. It must have a length of 22 and the position have to be in the
        correct order based on robotDataOld motor_keys order. If empty it will send 1 to all motors.
        :param torque_list: The list of torques to send. It must have a length of 22 and the torques have to be in the
        correct order based on robotDataOld motor_keys order. If empty it will send 100 to all motors.
        :return:
        """
        robot = RobotDataOld()
        if torque_list is None:
            torque_list = [100 for i in range(len(robot.motor_keys))]

        if pos_list is None:
            pos_list = [1 for i in range(len(robot.motor_keys))]

        if len(pos_list) != len(robot.motor_keys):
            print("SIZE ERROR")
            print("check out the number of arguments for \"Position values\"")
        else:
            j = 0
            for i in robot.motor_keys:
                robot.targets[i]["position"] = pos_list[j]
                j += 1
        if len(torque_list) != len(robot.motor_keys):
            print("SIZE ERROR")
            print("check out the number of arguments for \"Torque values\"")
        else:
            j = 0
            for i in robot.motor_keys:
                robot.targets[i]["torque"] = torque_list[j]
                j += 1
        self.send_to(address_port, str(Message(5, str(robot))))

    def send_animation(self, address_port, excel_path: str) -> None:
        """
        This method send several positions to the robot with a given delay between each command. The commands must be
        stored in an excel file with the same shape than the one given in this project.
        :param address_port: A tuple containing the address and port of the destination ex: (127.0.0.1, 50000)
        :param excel_path: The path to the excel file
        :return: None
        """
        df = pd.read_excel(excel_path)
        for i in range(len(df)):
            pos = list(df.iloc[i][2:])
            print(pos)
            self.send_old_commands(address_port, pos)
            time.sleep(list(df.iloc[i])[1] / 1000)
