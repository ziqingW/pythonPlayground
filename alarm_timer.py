import time
import string
import winsound

def alarmClock():
  while True:
    try:
      min = float(raw_input("How long do you want to sleep, in minutes? >>"))
    except:
      print "It's wrong format, input again."
    else:
      if min <= 0:
        print "It's too short to be true, try again."
        continue
      else:
        fre = 2500
        dur = 1000
        print "Sleeping ~~~"
        seconds = min * 60
        time.sleep(seconds)
        print "Wake UP!"
        winsound.Beep(fre, dur)


alarmClock()