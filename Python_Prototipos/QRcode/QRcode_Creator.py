import qrcode
from PIL import Image

#Inserindo o dado que sera gerado o QRcode
dadoo = input("Insira o dado no qual sera gerado o QRcode: ")
#Gerando o QRcode
Codigo_QR = qrcode.QRCode(version=2, box_size=10, border=5)
Codigo_QR.add_data(dadoo)
Codigo_QR.make(fit=True)
#criando uma imagem do QRcode
image = Codigo_QR.make_image(fill="black", back_color="white")
#Salvando a imagem
image.save("qr_code.png")
Image.open("qr_code.png")