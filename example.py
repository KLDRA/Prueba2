import qrcode

# Datos para el código QR
data = "http://kldra.duckdns.org"

# Crear el código QR
qr = qrcode.make(data)

# Guardar la imagen del código QR
qr_path = "/mnt/data/kldra_qr_code.png"
qr.save(qr_path)

qr_path