import time
def remaintime(t):
    if t == 0:
        a = "time is over."
        return a
    else:
        print("waits for", str(t), "seconds." )
        time.sleep(1)
        return remaintime(t - 1)

print(remaintime(10))