import pyautogui
import time

MapNumber = {1:[137, 535],11:[758,534],21:[631,627],
             2:[205, 540],12:[819,533],22:[697,628],
             3:[264, 538],13:[137,627],23:[755,626],
             4:[319, 538],14:[199,628],24:[820,626],
             5:[392,526],15:[263,629],25:[136,719],
             6:[454,540],16:[321,626],
             7:[513,536],17:[383,629],
             8:[567,532],18:[446,628],
             9:[638,536],19:[507,626],
             10:[693,533],20:[570,626]}

def AutoInsert(game:list):
    pyautogui.hotkey('winleft','2')
    time.sleep(2)
    pyautogui.press('down', presses=13)
    time.sleep(2)

    for i in game:
        if i in MapNumber:
            px = MapNumber[i][0]
            py = MapNumber[i][1]
            time.sleep(0.1)
            pyautogui.click(x=px,y=py)
    pyautogui.press('down', presses=16)
    time.sleep(0.3)
    pyautogui.click(x=780, y=717)
    pyautogui.press('home')