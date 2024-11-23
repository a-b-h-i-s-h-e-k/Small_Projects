'''

Decoding a QR code means finding the value, number, text or link behind the QR 
code. There are many ways to decode a QR code used by your smartphone 
cameras, which helps you scan a QR code while making online payments.


To decode a QR code, you need an image of a QR code. 

For decoding QR codes using Python, you need to install two Python libraries in 
your Python environment; pyzbar and pillow. You can install both these libraries by 
executing the commands mentioned below in your command prompt or terminal:

    pip install pyzbar
    pip install pillow
   
    
'''

from pyzbar.pyzbar import decode
# Import the 'decode' function from the 'pyzbar.pyzbar' module. 
# This function is used to decode barcodes and QR codes from images.


from PIL import Image
# Import the 'Image' class from the 'PIL' (Pillow) module.
# Pillow is a Python Imaging Library that provides the ability to 
# create, modify, and save images.

decocdeQR = decode(Image.open('w3school.png'))
# 1. Open the image file 'w3school.png' using PIL's 'Image.open' method 
# and pass it to the 'decode' function.
# 2. The 'decode' function reads the image and scans for any barcodes or 
# QR codes present in the image.
# 3. The result is stored in the variable 'decocdeQR'. The result is a 
# list of objects, where each object represents a decoded barcode 
# or QR code.

print(decocdeQR[0].data.decode('ascii'))
# 1. Access the first decoded QR code/barcode in the 'decocdeQR' list using the index [0].
# 2. Each decoded object has a 'data' attribute which contains the encoded information 
# (like a URL or text).
# 3. Use the 'decode' method with the 'ascii' parameter to convert the binary data 
# into a readable string.
# 4. Finally, print the decoded string.




