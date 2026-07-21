from PIL import Image
import sys
from PIL import ImageOps
if len(sys.argv) < 3 :
    sys.exit("Too few argument")
if len(sys.argv) > 3 :
    sys.exit("Too many argument")
if not sys.argv[1].lower().endswith(".jpg") and sys.argv[2].lower().endswith(".jpg") :
    sys.exit("FILE TYPE IS NOT SAME")
elif not sys.argv[1].lower().endswith(".jpeg") and sys.argv[2].lower().endswith(".jpeg") :
    sys.exit("FILE TYPE IS NOT SAME")
elif not sys.argv[1].lower().endswith(".png") and sys.argv[2].lower().endswith(".png") :
    sys.exit("FILE TYPE IS NOT SAME")
try:
    with Image.open(sys.argv[1],"r") as fahad_img , Image.open ("shirt.png","r") as shirt_img:
        fahad_img = ImageOps.fit(image=fahad_img,size=(600,600))
        # fahad_img = fahad_img.rotate(90)
        fahad_img.paste(shirt_img,shirt_img)
        fahad_img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File not Found!!!!")

