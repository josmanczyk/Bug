import tkinter as tk
import time
import random

random.seed()
class Bug():
    def __init__(self):
        self.window     = tk.Tk()
        self.frameTime  = time.time()
        self.onewayTime = time.time()
        self.randomTime = random.uniform(2, 10)
# walking resources
        self.walkingUp      = [tk.PhotoImage(file='resources/walkingUp.gif', format = 'gif -index %i' % (i)) for i in range(2)]
        self.walkingDown    = [tk.PhotoImage(file='resources/walkingDown.gif', format = 'gif -index %i' % (i)) for i in range(2)]
        self.walkingLeft    = [tk.PhotoImage(file='resources/walkingLeft.gif', format = 'gif -index %i' % (i)) for i in range(2)]
        self.walkingRight   = [tk.PhotoImage(file='resources/walkingRight.gif', format = 'gif -index %i' % (i)) for i in range(2)]
        self.coffeeBreak    = [tk.PhotoImage(file='resources/coffeeBreak.gif', format = 'gif -index %i' % (i)) for i in range(2)]
        self.frameIndex = 0
        self.walking    = self.walkingRight
        self.img        = self.walking[self.frameIndex]
# window configuration
        self.window.config(highlightbackground = 'white')
        self.window.wm_attributes('-transparentcolor', 'white')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.label = tk.Label(self.window, bd = 0, bg = 'white')
# window action
        self.x = 0
        self.y = 0
        self.vector = [1, 0]
        self.window.geometry('128x128+{x}+{y}'.format(x = str(self.x), y = str(self.y)))
        self.label.configure(image = self.img)
        self.label.pack()
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):
# walking
        if time.time() > self.frameTime + 0.05:
                self.frameTime = time.time()
                self.frameIndex = (self.frameIndex + 1) % 2
                self.img = self.walking[self.frameIndex]
# pinch of unpredictability
        if time.time() > self.onewayTime + self.randomTime:
                self.onewayTime = time.time()
                self.randomTime = random.uniform(2, 10)
                self.vector[0] = random.choice([-1, 0, 1])
                self.vector[1] = random.choice([-1, 0, 1]) 
                if self.vector == [0, -1]:
                        self.walking = self.walkingUp
                elif self.vector == [0, 1]:
                        self.walking = self.walkingDown
                elif self.vector[0] < 0:
                        self.walking = self.walkingLeft 
                elif self.vector[0] > 0:
                        self.walking = self.walkingRight
                elif self.vector == [0, 0]:
                        self.walking = self.coffeeBreak
        self.x += self.vector[0]
        self.y += self.vector[1] 
# window action
        self.window.geometry('128x128+{x}+{y}'.format(x = str(self.x), y = str(self.y)))
        self.label.configure(image = self.img)
        self.label.pack()
        self.window.after(10, self.update)
Bug()