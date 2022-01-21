import serial
import json
import requests
import websocket
import time
ws=websocket.WebSocket()
ws.connect('ws://192.168.1.141:8000/ws/teste/')
ser=serial.Serial('COM3',baudrate=9600,timeout=3.5)
arduinoData=[]
i=0
while 1:
	arduinoData.append(ser.readline().decode('utf-8'))
	if len(arduinoData)<2:
		pass
	else:
		time.sleep(3)
	
		ws.send(json.dumps({'value':float(arduinoData[i])}))
	i+=1
