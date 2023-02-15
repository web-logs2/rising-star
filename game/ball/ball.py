import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))  # 设置窗口
ball = pygame.image.load("mouse.gif")  # 导入小球图片，图片的路径请自行修改。
ballrect = ball.get_rect()  # 通过get_rect()这个函数就可以获取图片的位置
print(ballrect)  # 这里可以通过输出来看一下图片的所在位置
print(ballrect.right)  # 图片右下角x轴坐标  bottom是图片右下角y轴坐标   同理left和top就是左上角的x,y坐标
seppn = [1, 1]  # x轴和y轴的位置
color = (0, 0, 0)  # 设置颜色
while True:  # 主循环
    screen.fill(color)  # 每次在while循环更新的时候我们重画背景，这样会覆盖上次小球移动的痕迹
    for event in pygame.event.get():  # 添加检查事件
        if event.type == pygame.QUIT:  # 退出事件，当鼠标点击退出按钮时退出程序
            sys.exit()
    ballrect = ballrect.move(seppn)  # 向x轴和y轴移动
    if ballrect.left < 0 or ballrect.right > 600:  # 碰撞检查
        seppn[0] = -seppn[0]  # 取反
    if ballrect.top < 0 or ballrect.bottom > 400:
        seppn[1] = -seppn[1]  # 取反
    screen.blit(ball, ballrect)  # 将ball和ballrect 显示在窗口中
    screen.blit(pygame.font.SysFont("MicrosoftYaHei", 16).render(str(ballrect), True, "red"), (0, 0))
    screen.blit(pygame.font.SysFont("MicrosoftYaHei", 16).render(str(ballrect.right), True, "red"), (0, 8))
    pygame.display.flip()  # 显示窗口的内容
