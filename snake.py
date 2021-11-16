import selenium, time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("Snake Bot\nby Owen")
def w():
  pyautogui.press('w')
def a():
  pyautogui.press('a')
def s():
  pyautogui.press('s')
def d():
  pyautogui.press('d')
def press(key):
  pyautogui.press(key)
driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(626, 740)
driver.get("https://www.google.com/fbx?fbx=snake_arcade")
game = driver.find_elements_by_class_name("cer0Bd")[0]
gridsize = "17 x 15"
pyautogui.press('RETURN')
time.sleep(0.5)
press('s')