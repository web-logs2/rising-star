import pygame
import sys
import random

# 一定要配合 https://www.pygame.org/docs/ 文档看各种方法的介绍

background_image = 'background.jpg'
mouse_image = 'mouse.gif'
pygame.init()  # 初始化
pygame.display.set_caption("Hello Pygame")  # 设置窗口标题
screen = pygame.display.set_mode((1200, 848), 0, 32)  # set_mode: 返回一个 Surface 对象，代表了桌面上出现的窗口。第一个参数代表分辨率；第二个参数是标志位，如果不需要使用热河特性，则指定为 0；第三个为色深。
background = pygame.image.load(background_image).convert()  # convert: 将图像转化为 Surface 对象,每次加载完图像后就要使用这个函数
# convert具体解释： 若想将图片更快速地加载出来,可以使用convert()指令，虽然显示结果与不加convert()指令一致,但是使用convert可以转换格式, 提高blit的速度。通俗得地讲,如果想在blit之外获得速度,那就需要 convert().
# convert()所指的“格式”并非指文件格式工(如png.jpeg, gif),它是所谓的“像素格式”。 它代表了一个surface记录一个特定像素的颜色的方法。如果surface格式跟显示格式不一样,那 SDL就要在每次blit的时候去转化——这是个相当费时的过程
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()  # convert_alpha: 相比convert，保留了Alpha通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。可以试试不用convert_alpha的效果。
while True:
    for event in pygame.event.get():  # get() 拿到所有事件的列表
        if event.type == pygame.QUIT: pygame.quit();sys.exit()  # 如果是退出事件(点击窗口的关闭按钮) 就关闭退出程序
    screen.blit(background, (0, 0))  # 画上背景图 blit: 第一个参数为一个 Surface 对象，第二个为左上角位置坐标。画完以后得用 update 更新，否则画面一片漆黑
    x, y = pygame.mouse.get_pos()  # 获得鼠标位置坐标
    # 计算光标图片左上角位置的坐标
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor, (x, y))  # 画上光标  第二个参数为左上角位置坐标
    # 刷新画面
    pygame.display.update()

'''
上面的程序，一直运行直到关闭窗口而产生了一个 QUIT 事件，Pygame 会接受用户的各种操作（比如按键盘，移动鼠标等）产生事件。事件随时可能发生，而且量也可能会很大，Pygame 的做法是把一系列的事件存放一个队列里，逐个的处理
上面使用了 pygame.event.get() 来处理所有的事件；也可以使用 pygame.event.wait()，pygame 会等到发生一个时间才继续下去；另外一个方法 pygame.event.poll()，一旦调用，它会根据现在的情形返回一个真实的事件，或者一个 “什么都没有”
接下来我们写一个把发生的事件输出的程序
'''

# pygame.init()
# SCREEN_SIZE = (640, 480)
# screen = pygame.display.set_mode(SCREEN_SIZE, 0, 0)
# font = pygame.font.SysFont("MicrosoftYaHei", 16)  # 从系统字体创建一个 Font对象  SysFont（名称，大小，粗体=False，斜体=False）-> Font
# font_height = font.get_linesize()  # 获取默认行距  本例子 之前输出看了下是12
# while True:
#     event = pygame.event.wait()  # 从队列中返回单个事件。如果队列为空，此函数将等待直到有事件
#     if event.type == pygame.QUIT:sys.exit()
#     screen.fill((255, 255, 255))  # 用纯色填充表面 fill(color, rect=None, special_flags=0) -> Rect   这里使用了rgb(255, 255, 255)   Rect是用于存储坐标的对象，之后再深入演示
#     screen.blit(font.render(str(event), True, "purple", "green"), (0, font_height))  # render方法第一个参数是Surface 第二个是抗锯齿开关 第三个是字体颜色 第四个是字体背景(不填默认透明)  blit参数同上，这里x轴为0 紧贴左边，然后y轴距顶部空出一个行距后绘制font的Surface
#     # Font.render()将创建一个此Font的 Surface，并在其上呈现Font。 pygame.font是用于加载和渲染字体的，无法直接在现有 Surface 上绘制文本 所以必须使用Font.render()创建文本的可视化（Surface），然后将该图像 blit 到另一个 Surface 上
#     screen.blit(font.render(str(event), True, "red"), (0, 50))
#     screen.blit(font.render(str(event), True, "black"), (50, 59))  # 看起来字体实际大小应该是9  可能surface还包含上下一点空间吧
#     pygame.display.update()

'''
字体飘动
'''
# pygame.init()
# screen = pygame.display.set_mode((1200, 848), 0, 32)
# background_image = 'background.jpg'
# background = pygame.image.load(background_image).convert()
# print(pygame.font.get_fonts())  # 看下都有哪些字体可选
# font = pygame.font.SysFont("songti", 40)
# text_surface = font.render("你好", True, (255, 0, 255))
# x = 0
# y = (screen.get_height() - text_surface.get_height()) / 2
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     screen.blit(background, (0, 0))
#     x -= 1
#     if x < -text_surface.get_width():
#         x = screen.get_width() - text_surface.get_width()
#     screen.blit(text_surface, (x, y))
#     pygame.display.update()

'''
图像移动
'''
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
# background = pygame.image.load('background.jpg').convert()
# mouse_cursor = pygame.image.load("mouse.gif").convert_alpha()
# move_x, move_y = 0, 0
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: exit()
#         if event.type == pygame.KEYDOWN:
#             # 键盘有按下？
#             if event.key == pygame.K_LEFT:
#                 # 按下的是左方向键的话，把x坐标减一
#                 move_x -= 3
#             elif event.key == pygame.K_RIGHT:
#                 # 右方向键则加一
#                 move_x += 3
#             elif event.key == pygame.K_UP:
#                 # 类似了
#                 move_y -=3
#             elif event.key == pygame.K_DOWN:
#                 move_y += 3
#         elif event.type == pygame.KEYUP:
#             # 如果用户放开了键盘，什么都不做
#             pass
#         screen.blit(background, (0, 0))
#         screen.blit(mouse_cursor, (move_x, move_y))
#         # 在新的位置上画图
#         pygame.display.update()

'''
图像持续移动
'''
# pygame.init()
# screen = pygame.display.set_mode((640, 480), 0, 32)
# background = pygame.image.load('background.jpg').convert()
# mouse_cursor = pygame.image.load("mouse.gif").convert_alpha()
# clock = pygame.time.Clock()
# move_x, move_y = 0, 0
# while True:
#     clock.tick(60)  # 每秒60帧
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: exit()
#     a = pygame.key.get_pressed()  # 获取所有键盘按钮的状态 返回一个布尔值序列，表示键盘上每个键的状态 被按下是true
#     # 键盘有按下？
#     if a[pygame.K_LEFT]:
#         # 按下的是左方向键的话，把x坐标减一
#         move_x -= 3
#     if a[pygame.K_RIGHT]:
#         # 右方向键则加一
#         move_x += 3
#     if a[pygame.K_UP]:
#         # 类似了
#         move_y -= 3
#     if a[pygame.K_DOWN]:
#         move_y += 3
#     screen.blit(background, (0, 0))
#     screen.blit(mouse_cursor, (move_x, move_y))
#     # 在新的位置上画图
#     pygame.display.update()

'''
多张图像移动
'''
# pygame.init()
#
#
# class Money():
#     def __init__(self, img_file):
#         self.x = random.randint(10, 700)
#         self.y = random.randint(0, 20)
#         self.image = pygame.image.load(img_file)
#
#     def move(self):  # 斜着移动的
#         if self.y > 480: self.y = -50
#         else:
#             self.y += 1
#         screen.blit(self.image, [self.x, self.y])
#
#
# screen = pygame.display.set_mode((854, 480))  # 窗口大小
# img_list = ["1.png", "2.png", "3.png"]
# img_list2 = ["4.png", "5.png", "6.png", "7.png"]
# background = pygame.image.load("background.jpg")
# # 创建空列表，储存对象
# w = []
# for i in range(4):  # 插入4张图片 并且限制部分图片的频率
#     if random.random() >= 0.8:
#         img_file = random.choice(img_list2)
#     else:
#         img_file = random.choice(img_list)
#     a = Money(img_file)
#     w.append(a)
#
# while True:
#     screen.blit(background, [0, 0])
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#     for i in w:
#         i.move()
#     my_rect = pygame.Rect(50, 100, 100, 200)  # 50，100为矩形框左上角坐标，100，200为矩形框的宽和高  这一步是定义矩形Surface
#     pygame.draw.rect(screen, [0, 234, 45], my_rect, 2)  # 窗口中画上刚刚定义的矩形Surface；第一个参数为要绘制在哪；第二个为rgb颜色，用列表表示；要画的对象；2为矩形框粗细（可省）
#     pygame.display.flip()  # 和update的区别去官网看

'''
使用rect为载体加载图片
'''
# pygame.init()
# screen = pygame.display.set_mode((854, 480))  # 窗口大小
# background = pygame.image.load("background.jpg")
# img = pygame.image.load("6.png")  # 加载图片
# img_rect = img.get_rect()  # 获取图片的边框，并创建一个矩形对象
# print(img_rect.top)  # 图片左上角y轴坐标
# print(img_rect.left)  # 图片左上角x轴坐标
# print(img_rect.bottom)  # 图片右下角y轴坐标
# print(img_rect.right)  # 图片右下角x轴坐标
# print(img_rect.width)  # 图片的宽度
# print(img_rect.height)  # 图片的高度
# print(img_rect.center)  # 图片中心点坐标
# print(img_rect.size)  # 图片大小
# while True:
#     screen.blit(background, (0, 0))
#     screen.blit(img, img_rect)  # 将图片移动到矩形框上
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#     img_rect.move_ip(1, 1)  # 让rect对象移动的指令
#     pygame.display.flip()
