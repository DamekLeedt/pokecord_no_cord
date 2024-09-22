import tkinter as tk
from PIL import Image, ImageTk

def main():
    show_image()

def tk_tests():
    window = tk.Tk()

    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame1.pack(fill=tk.Y, side=tk.LEFT)

    frame2 = tk.Frame(master=window, width=100, bg="yellow")
    frame2.pack(fill=tk.Y, side=tk.LEFT)

    frame3 = tk.Frame(master=window, width=50, bg="blue")
    frame3.pack(fill=tk.Y, side=tk.LEFT)

    window.mainloop()

def entry_widget():
    window = tk.Tk()
    frame_a = tk.Frame()

    entry = tk.Entry(master=frame_a, width=40, fg="black", bg="white")
    entry.insert(0, "What is your name?")
    entry.pack()

    frame_a.pack()

    window.mainloop()

def frame_effects():

    border_effects = {
        "flat": tk.FLAT,
        "sunken": tk.SUNKEN,
        "raised": tk.RAISED,
        "groove": tk.GROOVE,
        "ridge": tk.RIDGE,
    }

    window = tk.Tk()

    for relief_name, relief in border_effects.items():
        frame = tk.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tk.LEFT)
        label = tk.Label(master=frame, text=relief_name)
        label.pack()

    window.mainloop()

def show_image():
    window = tk.Tk()

    canvas = tk.Canvas()
    canvas.pack()

    image = Image.open("./images/137.png")
    image = image.resize((500, 500))

    img = ImageTk.PhotoImage(image)
    canvas.create_image(100,100,image=img)

    window.mainloop()

main()