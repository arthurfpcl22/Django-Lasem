from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.groupname='dashboard'
		await self.channel_layer.group_add(
			self.groupname,
			self.channel_name,
		)
		
		await self.accept()
		
	async def disconnect(self,close_code):
		pass
	async def receive(self,text_data):
		Valor1=float(json.loads(text_data[0:5]))
		Valor2=float(json.loads(text_data[5:10]))
		#val=datapoint['value']
		
		await self.channel_layer.group_send(
			self.groupname,
			{
				'type':'deprocessing',
				'Valor1':Valor1,
				'Valor2':Valor2
				
			}
		)
		
		print('Temperatura',text_data[0:5])
		print('Umidade',text_data[5:10])
		#pass
	async def deprocessing(self,event):
		valOther=event['Valor1']
		valOther2=event['Valor2']
		
		await self.send(text_data=json.dumps({'value1':valOther,'value2':valOther2}))
