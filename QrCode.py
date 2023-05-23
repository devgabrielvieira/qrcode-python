import qrcode

meu_qrcode = qrcode.make(
    "https://www.instagram.com/devgabrielvieira/"
)

meu_qrcode.save("qrcode.png")

meu_qrcode.show()