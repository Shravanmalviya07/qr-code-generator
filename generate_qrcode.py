import qrcode
from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L

qr = QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("put your webside link here")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("custom_qrcode.png")

print("Custom QR Code Generated!")
