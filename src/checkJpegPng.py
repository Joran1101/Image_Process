import os

path = './dataset/text/'

def is_valid_jpg(jpg_file):
    with open(jpg_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        return buf ==  b'\xff\xd9'

def is_valid_png(png_file):
    with open(png_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        return buf == b'\x60\x82'

if __name__=="__main__":
    for file in os.listdir('./dataset/text'):
        pic_file = path + file
        isJpg = is_valid_jpg(pic_file)
        isPng = is_valid_png(pic_file)

        print("jpeg : %s, png %s, file %s " % (isJpg, isPng, file))
