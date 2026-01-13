import qrcode

sitio = input("Coloca la URL que quieras convertir a QR: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(sitio)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("heladoschela.png")

print("QR generado correctamente como <nombreDefotoResultante>.png")

