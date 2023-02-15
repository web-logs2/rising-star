import sys
import pygame

pygame.init()
pygame.display.set_caption('Flying Bird')  # 设置窗口名字
width, height = 700, 500
screen = pygame.display.set_mode((width, height))  # 设置窗口大小
bg = pygame.image.load("img/bg_day.png")  # 加载背景图片
font = pygame.font.SysFont("Arial", 36)  # 设置字体字号和大小
score = 0  # 设置初始分数
while True:
    screen.blit(bg, (0, 0))  # 加载背景图片
    for event in pygame.event.get():  # 检测时间，如果鼠标点击叉号，就退出
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(font.render('Score : ' + str(score), True, (255, 255, 255)), (0, 0))  # 加载字体
    pygame.display.flip()  # 更新
