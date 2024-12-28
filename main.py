from PIL import Image, ImageDraw, ImageFont
print('Генератор мемов запущен!')
top_text=input('Вверхний текст: ')
bottom_text=input('Нижний текст: ')
print(top_text, bottom_text)
print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
image_number = int(input('Номер картинки: '))
if image_number==1:
    image_file='Кот в ресторане.png'
else:
    image_file="Кот в очках.png"
print(image_file)
image=Image.open(image_file)
draw=ImageDraw.Draw(image)
font=ImageFont.truetype('impact.ttf', size=72)

width, height=image.size

draw.text((width // 2, 10), top_text, fill='white', font=font, anchor='mt', stroke_width=3, stroke_fill='black')
draw.text((width // 2, height-10), bottom_text, fill='white', font=font, anchor='mb', stroke_width=3, stroke_fill='black')

image.save('meme.png')