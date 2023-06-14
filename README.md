# machine-learning-and-wireless-communication
This project is based on Machine Learning and Wirless Communication. 
# AIM:
The aim of the project is to use wireless communication devices to act as a source of signal detection. The signal detection can be used to Home automation through different gestures.
# Tools and Technologies used:
Machine Learning, Keras, PySerial, SVM, Arduino, USRPs, SDR, Wireless Communication.
# The Project:
Two antennas are set-up, one acts as a source of transmitting signals and the other is used to acts as a receiving signals. Now, the idea is that when a person puts his/her hand and performs some kind of gestures.
Then there is change in the amplitude as well as frequency signals. Now this distortion and shifts can be used to define a gesture and use it as a characteristics to train a model which can make predictions in real time.
The USRPs can send any signal, we are only concerned about the changes and shift. After collecting the samples before hand, these samples can be used to characterise a gesture. In this project we have tried to 
do it for 3 gestures. The signal collection and training the model with the samples is not an easy job, Why?. Sening a signal from one source to the transmitter highly depends upon the surrounding as well as
the frequency at which the signals are being transmitted and also the frequency and the samples rates of the signal. And kind of disturbance in the surrounding may lead to a huge distortion as well as shifts in the 
signal parameters. Suggestion is to use a closed system where one can only use our hand the system always remains in some particluar state. Distance between the antennas is also a prime factor. 
After collecting the samples and training the model with the changes in the amplitude of the signal and shifts in frequency of the signals. Now the model will be used to make the prediciton in the real time to classify
the different gestures.
Next the task is how we can use the predicition in the real time and further use the made prediciton for home automation.
For making the prediciton in the real time you can use the real time sample collecting using python which can directly collect the samples from the USRPs. Next take those samples may be in a set of 30000 per sec and 
further use it make prediciton. 
For the home automation part in the real time what we did is we used an Arduino to control an LED. Next we connect the Arduino through a set of python codes and ran it. Hurrah! it finally worked. This shows how we
can use the wireless deveices which send signals and use their distortion as mean to control our home appliances. Although the project is not that good to put it on a large scale, yet the idea to do is cracked!!!!!
