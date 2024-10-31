import pyautogui
import time

while(True):
        try:
            playButton1 = pyautogui.locateOnScreen('Play.png', confidence=0.9)
            pyautogui.click(playButton1)
        
        
        except:
            try:
                playButton2 = pyautogui.locateOnScreen('Play2.png', confidence=0.9)
                pyautogui.click(playButton2)
                
            except:
                try:
                    xButton = pyautogui.locateOnScreen('X.png', confidence=0.9)
                    pyautogui.click(xButton)

                except:
                    try:
                        cart_surfer = pyautogui.locateOnScreen('Start.png', confidence=0.9)
                        pyautogui.click(cart_surfer)
                        
                    except:
                            t_end = time.time()+4
                            while time.time() < t_end:
                                pyautogui.press("space")
                                pyautogui.press("a")
                                pyautogui.press("s")
                                
                           
   