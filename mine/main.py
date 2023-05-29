#the requests module helps us make requests from the HTTP
import requests
import json

api_key = '7ab4676347798fbf76da191adbd020c8'

city_list = ['Lagos', 'Ibadan', 'Abuja', 'Port Harcourt', 'Warri']
# city = input('Enter city name: ')
height = [300, 430, 555, 690, 825]


from PIL import Image, ImageFont, ImageDraw
from datetime import date

image = Image.open("post.png")
draw = ImageDraw.Draw(image)

#for adding the heading text to the image.
font = ImageFont.truetype("Inter-Medium.ttf", size=50)
content = "Latest Weather Forecast!"
color = "rgb(255, 255, 255)" 
(x, y) = (45, 55)
draw.text((x, y), content, color, font=font)


#for adding the date of the forecast
font = ImageFont.truetype("Inter-Medium.ttf", size=30)
today = date.today()
content = date.today().strftime("%A - %B %m %Y")
color = "rgb(255, 255, 255)" 
(x, y) = (45, 145)
draw.text((x, y), content, color, font=font)

index = 0
for city in city_list:
    apikeyURL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7ab4676347798fbf76da191adbd020c8&units=metric'
    response = requests.get(apikeyURL)
    data = json.loads(response.text)

    font = ImageFont.truetype("Inter-Medium.ttf", size=50)
    color = "rgb(0, 0, 0)" 
    (x, y) = (130, height[index])
    draw.text((x, y), city, color, font=font)

    font = ImageFont.truetype("Inter-Medium.ttf", size=40)
    content = str(data['main']['temp']) + chr(176) + "C"
    color = "rgb(255, 255, 255)" 
    (x, y) = (600, height[index])
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype("Inter-Medium.ttf", size=40)
    content = str(data['main']['humidity']) + '%'
    color = "rgb(255, 255, 255)" 
    (x, y) = (800, height[index])
    draw.text((x, y), content, color, font=font)

    index += 1


image.show()
image.save("test.png")
print("it is working")