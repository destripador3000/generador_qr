import qrcode
sitio = input("Coloca la url que quieras convertir a qr")
qr.add_data(sitio)
qr.make(fit=True)
img =qr.make_image(fill='black', back_color='white')
img.save('heladoschela.png')
