import pygame
from sys import exit
import random
# 窗口大小
WIDTH = 800
HEIGHT = 600


# 定义蛇类
class Snake(object):
    def __init__(self):
        self.direction = pygame.K_LEFT
        self.body = []
        for x in range(5):  # 初始化蛇的长度
            self.addnode()

    # 增加块
    def addnode(self):
        left, top = (360, 360)
        if self.body:
            left, top = (self.body[0].left, self.body[0].top)
        node = pygame.Rect(left, top, 20, 20)  # left top width height
        if self.direction == pygame.K_LEFT:
            node.left -= 20
        elif self.direction == pygame.K_RIGHT:
            node.left += 20
        elif self.direction == pygame.K_UP:
            node.top -= 20
        elif self.direction == pygame.K_DOWN:
            node.top += 20
        self.body.insert(0, node)  # 头插入

    # 删除块
    def delnode(self):
        self.body.pop()

    # 游戏结束判断 撞墙 撞自己
    def ifdead(self):
        if self.body[0].x not in range(WIDTH):
            return True
        if self.body[0].y not in range(HEIGHT):
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False

    # 贪吃蛇移动
    def move(self):
        self.addnode()
        self.delnode()

    # 改变方向
    def changedirection(self, Dir):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if Dir in LR+UD:
            # 同方向不变
            if(Dir in LR) and (self.direction in LR):
                return
            if(Dir in UD) and (self.direction in UD):
                return
            self.direction = Dir


# 食物类
class Food:
    def __init__(self):
        self.rect = pygame.Rect(-20, 0, 20, 20)

    # 移除块
    def remove(self):
        self.rect.x = -20

    # 创建块
    def set(self):
        if self.rect.x == -20:
            W = []
            H = []
            for pos1 in range(20, WIDTH-20, 20):  # 不在边缘出现
                W.append(pos1)
            for pos2 in range(20, HEIGHT-20, 20):
                H.append(pos2)
            self.rect.left = random.choice(W)
            self.rect.top = random.choice(H)


# 绘制文字
def show_text(screen, pos, text, color, font_size=60):
    cur_font = pygame.font.SysFont("宋体", font_size)
    text_fmt = cur_font.render(text, 1, color)
    screen.blit(text_fmt, pos)


def main():
    # 音乐初始化
    pygame.mixer.pre_init(44100, 16, 1, 4096)
    # pygame 初始化
    pygame.init()
    pygame.mixer.set_num_channels(8)
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    # 音乐导入
    gamesound = pygame.mixer.Sound("b.ogg")
    gamesound.set_volume(1.0)
    diesound = pygame.mixer.Sound("a.ogg")
    diesound.set_volume(1.0)
    pygame.display.set_caption('贪吃蛇')
    clock = pygame.time.Clock()
    scores = 0
    ifdead = False
    snake = Snake()
    food = Food()
    # 游戏音乐循环播放
    gamesound.play(-1)
    isplay = False

    def diesoundon(a):  # 死亡音乐
        if a is True:
            return
        else:
            diesound.play(-1)

    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                snake.changedirection(event.key)
                if event.key == pygame.K_SPACE and ifdead:
                    diesound.stop()
                    return main()

        if not ifdead:
            snake.move()

        # 画蛇
        for rect in snake.body:
            pygame.draw.rect(screen, (255, 20, 147), rect, 0)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

        ifdead = snake.ifdead()
        length = len(snake.body)
        # 胜利（不可能的）
        if length == (WIDTH/20)*(HEIGHT/20):
            show_text(screen, (200, 200), 'YOU WIN', (227, 29, 18), 125)
        if food.rect == snake.body[0]:
            scores += 1
            food.remove()
            snake.addnode()
        if ifdead:
            show_text(screen, (130, 200), 'GAME OVER', (227, 29, 18), 125)
            show_text(screen, (230, 280), 'please press space to try again...', (0, 0, 22), 30)
            gamesound.stop()
            diesoundon(isplay)
            isplay = True
        food.set()
        # 防止出现在身体里
        while food.rect in snake.body:
            food.remove()
            food.set()
        # 画食物
        pygame.draw.rect(screen, (0, 255, 0), food.rect, 0)
        show_text(screen, (680, 20), 'Scores:', (0, 0, 0), 30)
        show_text(screen, (760, 20), str(scores), (255, 0, 0), 30)
        pygame.display.update()
        # 游戏速度
        clock.tick(12)


if __name__ == '__main__':
    main()