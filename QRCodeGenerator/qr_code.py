import os
import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.ERROR_CORRECT_H, 
    box_size=10, 
    border=10)

# Add the data to the QR code
qr.add_data("https://github.com/ampzn")
qr.make(fit=True)

# Generate the image with the specified colors
img = qr.make_image(fill_color="purple", back_color="black")

# Construct the absolute path to the img folder within the QRCodeGenerator directory
dir_path = os.path.dirname(os.path.realpath(__file__))
img_path = os.path.join(dir_path, "img", "ampzn_github.png")

# Save the image to the specified absolute path
img.save(img_path)
