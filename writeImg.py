from PIL import Image, ImageDraw, ImageFont

image = Image.open('image/3.png')
message = "Happy Birthday!"
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Bold.ttf', size=200)
(x, y) = (70, 30)
color = 'rgb(0, 0, 0)'
draw.text((x, y), message, fill=color, font=font)

messages = "Happy Birthday!"
(x, y) = (100, 900)
color = 'rgb(0, 0, 0)'
draw.text((x, y), messages, fill=color, font=font)
image.save('greeting_card.png')