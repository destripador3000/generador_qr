import qrcode
sitio = 'https://www.google.com/maps/place/HELADOS+CHELA/@4.2663322,-75.9311091,15z/data=!4m6!3m5!1s0x8e384dff1641e395:0xa850caeedfaea541!8m2!3d4.2663322!4d-75.9311091!16s%2Fg%2F11r3tqtgv_?entry=ttu'

qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(sitio)
qr.make(fit=True)
img =qr.make_image(fill='black', back_color='white')
img.save('heladoschela.png')