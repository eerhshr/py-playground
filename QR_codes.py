import segno


def scan():
    qrcode = segno.make_qr('Hello World')
    qrcode.save(
        "basic_qrcode.png",
        scale=5,
    )
