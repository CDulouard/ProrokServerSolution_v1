from Message import *
from Server import *
import time

if __name__ == "__main__":
    server = Server("127.0.0.1", 50000, "test")
    server.start()
    time.sleep(5)
    server.stop()
    
    

