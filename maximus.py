import Tkinter as tk
import tkMessageBox
import os
import sys
root = tk.Tk()
#root.attributes('-fullscreen', True)
root.minsize(300,100)
root.title('Maximus @arshit09')
w = tk.Label(root, text="MAXIMUS\nFor more such tools: github.com/arshit09")
w.pack()
def helloCallBack():
    phish = tk.Tk()
    z = tk.Label(phish, text="MAXIMUS\nFor more such tools: github.com/arshit09")
    z.pack()
    phish.mainloop()
    #os.system('git clone https://github.com/arshit09/Ezzz')
b1 = tk.Button (root, text="Phishing Tools",command = helloCallBack)
b1.pack()
b2 = tk.Button (root, text="Payload/Backdoor Generator",command = helloCallBack)
b2.pack()
b3 = tk.Button (root, text="Dos/DDoS Tool",command = helloCallBack)
b3.pack()
b4 = tk.Button (root, text="WiFi Attack Tools",command = helloCallBack)
b4.pack()
b5 = tk.Button (root, text="SMS and Call Bomber",command = helloCallBack)
b5.pack()
b6 = tk.Button (root, text="Collections of Tools' Tool",command = helloCallBack)
b6.pack()
root.mainloop()