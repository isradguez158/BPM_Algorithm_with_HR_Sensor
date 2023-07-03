import numpy as np
#import matplotlib.pyplot as plt
import time
import datetime as dt

import HR as HR
import datetime
import RPi.GPIO as GPIO

date = datetime.datetime.now()
    
def write_csv(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12):
    with open("/home/isra/isra/"+str(date)+".csv", "a") as log:
        log.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}\n".format(str(V1),str(V2),str(V3),str(V4),str(V5),str(V6),str(V7),str(V8),str(V9),str(V10),str(V11),str(V12)))

with open("/home/isra/isra/"+str(date)+".csv", "a") as log:
    log.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}\n".format("t","L_tor","R_tor","L_Cmd","R_Cmd","0", "0","L_Enc_angle","R_Enc_angle","L_Enc_Vel","R_Enc_vel","Heart_Rate"))


print("Begin")

start = time.time()
now = 0
t_pr1 = 0
t_pr2 = 0
Delta_T1 = .02

Hr = HR.HR(21)
HR=0

while(True):
    Hr.Read_HR()
    now=(time.time()-start)

    if (Hr.BPM > 87 and Hr.BPM < 200):
        HR=Hr.BPM
        
    if (now - t_pr2 > .5):
        t_pr2 = now
        print("time: " + str(now)+" BPM: " + str(HR))
     
    if (now - t_pr1 > .01):
        t_pr1 = now
        write_csv(now,0,0,0,0,0,0,0,0,0,0,HR)

    
    
