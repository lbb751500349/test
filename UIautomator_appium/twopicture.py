# coding=utf-8

from PIL import Image

data = Image.open('/Users/didi/Documents/must.png')
imgry = data.convert('L')
out = imgry.convert('1')
out.save('/Users/didi/Documents/test/123456.png')
out.show()


# import sys
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# try:
#     from pyocr import pyocr
#     from PIL import Image
# except ImportError:
#     raise SystemExit
# #导入库
# tools = pyocr.get_available_tools()[:]
# if len(tools) == 0:
#     print("No OCR tool found")
#     sys.exit(1)
# #查找OCR引擎
# print ("Using '%s'" % (tools[0].get_name()))
# print (tools[0].image_to_string(Image.open('/Users/didi/Documents/zoom/zhentxyzm1.png'),lang='eng'))
# lang='chi_sim'为OCR的识别语言库。C:\Program Files (x86)\Tesseract-OCR\tessdata



# import pyocr
# from PIL import Image
# img = Image.open('/Users/didi/Downloads/33.png')
# print(pyocr.iimage_to_string(img))
#
# img = img.convert('L')
# img.save('/Users/didi/Downloads/4.png')
# print(image_to_string(img))
#
# from PIL import Image
# import time
#
# def curr_time():
#     time_chuo = time.localtime(time.time())
#     zhuanhuan_time = time.strftime('%Y-%m-%d %H:%M.%S',time_chuo)
#     return zhuanhuan_time
#
# def pIx(picture):
#     data = Image.open(picture)
#     # 图片的长宽
#     data.size
#
#     w = (data.size)[0]
#     h = (data.size)[1]
#
#     zuobiao=[]
#     hengxian = []
#
#     # data.getpixel((x,y))获取目标像素点颜色。
#     # data.putpixel((x,y),255)更改像素点颜色，255代表颜色。
#     print('start:%s'%curr_time())
#     # z = 0
#     try:
#         for x in range(1, w - 1):
#             if x > 1 and x != w - 2:
#                 # 获取目标像素点左右位置
#                 left = x - 1
#                 right = x + 1
#             for y in range(1, h - 1):
#                 # 获取目标像素点上下位置
#                 up = y - 1
#                 down = y + 1
#                 if x <= 2 or x >= (w - 2):
#                     data.putpixel((x, y), 255)
#                 elif y <= 2 or y >= (h - 2):
#                     data.putpixel((x, y), 255)
#                 elif data.getpixel((x, y)) == 0:
#                     if y > 1 and y != h - 1:
#
#                         # 以目标像素点为中心点，获取周围像素点颜色
#                         # 0为黑色，255为白色
#                         up_color = data.getpixel((x, up))
#                         down_color = data.getpixel((x, down))
#                         left_color = data.getpixel((left, y))
#                         left_down_color = data.getpixel((left, down))
#                         right_color = data.getpixel((right, y))
#                         right_up_color = data.getpixel((right, up))
#                         right_down_color = data.getpixel((right, down))
#                         #add left_up_color
#                         left_up_color = data.getpixel((left,up))
#
#                         # if cuurent_color == 0:
#
#                         # if up_color == 0 or right_color == 0 or down_color == 0 or left_color ==0 or \
#                         #         right_up_color == 0 or left_down_color == 0 or left_down_color == 0 or \
#                         #         right_down_color == 0:
#                         #
#                         #     zuobiao = [x,y]
#                         #     hengxian.append(zuobiao)
#                         # 去除竖线干扰线
#                         if down_color == 0:
#                             if left_color == 255 and left_down_color == 255 and \
#                                     right_color == 255 and right_down_color == 255:
#                                 data.putpixel((x, y), 255)
#                 #
#                 #         # 去除横线干扰线
#                 #         elif right_color == 0:
#                 #             if down_color == 255 and right_down_color == 255 and \
#                 #                     up_color == 255 and right_up_color == 255:
#                 #                 data.putpixel((x, y), 255)
#                 #
#                 #     # 去除斜线干扰线
#                 #     if left_color == 255 and right_color == 255 \
#                 #             and up_color == 255 and down_color == 255:
#                 #         data.putpixel((x, y), 255)
#                 # else:
#                 #     pass
#                 data.save("/Users/didi/Documents/test/test.png")
#                 # print(1)
#
#     except:
#         return False
#
#     # print(len(hengxian))
#     # if len(hengxian) > 1000:
#     #     print('1111')
#     #     for zb in range(len(hengxian)):
#     #         print('222222')
#     #         print(hengxian[zb][0], hengxian[zb][1])
#     #         data.putpixel((hengxian[zb][0], hengxian[zb][1]), 255)
#     #         # 保存去除干扰线后的图片
#     #         data.save("/Users/didi/Documents/test/test.png")
#     #     print('end:%s' % curr_time())
#
# pIx('/Users/didi/Documents/test/zhentxyzm1.png')

