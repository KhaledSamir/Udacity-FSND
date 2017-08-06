import webbrowser;
import time;

print("Start counting to 3 ...");
mycount = 0
print(time.ctime());
secs = input("Enter how many seconds you wanna the program to wait")
while(mycount < 3) :
        time.sleep(secs);
        webbrowser.open("https://www.youtube.com/watch?v=NxLQK2xLoSs&index=5&list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbAVMdT2owtxkU8k");
        mycount += 1;


