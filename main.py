import keyboard
from image_reader import recognize_japanese_text
from overlay import create_overlay
from image_extractor import take_screenshot

def main():
    image_data, top_left_coords = take_screenshot()

    recognized_words = recognize_japanese_text(image_data)
    create_overlay(image_data, recognized_words, top_left_coords)

main()