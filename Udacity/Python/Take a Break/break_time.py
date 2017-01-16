import webbrowser
import time

total_break = 3
break_count = 0

print("This program started on: " + time.ctime())
while (break_count <= total_break):
    time.sleep(2)
    webbrowser.open("https://www.facebook.com/", new=2)
    break_count += 1

print("This program finished on: " + time.ctime())

