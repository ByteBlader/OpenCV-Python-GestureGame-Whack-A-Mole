# OpenCV Python 手势游戏：打地鼠
### 🐹 使用Python和OpenCV实现打地鼠的手势游戏 [English Docs](https://github.com/uliaxs0n/OpenCV-Python-GestureGame-Whack-A-Mole/blob/main/README.md)
这是一个使用Python和OpenCV开发的有趣且互动的游戏，玩家使用手势来玩家喻户晓的“打地鼠”游戏。游戏利用摄像头检测手部动作，并模拟敲打弹出的地鼠以获得积分。
![Screenshot](https://pic.superbed.cc/item/666117dbfcada11d37d8d61a.jpg)

## 特点

- **手势识别**：游戏使用OpenCV的手部跟踪模块来检测手势。
- **实时互动**：玩家可以使用摄像头实时与游戏互动。
- **得分统计**：在击中地鼠时记录玩家的得分。

## 导入

- Python 3.x
- OpenCV
- NumPy
- cvzone（OpenCV辅助库）

## 安装

1. 克隆仓库：
   ```
   git clone https://github.com/uliaxs0n/OpenCV-Python-GestureGame-Whack-A-Mole.git 
   ```
2. 安装所需包：
   ```
   pip install opencv-python numpy cvzone
   ```
3. 运行游戏：
   ```
   python main.py
   ```

## 游玩

- 打开游戏并允许访问您的摄像头。
- 使用手敲打出现的地鼠。
- 游戏将检测手的位置并在相应的手中显示一个锤子。
- 在地鼠消失前敲打它以获得分数。

## 控制

- **右手**：将出现右侧的锤子。
- **左手**：将出现左侧的锤子。

## 贡献

对于错误报告，请在Github上创建问题咨询我。

## 许可证

本项目采用 [Apache-2.0许可证](https://github.com/uliaxs0n/OpenCV-Python-GestureGame-Whack-A-Mole/blob/main/LICENSE) 许可协议。
