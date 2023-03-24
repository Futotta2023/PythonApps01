from PIL import Image
Image.open('input.png').convert('RGB').save('output.jpg', quality=90)
