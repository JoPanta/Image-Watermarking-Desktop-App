from PIL import Image
import os


resize = (100, 100)
fhd = (1920, 1080)
# Open the base and overlay images
base_image = Image.open("thewitcher.jpg")
watermark = Image.open("png.png")

#resize wattermark and base_image
base_image.thumbnail(fhd)
watermark.thumbnail(resize)

# Convert the overlay image to RGBA mode
watermark = watermark.convert("RGBA")

# Define the position where the overlay image will be pasted
position = (1720, 950)

# Overlay the image over base image
base_image.paste(watermark, position, watermark)

# now do the same for all images in images folder, and save them to watermarked folder
#first covert them to fhd
folder_path = "./images"
output_folder_path = "./fhd images"

for image in os.listdir(folder_path):
    if image.endswith(".jpg"):
        image_path = os.path.join(folder_path, image)

        i = Image.open(image_path)
        fn, fext = os.path.splitext(image)

        i.thumbnail(fhd)
        output_path = os.path.join(output_folder_path, "{}_fhd{}".format(fn, fext))
        i.save(output_path)

#then watermark them
