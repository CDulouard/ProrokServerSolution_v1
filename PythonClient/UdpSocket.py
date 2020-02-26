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
        Thread.__init__(self)
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.buffer_size: int = buffer_size
        self.hash_password: str = ""
        self.is_running: bool = False
        self.port = None
        self.ip_address = None

    def start_socket(self, ip_address_server: str, port_server: int, password: Optional[str] = "") -> None:
        self.port = port_server
        self.ip_address = ip_address_server
        self.socket.bind((ip_address_server, port_server))
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.hash_password = hashlib.sha1(bytes(password, "utf8")).hexdigest()
        self.start()

    def stop_socket(self):
        self.is_running = False
        self.socket.shutdown(socket.SHUT_RD)
        self.socket.close()
        self.join()

    def run(self) -> None:
        self.is_running = True
        self.receive()

    def receive(self) -> None:
        while self.is_running:
            try:
                data, address = self.socket.recvfrom(1024)  # buffer size is 1024 bytes
                self.handler(data, address)

            except OSError:
                pass
            except:
                print("Receive error")

    def handler(self, data: bytes, address):
        print(f"From : \nip address : {address[0]}\nport : {address[1]}")
        print("received message:", data)

    def send_to(self, address_port, message: str):
        self.socket.sendto(str.encode(message, 'utf8'), address_port)

    def old_connection(self, address_port, password: str, hash_pass: Optional[bool] = True):
        if hash_pass:
            hash_password = hashlib.sha1(bytes(password, "utf8")).hexdigest()
        else:
            hash_password = password
        self.send_to(address_port,
                     str(Message(1, Message.spe_creat_connection_message(hash_password, port=self.port))))

    def send_old_commands(self, address_port, pos_list: Optional[list] = None, torque_list: Optional[list] = None):
        robot = RobotDataOld()
        if torque_list is None:
            torque_list = [100 for i in range(len(robot.motor_keys))]

        if pos_list is None:
            pos_list = [0 for i in range(len(robot.motor_keys))]

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

    def send_animation(self, address_port, excel_path: str):
        df = pd.read_excel(excel_path)
        for i in range(len(df)):
            pos = list(df.iloc[i][2:])
            print(pos)
            self.send_old_commands(address_port, pos)
            time.sleep(list(df.iloc[i])[1]/1000)
