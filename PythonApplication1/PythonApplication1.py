import sys
#print(sys.path)
sys.path.append('C:/Users/Admin/AppData/Roaming/Python/Python311/site-packages')
from PIL import Image
Image.open('input.png').convert('RGB').save('output.jpg', quality=90)