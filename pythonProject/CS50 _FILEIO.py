#NEW THINGS
from PIL import Image
import sys
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")
#sort
rabbit = ["General Munchkins", "Old Carrot", "Mr. Rabbler"]
for rabbits in sorted(rabbit):
    print(f"hello, {rabbits}!")
 #37:48
 #MAKING GIFS
images = []
for arg in sys.argv[1:]:
         image = Image.open(arg)
         images.append(image)
images[0].save(
    "costumes.gif", save_all=True, loop = 0, append_images = [images[1]], duration = 200
)#works in vs i guess
