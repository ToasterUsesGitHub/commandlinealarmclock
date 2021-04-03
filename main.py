import random
import time
import webbrowser


def run():
    videos = [
        "https://www.youtube.com/watch?v=QYBVHJm6tS4&t=23s",
        "https://www.youtube.com/watch?v=d9mUGr7yoIM",
        "https://www.youtube.com/watch?v=XqZsoesa55w"
    ]
    hour = int(input("What hour do you want to wake up in 24HR time?   "))
    minute = int(
        input("What minute of the hour would you like to wake up?   "))
    hour_now = int(time.strftime('%H'))
    minute_now = int(time.strftime('%M'))
    hourfinal = hour_now - hour
    hourfinal = hourfinal * 60 + hourfinal * 60
    minutefinal = minute - minute_now
    minutefinal = minutefinal * 60
    final = hourfinal + minutefinal
    randomvideo = random.choice(videos)
    time.sleep(int(final))
    webbrowser.open(randomvideo)
    runagain = str(input("Would you like to run the alarm again?(y/n)  "))
    if runagain == "y" or runagain == "Y":
        run()
    elif runagain == "n" or runagain == "N":
        print("Alarm clock stopped.")
run()
