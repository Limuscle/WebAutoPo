# from selenium import webdriver
# from time import sleep
#
# #打开谷歌浏览器,并且赋值给变量d
# d = webdriver.Chrome()
# d.maximize_window()# 最大化窗口
#
#
# # 通过get() 打开一个网址
# d.get('https://www.baidu.com')
# sleep(5)
#
# # 关闭当前窗口
# d.close()
# # 关闭所有窗口，并且关闭驱动
# d.quit()


# for i in range(1, 10):
#     for y in range(1, i + 1):
#         msg = '{0}*{1}={2}'.format(i, y, i * y)
#         print(msg, end='\t')
#     print()

# a = [4, 3, 6, 2, 45, 1, 65, 35, 753, 11, 5]
# # 排序次数
# times = len(a) - 1
# while times > 0:
#     for i in range(times):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
#     times = times - 1
# print(a)

a = lambda x, y: x**y
print(a(10, 3))