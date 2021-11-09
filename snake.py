import selenium, keyboard, time, os, math, random, pathfinding, ctypes, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("Snake Bot\nby Owen")
driver = webdriver.Chrome('chromedriver.exe')
driver.set_window_size(626, 740)
driver.get("https://www.google.com/fbx?fbx=snake_arcade")
game = driver.find_elements_by_class_name("ahZmw")[0]
gridsize = "17 x 15"
keyboard.press_and_release('RETURN')
keyboard.press_and_release('w')
