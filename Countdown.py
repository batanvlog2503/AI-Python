import time

my_time = int(input("Enter the time in second: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    #print(x)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")

print(time.ctime()) # lấy thời gian hiện tại
print(time.time())