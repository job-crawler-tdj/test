import time
print("Hello World")

now = time.localtime()
current_time = time.strftime("%H:%M:%S", now)

print("現在的時間是：", current_time)
