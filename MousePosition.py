# New Mouse Position Clicker. By BigEmo
import pyautogui as py, keyboard

def myClicker():
    print("Enter to show position. ")
    print("Press Ctrl-C to quit. ")
    while True:
      keyboard.wait('enter')
      print(tuple(py.position()))


def ended():
  try:
    myClicker()
  except:
      print("Done")

ended()