import tkinter as tk
import time
import random
import mouse

random.seed()
class Bug():
        def __init__(self):
                self.window = tk.Tk()
# ------------- RESOURCES -----
        # ----- animation
                self.walkingUp    = [tk.PhotoImage(file='resources/walkingUp.gif', format = 'gif -index %i' % (i)) for i in range(2)]
                self.walkingDown  = [tk.PhotoImage(file='resources/walkingDown.gif', format = 'gif -index %i' % (i)) for i in range(2)]
                self.walkingLeft  = [tk.PhotoImage(file='resources/walkingLeft.gif', format = 'gif -index %i' % (i)) for i in range(2)]
                self.walkingRight = [tk.PhotoImage(file='resources/walkingRight.gif', format = 'gif -index %i' % (i)) for i in range(2)]
                self.coffeeBreak  = [tk.PhotoImage(file='resources/coffeeBreak.gif', format = 'gif -index %i' % (i)) for i in range(2)]     
# ------------- INIT CONFIG -----
        # ----- animation
                self.frameIndex    = 0
                self.animationType = self.walkingRight
                self.image         = self.animationType[self.frameIndex]
        # ----- time
                self.frameTime      = 0.05
                self.randomTime     = 2
                self.frameStopTime  = time.time()
                self.randomStopTime = time.time()
        # ----- position
                self.x = 0
                self.y = 0
                self.vector         = [1, 0]
                self.previousVector = [0, 0]
        # ----- mode
                self.isRandom = True
                self.isChasingMouse = False
        # ----- window
                self.window.config(highlightbackground = 'white')
                self.window.attributes('-topmost', True)
                self.window.wm_attributes('-transparentcolor', 'white')
                self.window.overrideredirect(True)
                self.window.geometry('128x128+{x}+{y}'.format(x = str(self.x), y = str(self.y)))
                self.label = tk.Label(self.window, bd = 0, bg = 'white')
                self.label.configure(image = self.image)
                self.label.pack()
                self.window.after(0, self.update)
                self.window.mainloop()

        def update(self):
# ------------- MOUSE -----
                if mouse.is_pressed("left"):
                        self.isRandom       = False
                        self.isChasingMouse = True
                else:
                        self.isRandom       = True
                        self.isChasingMouse = False
# ------------- VECTOR -----
        # ----- controlled vector selection
                if self.isRandom == False:
                # ----- vector orientation towards the mouse
                        if self.isChasingMouse == True:
                                self.mousePosition = mouse.get_position()
                                self.geometryInfo  = (self.window.winfo_geometry()).split("+")
                                self.bugPosition   = [int(self.geometryInfo[1]), int(self.geometryInfo[2])]
                                for i in range(0, 2):
                                        self.vector[i] = 0
                                        if self.mousePosition[i] > self.bugPosition[i]:
                                                self.vector[i] = 1
                                        elif self.mousePosition[i] < self.bugPosition[i]:
                                                self.vector[i] = -1
        # ----- random vector selection  
                elif self.isRandom == True:
                        if time.time() > self.randomStopTime + self.randomTime:
                                self.randomStopTime = time.time()
                                self.randomTime     = random.uniform(2, 10)
                                self.vector[0] = random.choice([-1, 0, 1])
                                self.vector[1] = random.choice([-1, 0, 1])
        # ----- math implementation of "taking a step" 
                self.x += self.vector[0]
                self.y += self.vector[1]
# ------------- ANIMATION -----
        # ----- animation type settings     
                self.isFirstIdentical  = (self.vector[0] == self.previousVector[0])
                self.isSecondIdentical = (self.vector[0] == self.previousVector[0])
                if self.isFirstIdentical == False | self.isSecondIdentical == False:
                        self.previousVector = [self.vector[0], self.vector[1]]
                        if self.vector == [0, -1]:
                                self.animationType = self.walkingUp
                        elif self.vector == [0, 1]:
                                self.animationType = self.walkingDown
                        elif self.vector[0] < 0:
                                self.animationType = self.walkingLeft 
                        elif self.vector[0] > 0:
                                self.animationType = self.walkingRight
                        elif self.vector == [0, 0]:
                                self.animationType = self.coffeeBreak
        # ----- animation of "taking steps"
                if time.time() > self.frameStopTime + self.frameTime:
                        self.frameStopTime = time.time()
                        self.frameIndex    = (self.frameIndex + 1) % 2
                        self.image         = self.animationType[self.frameIndex]
        # ----- window action
                self.window.geometry('128x128+{x}+{y}'.format(x = str(self.x), y = str(self.y)))
                self.label.configure(image = self.image)
                self.label.pack()
                self.window.after(10, self.update)
Bug()