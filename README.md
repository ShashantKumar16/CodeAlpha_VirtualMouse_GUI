# 🖱️ Virtual Mouse Simulator (GUI Version) — CodeAlpha Internship

This project is developed as part of the **CodeAlpha Artificial Intelligence Internship (June–July 2025)** by **Shashant Kumar**.

## 📌 Project Overview

This is a **GUI-based simulation** of an AI-powered virtual mouse built using Python. It mimics gesture-based mouse control by using sliders and click buttons — allowing users to simulate mouse movement and actions without a webcam.

> ⚠️ **Note:** Due to webcam hardware issues, this project replaces hand gesture detection with a GUI interface for interaction using `pyautogui`.

## 🧠 Features

- 🎮 Simulate mouse movement using **X/Y position sliders**
- 🖱️ Perform **left** and **right clicks** with buttons
- 💻 Built using **Streamlit** for a clean user interface
- 🧰 Uses `pyautogui` to control the actual mouse pointer

## 🧰 Tech Stack

- Python 3
- Streamlit
- PyAutoGUI

## 💻 How to Run the App

### Step 1: Install Required Libraries

```bash
pip install streamlit pyautogui
Step 2: Run the App
streamlit run virtual_mouse_gui.py
🎮 Controls Summary
| UI Control       | Function                            |
| ---------------- | ----------------------------------- |
| `X`, `Y` sliders | Move mouse pointer to screen coords |
| `Left Click`     | Simulates a standard left click     |
| `Right Click`    | Simulates a right click             |
📂 File Structure
Task3VirtualMouse_GUI/
├── virtual_mouse_gui.py       # Main Streamlit app
└── README.md                  # Project documentation
📽️ Demo Video
🎥 Coming soon... (To be posted on LinkedIn with CodeAlpha tag)
👨‍💻 Author
Shashant Kumar
AI Intern @ CodeAlpha
GitHub
LinkedIn

📜 License
This project is licensed under the MIT License.

---



