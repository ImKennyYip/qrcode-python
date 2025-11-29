import qrcode

# url = "kennyyipcoding.com"
url = input("Enter a URL: ").strip() #removes leading/trailing whitespaces
image_file = "./qrcode.png"

img = qrcode.make(url)
img.save(image_file)


qr = qrcode.QRCode()
qr.add_data(url)
# image = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img = qr.make_image()
img.save(image_file)