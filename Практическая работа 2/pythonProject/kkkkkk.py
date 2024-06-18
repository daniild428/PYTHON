from PIL import Image, ImageDraw



img = Image.new('RGB', (400, 400), color = 'white')
draw = ImageDraw.Draw(img)





draw.polygon([(50, 150), (200, 100), (350, 150)], fill='brown') # основание домика
draw.polygon([(50, 150), (200, 100), (350, 150)], outline='black') # крыша
draw.rectangle([(100, 150), (300, 300)], fill='white', outline='black') # дверь
draw.rectangle([(150, 200), (200, 250)], fill='blue', outline='black') # окно



# draw.ellipse([(150, 200), (200, 250)], fill='gray', outline='black') # тело
# draw.ellipse([(160, 220), (180, 240)], fill='white', outline='black') # лицо
# draw.line([(150, 200), (170, 190)], fill='black', width=2) # уши
# draw.line([(200, 200), (180, 190)], fill='black', width=2) # уши
# draw.line([(160, 210), (140, 230)], fill='black', width=1) # хвост
#
#
# draw.polygon([(50, 300), (200, 200), (350, 300)], fill='brown') # корпус
# draw.rectangle([(100, 200), (150, 250)], fill='white', outline='black') # парус
# draw.line([(125, 200), (125, 250)], fill='black', width=2) # мачта

img.save('name.png')