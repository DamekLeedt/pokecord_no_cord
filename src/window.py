import tkinter as tk

HEIGHT = 375
WIDTH = 750

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack(fill='both')

background_image = tk.PhotoImage(file='../images/backgrounds/image.png')
background = tk.Label(root, image=background_image, border=3)
background.place(relx=0.01, rely=0.02, relheight=0.75, relwidth=0.75)

pokemon_image = tk.PhotoImage(file='../images/pokemon/137.png')
pokemon = tk.Label(root, image=pokemon_image)
pokemon.place(relx=0.33, rely=0.25, relheight=0.2, relwidth=0.1)

# button = tk.Button(frame, text="HeightxWidth of window.")
# button.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.6)

root.mainloop()
