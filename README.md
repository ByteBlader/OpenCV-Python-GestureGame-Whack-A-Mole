# OpenCV Python GestureGame: Whack-A-Mole
### 🐹 Python combined with OpenCV to implement Whack-A-Mole gesturegame [中文文档](https://github.com/ByteBlader/OpenCV-Python-GestureGame-Whack-A-Mole/blob/main/README_CN.md)
This is a fun and interactive game developed using Python and OpenCV, where players use hand gestures to play a virtual version of the classic "Whack-A-Mole" game. The game utilizes the camera to detect hand movements and simulates the act of whacking moles as they pop up from their holes.
![Screenshot](https://pic.superbed.cc/item/666117dbfcada11d37d8d61a.jpg)

## Features

- **Hand Gesture Recognition**: The game detects hand gestures using OpenCV's hand tracking module.
- **Real-Time Interaction**: Players can interact with the game in real-time.
- **Score Tracking**: Keeps track of the player's score as they hit the moles.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- cvzone (a helper library for OpenCV)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ByteBlader/OpenCV-Python-GestureGame-Whack-A-Mole.git
   ```
2. Install the required packages:
   ```
   pip install opencv-python numpy cvzone
   ```
3. Run the game:
   ```
   python main.py
   ```

## How to Play

- Open the game and allow access to your camera.
- Use your hand to whack the moles as they appear.
- The game will detect your hand's position and show a hammer in the corresponding hand.
- Whack the mole before it disappears to earn points.

## Game Controls

- **Right Hand**: A right-side hammer will appear.
- **Left Hand**: A left-side hammer will appear.


## Contributing

For bug reports, please create an issue.

## License

This project is open-source and available under the [Apache-2.0 License](https://github.com/ByteBlader/OpenCV-Python-GestureGame-Whack-A-Mole/blob/main/LICENSE).
