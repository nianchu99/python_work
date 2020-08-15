from PIL import Image

cat = Image.open('cat.jpg')

size = cat.size

print(size)

width, height = cat.size
print(str(width) + "  " +  str(height))
print(cat.filename)
# 描述了原始文件的图像格式，返回字符串
print(cat.format)
print(cat.format_description)
cat.save('cat.png')

im = Image.new('RGBA', (100,200), 'green')
im.save('greenImage.png')
im2 = Image.new('RGB', (20,20))
im2.save('transParentImage.png')

# 裁剪图片
croppedCat = cat.crop((335, 345, 565, 560))
croppedCat.save('croppedCat.png')
