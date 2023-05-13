import time
print("Hello World")

now = time.localtime()
current_time = time.strftime("%H:%M:%S", now)

print("Current timef is：", current_time)
