import barcode


qr = barcode.Code39("hei po de",writer= barcode.writer.ImageWriter())
qr.save("123")