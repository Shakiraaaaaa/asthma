import qrcode

# URL of your locally hosted or uploaded video
video_url = "https://youtu.be/7G3eXI_DPn8?si=B_Vd8EXX2eyDdg9O"  # Replace with your video URL

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (number of boxes)
)

qr.add_data(video_url)  # Add the video URL to the QR code
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image
img.save("video_qr_code.png")

print("QR code generated and saved as 'video_qr_code.png'.")
