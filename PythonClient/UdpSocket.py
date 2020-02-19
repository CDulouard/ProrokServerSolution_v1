import socket
from threading import Thread
from typing import Optional
import hashlib
import time


class UdpSocket(Thread):

    def __init__(self, buffer_size: Optional[int] = 1024) -> None:
        Thread.__init__(self)
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.buffer_size: int = buffer_size
        self.hash_password: str = ""
        self.is_running: bool = False

    def start_socket(self, ip_address_server: str, port_server: int, password: Optional[str] = "") -> None:
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

    def send_to(self, address, message: str):
        self.socket.sendto(str.encode(message, 'utf8'), address)
