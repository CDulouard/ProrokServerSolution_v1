from UdpSocket import UdpSocket
from Message import Message
import time

if __name__ == "__main__":
    server = UdpSocket()
    server.start_socket("192.168.50.85", 50000, "test")
    # server.start_socket("127.0.0.1", 50000, "test")
    # for i in range(5):
    #     time.sleep(1)
    #     server.send_to(('127.0.0.1', 27000), str(Message(1, Message.creat_connection_message(server.hash_password, verbose=1))))
    #     print("Attente")
    # time.sleep(1)
    for i in range(5):
        print(str(Message(1, Message.spe_creat_connection_message(server.hash_password, verbose=1))))
        server.send_to(('192.168.50.1', 50056),
                       str(Message(1, Message.spe_creat_connection_message(server.hash_password, verbose=1))))
        time.sleep(0.1)

    time.sleep(1)
    server.send_to(('192.168.50.1', 50056), str(Message(5, '{"targets": {"rAnkleRX": {"position": 0, "torque": 0}, "lAnkleRX": {"position": 0, "torque": 0}, "rAnkleRZ": {"position": 0, "torque": 0}, "lAnkleRZ": {"position": 0, "torque": 0}, "rShoulderRY": {"position": 0, "torque": 0}, "lShoulderBaseRY": {"position": 0, "torque": 0}, "rShoulderBaseRY": {"position": 0, "torque": 0}, "lShoulderRY": {"position": 0, "torque": 0}, "rShoulderRZ": {"position": 0, "torque": 0}, "lShoulderRZ": {"position": 0, "torque": 0}, "rKneeRX": {"position": 0, "torque": 0}, "lKneeRX": {"position": 0, "torque": 0}, "rHipRX": {"position": 0, "torque": 0}, "lHipRX": {"position": 0, "torque": 0}, "rHipRY": {"position": 0, "torque": 0}, "lHipRY": {"position": 0, "torque": 0}, "rHipRZ": {"position": 0, "torque": 0}, "lHipRZ": {"position": 0, "torque": 0}, "headRX": {"position": 0, "torque": 0}, "rElbowRX": {"position": 0, "torque": 0}, "lElbowRX": {"position": 0, "torque": 0}, "torsoRY": {"position": 0, "torque": 0}}}')))
    time.sleep(1)
    server.send_to(('192.168.50.1', 50056), str(Message(5,
                                                        '{"targets": {"rAnkleRX": {"position": 0, "torque": 0}, "lAnkleRX": {"position": 0, "torque": 0}, "rAnkleRZ": {"position": 0, "torque": 0}, "lAnkleRZ": {"position": 0, "torque": 0}, "rShoulderRY": {"position": 0, "torque": 0}, "lShoulderBaseRY": {"position": 0, "torque": 0}, "rShoulderBaseRY": {"position": 0, "torque": 0}, "lShoulderRY": {"position": 0, "torque": 0}, "rShoulderRZ": {"position": 0, "torque": 0}, "lShoulderRZ": {"position": 0, "torque": 0}, "rKneeRX": {"position": 0, "torque": 0}, "lKneeRX": {"position": 0, "torque": 0}, "rHipRX": {"position": 0, "torque": 0}, "lHipRX": {"position": 0, "torque": 0}, "rHipRY": {"position": 0, "torque": 0}, "lHipRY": {"position": 0, "torque": 0}, "rHipRZ": {"position": 0, "torque": 0}, "lHipRZ": {"position": 0, "torque": 0}, "headRX": {"position": 0, "torque": 0}, "rElbowRX": {"position": 0, "torque": 0}, "lElbowRX": {"position": 0, "torque": 0}, "torsoRY": {"position": 0, "torque": 0}}}')))
    time.sleep(1)
    server.send_to(('192.168.50.1', 50056), str(Message(5,
                                                        '{"targets": {"rAnkleRX": {"position": 0, "torque": 0}, "lAnkleRX": {"position": 0, "torque": 0}, "rAnkleRZ": {"position": 0, "torque": 0}, "lAnkleRZ": {"position": 0, "torque": 0}, "rShoulderRY": {"position": 0, "torque": 0}, "lShoulderBaseRY": {"position": 0, "torque": 0}, "rShoulderBaseRY": {"position": 0, "torque": 0}, "lShoulderRY": {"position": 0, "torque": 0}, "rShoulderRZ": {"position": 0, "torque": 0}, "lShoulderRZ": {"position": 0, "torque": 0}, "rKneeRX": {"position": 0, "torque": 0}, "lKneeRX": {"position": 0, "torque": 0}, "rHipRX": {"position": 0, "torque": 0}, "lHipRX": {"position": 0, "torque": 0}, "rHipRY": {"position": 0, "torque": 0}, "lHipRY": {"position": 0, "torque": 0}, "rHipRZ": {"position": 0, "torque": 0}, "lHipRZ": {"position": 0, "torque": 0}, "headRX": {"position": 0, "torque": 0}, "rElbowRX": {"position": 0, "torque": 0}, "lElbowRX": {"position": 0, "torque": 0}, "torsoRY": {"position": 0, "torque": 0}}}')))
    time.sleep(10)

    server.stop_socket()
