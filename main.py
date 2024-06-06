# OpenCV Python GestureGame Whack-A-Mole

import cv2
import cvzone
import math
import time
import numpy as np
import random
from cvzone.HandTrackingModule import HandDetector  # 导入手部检测模块

# 图片素材
background_image = cv2.imread('background_image.png') # 背景图片
background_image = cv2.resize(background_image, (1280, 720))  # 调整为1280x720像素

hammer_left = cv2.imread('hammer_left.png', cv2.IMREAD_UNCHANGED)  # 左锤图片
hammer_left = cv2.resize(hammer_left, (170, 170))  # 调整为170x170像素

hammer_right = cv2.imread('hammer_right.png', cv2.IMREAD_UNCHANGED)  # 右锤图片
hammer_right = cv2.resize(hammer_right, (170, 170))  # 调整为170x170像素

mouse = cv2.imread('mouse.png', cv2.IMREAD_UNCHANGED)  # 地鼠图片
mouse = cv2.resize(mouse, (109, 101))  # 调整为109x101像素

mouse_click = cv2.imread('mouse_click.png', cv2.IMREAD_UNCHANGED)  # 地鼠被打的图片
mouse_click = cv2.resize(mouse_click, (109, 101))  # 调整为109x101像素

# 全局变量
sx = 0  # 地鼠横坐标
sy = 0  # 地鼠纵坐标
ds = 0  # 地鼠存在状态
sc = -1  # 得分
cx = 0  # 手部横坐标
cy = 0  # 手部纵坐标
jsss = 0  # 手部判断锁定
zys = 0  # 左右手状态

# 构造游戏的类
class GameClass:

    # 类初始化
    def __init__(self):
        self.mouserandom()  # 在范围内随机生成地鼠
        self.mouseclick = False  # 地鼠是否被打
        self.lasttime = 0  # 地鼠刷新时间

    # 在范围内随机生成地鼠
    def mouserandom(self):
        global sx, sy, ds, sc
        sx = random.randint(280, 1020)
        sy = random.randint(280, 600)
        ds = 1  # 地鼠存在
        sc += 1  # 记录得分

    # 运行游戏
    def play(self):
        global ds, sx, sy
        w, h = 109, 101  # 地鼠素材长宽
        now = int(round(time.time() * 1000))
        if self.mouseclick:
            ds = 0  # 地鼠不存在状态
            now = int(time.time() * 1000)  # 取现在时间
            if now - self.lasttime > 500:  # 500毫秒后重置地鼠
                self.mouseclick = False
                self.mouserandom()
        else:
            if (sx - w // 2 < cx < sx + w // 2) and (sy - h // 2 < cy < sy + h // 2):  # 检测是否在范围内产生被打状态
                self.mouseclick = True
                self.lasttime = now

cap = cv2.VideoCapture(0)  # 电脑自带摄像头
cap.set(3, 1280)  # 窗口宽1280
cap.set(4, 720)  # 窗口高720
detector = HandDetector(maxHands=1, detectionCon=0.8)  # 手部检测
game = GameClass()  # 加载游戏类

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)  # 翻转摄像头照片
    hands, img = detector.findHands(img, flipType=False, draw=False)  # 手部检测
    screen_center = img.shape[1] // 2  # 取屏幕左右宽度

    if hands:  # 检测到存在手势
        hand = hands[0]
        List = hand['lmList']  # 检测食指位置
        cx = List[8][0]
        cy = List[8][1]
        if jsss == 0:
            if cx < screen_center:
                zys = 0  # 检测为右手
            else:
                zys = 1  # 检测为左手
        jsss = 1  # 锁定本轮首次检测结果
    else:
        jsss = 0  # 释放锁定

    img = cv2.addWeighted(background_image, 1, img, 0, 0)  # 覆盖背景图片
    game.play()

    if ds == 1:  # 地鼠处于正常状态
        img = cvzone.overlayPNG(img, mouse, (sx - 54, sy - 51))
    else:  # 地鼠处于被打状态
        img = cvzone.overlayPNG(img, mouse_click, (sx - 50, sy - 50))

    if zys == 0:  # 右手生成右锤
        img = cvzone.overlayPNG(img, hammer_right, (cx - 85, cy - 85))
    if zys == 1:  # 左手生成左锤
        img = cvzone.overlayPNG(img, hammer_left, (cx - 85, cy - 85))

    cv2.putText(img, f'Score:{sc}', (1111, 545), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)  # 得分文本
    cv2.imshow('OpenCV Python GestureGame Whack-A-Mole', img)

    # ESC按键结束
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()