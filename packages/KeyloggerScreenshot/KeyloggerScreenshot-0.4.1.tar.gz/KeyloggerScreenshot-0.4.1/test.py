from PIL import Image
import pyautogui as pg

image = Image.open('New_Image (1).png')
new_image = image.resize((1920, 1080))
new_image.save('New_Image (1).png')

x, y = new_image.size
print(x, y)
nx, ny = pg.size()
print(nx, ny)
