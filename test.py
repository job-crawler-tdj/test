import time
print("Hello World")

now = time.localtime()
current_time = time.strftime("%H:%M:%S", now)

print("Current time is：", current_time)
