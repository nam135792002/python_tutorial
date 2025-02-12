import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_email():
    time.sleep(4)
    print("You get the email")

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_email)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")
