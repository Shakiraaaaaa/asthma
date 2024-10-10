import qrcode

# The URL you want to encode in the QR code
url = "https://shakiraaaaaa.github.io/asthma/"

# Generate QR code
qr = qrcode.make(url)

# Save the QR code as an image file
qr.save("asthma_qr_code.png")

print("QR code generated and saved as 'asthma_qr_code.png'")
