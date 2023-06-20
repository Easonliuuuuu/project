from quakefeeds import QuakeFeed
import folium
from datetime import datetime
from folium.features import DivIcon


feed = QuakeFeed("4.5", "day")

my_map = folium.Map(tiles='Stamen Terrain', zoom_start = 17)

for i in range(len(feed)):

	""" Convert the timestamp to UTC time """
	timestamp = round (feed[i]['properties']['time']/1000)
	dt_object = str(datetime.utcfromtimestamp(timestamp+28800))+' (UTC+8)'
	print(" 地點: ",feed.event_title(i)+ ' \n '+ "時間 "+dt_object + "\n",'[緯度,經度]',[feed.location(i)[1],feed.location(i)[0]],"\n",'震度:',feed.magnitude(i),"\n",'震源深度(KM):',feed.depth(i))

	""" Marks in terms of Pixels units """
	folium.CircleMarker(
	radius=1.5**feed.magnitude(i),
	location=[feed.location(i)[1],feed.location(i)[0]],
	popup=feed.event_title(i)+' at '+ dt_object,
	#color='#3186cc',
	color='#1abc9c',
	fill=True,
	).add_to(my_map)

	""" Marks in terms of Meters units"""
	folium.Circle(
	radius=feed.magnitude(i),
	location=[feed.location(i)[1],feed.location(i)[0]],
	popup=feed.event_title(i)+' at '+ dt_object,
	color='#3186cc',
	fill=False,
	).add_to(my_map)

	""" Add some text to the marker """
	tooltip = feed.event_title(i)+' at '+ dt_object

	if (feed.magnitude(i))>5:
		color='red'
	else:
		color='green'

	
		
	""" A balloon marker """	
	folium.Marker([feed.location(i)[1],feed.location(i)[0]] ,
	popup=feed.event_title(i)+' at '+ dt_object,
	tooltip=tooltip,
	icon=folium.Icon(color=(color), icon='circle' )#icon='info-sign',prefix='fa',icon='circle'
	).add_to(my_map)

	""" Add text on the map """
	folium.map.Marker(
	[feed.location(i)[1],feed.location(i)[0]] ,
	icon=DivIcon(
		icon_size=(18,70),
		icon_anchor=(9,25),
		html='<div style="font-size: 10pt; color: white;">%s</div>' % float(feed.magnitude(i)),
		)
	).add_to(my_map)


""" Display the map """
my_map.save('index.html')

