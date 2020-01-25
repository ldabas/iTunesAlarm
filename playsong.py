
import sys
from subprocess import Popen, PIPE
import schedule
import time

wakeupTime = str(sys.argv[1])

def music(script):

	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
	stdout, stderr = p.communicate(script)

	print(p.returncode, stdout, stderr)

def job():
	for i in range(0,2):
		try:
			music('tell application "Music" to activate')
			music('tell application "Music" to play the playlist named "WakeUp"')
		except:
			music('tell application "Music" to play the playlist named "WakeUp"')		


schedule.every().day.at(wakeupTime).do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)


