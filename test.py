from Processor import ImageProcessor
from Image_Capture import load_image, show_image 

test=load_image(r"C:\Users\ASUS\Desktop\ATAKAN.jpeg")

#gray_img=ImageProcessor.turn_gray(test)

#show_image(gray_img,title="gri dönüşüm")

# binary_image=ImageProcessor.turn_binary(test)
# show_image(binary_image,title="Binary daaa")

# rotation_image=ImageProcessor.rotation_image(test)
# rotation_image=ImageProcessor.rotation_image(rotation_image)
# rotation_image=ImageProcessor.rotation_image(rotation_image)
# rotation_image=ImageProcessor.rotation_image(rotation_image)

# show_image(rotation_image,title="90 DERECE DÖNMÜŞ")

cropped_image=ImageProcessor.crop_image(test,100,150,100,50)
show_image(cropped_image,title="kırpma")




