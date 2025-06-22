import streamlit as st
import pyautogui
import time

st.set_page_config(page_title="Virtual Mouse GUI", layout="centered")

st.title("🖱️ Virtual Mouse Simulator - GUI Edition")
st.markdown("Simulate mouse movement and clicks using sliders and buttons.")

# Get screen size
screen_width, screen_height = pyautogui.size()

# User-controlled sliders for mouse position
x = st.slider("X Position", 0, screen_width, screen_width // 2)
y = st.slider("Y Position", 0, screen_height, screen_height // 2)

# Move button
if st.button("Move Mouse"):
    pyautogui.moveTo(x, y)
    st.success(f"Moved mouse to ({x}, {y})")

# Left click
if st.button("Left Click"):
    pyautogui.click()
    st.info("Left click performed.")

# Right click
if st.button("Right Click"):
    pyautogui.click(button='right')
    st.info("Right click performed.")

# Delay to avoid fast re-clicks
time.sleep(0.5)
