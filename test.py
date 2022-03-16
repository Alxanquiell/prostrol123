# task.py
from multiprocessing.managers import BaseManager,Namespace
from multiprocessing import Process, Queue, Manager
import time


if __name__=="__main__":
	que=Queue()
	lista=["listaaaaa","lissss"]
	BaseManager.register("zxc",callable=lambda:que)
	BaseManager.register("lista_d",callable=lambda:lista)
	m=BaseManager(address=("127.0.0.1",50000),authkey=b"1234567890")
	m.get_server().serve_forever()
