import time as t
time_now = t.localtime()
print(time_now)
print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")

print(time_now)

tt = t.time()
print(tt)

time_now = t.time()
delivery_time = time_now + ( 86400 * 7)
print(t.localtime(delivery_time))

t.sleep(5)
