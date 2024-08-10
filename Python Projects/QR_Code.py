import qrcode as qr

img = qr.make("https://images.unsplash.com/photo-1566024349847-9bb4b2deb743?q=80&w=465&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

img.save("car_image.png")