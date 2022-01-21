from django.shortcuts import render
from .utils import get_geo
import folium
from requests import get
# Create your views here.
def home(request):
	return render(request,'S_Lasem/base.html')
def teste(request):
	return render(request,'S_Lasem/teste.html')
def bicicleta(request):
	ip=get('https://api.ipify.org').text
	country,city,lat,lon=get_geo(ip)
	l_lat=lat
	l_lon=lon
	pointA=[l_lat,l_lon]
	m=folium.Map(width=800,height=500,location=pointA,zoom_start=12)
	folium.Marker(location=[float(l_lat), float(l_lon)],                
                  popup=city).add_to(m)
	m=m._repr_html_()
	context={
		
		'map':m,
		
	}
	
	return render(request,'S_Lasem/bicicleta.html',context)
