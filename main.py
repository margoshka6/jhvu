from PIL import Image
from PIL import ImageFilter
with Image.open("2345-1000x830.jpg") as pic_original:
    print("розмір",pic_original.size)
    print("формат", pic_original.format)
    print("тип",pic_original.mode)
    pic_original.show()

    pic_bw = pic_original.convert("L")
    pic_bw.save("bw.jpg")
    pic_bw.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up.jpg")
    pic_up.show()

    pic_rotated = pic_original.rotate(30,expand=True)
    pic_rotated.save("rotated.jpg")
    pic_rotated.show()