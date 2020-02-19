from UdpSocket import UdpSocket
import time

if __name__ == "__main__":
    server = UdpSocket()
    server.start_socket("127.0.0.1", 50000)
    for i in range(10):
        time.sleep(1)
        server.send_to(('127.0.0.1', 27000), "ping")
        print("Attente")
    server.stop_socket()


    
    

