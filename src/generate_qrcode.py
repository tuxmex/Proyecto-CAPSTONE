import qrcode
from PIL import Image
import sys
import getopt


def main(argv):
    code = ''
    try:
      opts, args = getopt.getopt(argv, "c:", ["codigo="])
    except getopt.GetoptError:
      print('qrcode.py -c <codigo_ a_generar> ')
      sys.exit(2)

    
    if opts is None or len(opts) == 0:
        print('qrcode.py -c <codigo_ a_generar> ')
        sys.exit(2)

    for opt, arg in opts:
      if opt in ("-c", "--codigo"):
         code = arg

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    print(code)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save("/home/gbarron/capstone/src/qrcodes/qrcode.png")

if __name__ == "__main__":
   main(sys.argv[1:])