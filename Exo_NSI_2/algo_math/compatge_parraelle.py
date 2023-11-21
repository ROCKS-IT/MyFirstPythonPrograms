import threading
import time

def hello(n):
    for i in range(5):
        print("je suis tache",n,"et ma valueur et",i)
    print("-------- fin de tache",n)

th = []
for n in range(4):
    t = threading.Thread(target = hello, args=[n])
    t.start()
    th.append(t)

for t in th:
    t.join()

input("apuy su enter")
