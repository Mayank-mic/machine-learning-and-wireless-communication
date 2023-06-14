import uhd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score



import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('/dev/ttyACM0',9600) #Create Serial port object called arduinoSerialData
# time.sleep(1)



rbf_svc = SVC(kernel='linear')

#from uhd import stream
usrp =uhd.usrp.MultiUSRP()

model = joblib.load('/home/narendra/Downloads/model2_finalized.pkl')
#Set USRP Paramters
usrp.set_rx_rate(30e3)
usrp.set_rx_freq(2.4e9)
usrp.set_rx_antenna("TX/RX")
usrp.set_rx_gain(50)


# print(usrp.recv_num_samps(1000, 865e6, 2e6, [0], 50))


recv_buffer = np.zeros((1, 1000), dtype=np.complex64)

#start Streaming
metadata= uhd.types.RXMetadata()
streamer = usrp.get_rx_stream(uhd.usrp.StreamArgs("fc32", "sc16"))

var='0'
prev='0'
while True:
#START STREAM
    stream_cmd =uhd.types.StreamCMD(uhd.types.StreamMode.start_cont)
    stream_cmd.stream_now = True
    streamer.issue_stream_cmd(stream_cmd)

    num_samps=30000
#Receive Samples
    samples= np.zeros(num_samps, dtype=np.complex64)

    for i in range(num_samps//1000):
        streamer.recv(recv_buffer, metadata)
        samples[i*1000: (i+1)*1000]= recv_buffer[0]
    
    
    
#stop stream

    stream_cmd =uhd.types.StreamCMD(uhd.types.StreamMode.stop_cont)
    streamer.issue_stream_cmd(stream_cmd)

    # print(len(samples))


    # print(samples)


    sumsamp= np.sum(np.abs(samples))
    print(sumsamp)
    y_pred = model.predict(pd.DataFrame([sumsamp]))

    print(y_pred[0])
    
    # if (sumsamp<6000):
    #     var = '1'
    # elif(sumsamp<8500 and sumsamp>6000):
    #     var = '0'
    var =str(y_pred[0])
    if(var=='0'):
        var=prev
    if(var=='2'):
        var='0'
    
    prev=var

#ARDUINO

    command = var
    arduino.write(command.encode('utf-8')) 
    time.sleep(1)