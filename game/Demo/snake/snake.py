import pygame
import random
import sys
import time
from pygame.locals import *


class Snake:
    def __init__(self):
        """初始化方法"""
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.playSurface = pygame.display.set_mode((640, 480))  # 设置界面
        pygame.display.set_caption("贪吃蛇游戏")  # 设置标题
        self.redColor = pygame.Color(255, 0, 0)  # 红色 方块
        self.blackColor = pygame.Color(0, 0, 0)  # 背景颜色黑色
        self.whiteColor = pygame.Color(255, 255, 255)  # 蛇本体颜色白色
        self.greyColor = pygame.Color(150, 150, 150)  # 游戏结束文字显示
        self.snakePosition = [100, 100]  # 蛇头坐标
        self.snakeSegments = [[100, 100], [80, 100], [60, 100]]  # 蛇身体
        self.foodPosition = [300, 300]  # 食物坐标   食物是 20*20 小方块
        self.food = 1  # 有1个食物
        self.direction = 'right'  # 默认方向
        self.changeDirection = self.direction  # 记录改变的方向

    def gameOver(self):
        self.gameOverFont = pygame.font.SysFont('simfang.ttf', 72)
        self.gameOverSurf = self.gameOverFont.render('Game Over', True, self.greyColor)
        self.playSurface.blit(self.gameOverSurf, [200, 10])
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()

    def keyPressEvent(self, event):
        """键盘事件"""
        if event.key == K_RIGHT or event.key == K_d:
            self.changeDirection = 'right'
        if event.key == K_LEFT or event.key == K_a:
            self.changeDirection = 'left'
        if event.key == K_UP or event.key == K_w:
            self.changeDirection = 'up'
        if event.key == K_DOWN or event.key == K_s:
            self.changeDirection = 'down'

    def move(self):
        """确定键盘 移动事件"""
        if self.changeDirection == 'right' and self.direction != 'left':  # 因为蛇不能直接掉头 所以向左时候不能直接右
            self.direction = self.changeDirection
        if self.changeDirection == 'left' and self.direction != 'right':
            self.direction = self.changeDirection
        if self.changeDirection == 'up' and self.direction != 'down':
            self.direction = self.changeDirection
        if self.changeDirection == 'down' and self.direction != 'up':
            self.direction = self.changeDirection
        if self.direction == 'right':
            self.snakePosition[0] += 20
        if self.direction == 'left':
            self.snakePosition[0] -= 20
        if self.direction == 'up':
            self.snakePosition[1] -= 20
        if self.direction == 'down':
            self.snakePosition[1] += 20

    def playMusic(self):
        """ 播放音乐"""
        music = pygame.mixer.music
        music.load("success.mp3")
        music.play()

    def main(self):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:  # 如果是键盘事件，调用keyPressEvent(event)方法
                    self.keyPressEvent(event)

            self.move()
            self.snakeSegments.insert(0, list(self.snakePosition))
            if self.snakePosition[0] == self.foodPosition[0] and self.snakePosition[1] == self.foodPosition[1]:
                self.playMusic()
                self.food = 0

            else:
                self.snakeSegments.pop()
            if self.food == 0:
                while True:
                    x = random.randint(1, 31)
                    y = random.randint(1, 23)
                    self.foodPosition = [int(x * 20), int(y * 20)]
                    if self.foodPosition not in self.snakeSegments:
                        break
            self.food = 1

            self.playSurface.fill(self.blackColor)

            for position in self.snakeSegments:
                pygame.draw.rect(self.playSurface, self.whiteColor, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(self.playSurface, self.redColor,
                             Rect(self.foodPosition[0], self.foodPosition[1], 20, 20))  # 界面添加 食物

            if self.snakePosition[0] > 620 or self.snakePosition[0] < 0:
                self.gameOver()
            if self.snakePosition[1] > 460 or self.snakePosition[1] < 0:
                self.gameOver()
            if self.snakePosition in self.snakeSegments[1:]:
                self.gameOver()

            pygame.display.update()

            self.fpsClock.tick(3)


if __name__ == '__main__':
    game = Snake()
    game.main()
