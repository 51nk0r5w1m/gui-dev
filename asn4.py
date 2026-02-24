# C. Fant / Spring 2026 / GUI Development V01 / ASN4

import tkinter as tk
from PIL import Image, ImageTk


class FoodViewer:
    def __init__(self):
        # --- Main window ---
        self.root = tk.Tk()
        self.root.title("Food Viewer")
        self.root.minsize(400, 300)

        # --- Two frames ---
        self.img_frame = tk.Frame(self.root)
        self.rbdBtn_frame = tk.Frame(self.root)

        # --- Load and resize all 4 images ---
        self.img1 = Image.open("images/chicken.jpg")
        self.img1 = self.img1.resize((400, 300))
        self.imgOne = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("images/pie.jpg")
        self.img2 = self.img2.resize((400, 300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("images/pizza.jpg")
        self.img3 = self.img3.resize((350, 300))
        self.imgThree = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("images/steak.jpg")
        self.img4 = self.img4.resize((300, 300))
        self.imgFour = ImageTk.PhotoImage(self.img4)

        # --- Label in img_frame, starts with chicken image ---
        self.lbl = tk.Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()

        # --- IntVar initialized to 1 (Chicken is selected at startup) ---
        self.var = tk.IntVar()
        self.var.set(1)

        # --- 4 Radiobuttons in rbdBtn_frame ---
        self.radio_a = tk.Radiobutton(self.rbdBtn_frame,
                                      text="Chicken",
                                      value=1,
                                      variable=self.var,
                                      command=self.on_radio_select)
        self.radio_a.pack(side="left", padx=10)

        self.radio_b = tk.Radiobutton(self.rbdBtn_frame,
                                      text="Pie",
                                      value=2,
                                      variable=self.var,
                                      command=self.on_radio_select)
        self.radio_b.pack(side="left", padx=10)

        self.radio_c = tk.Radiobutton(self.rbdBtn_frame,
                                      text="Pizza",
                                      value=3,
                                      variable=self.var,
                                      command=self.on_radio_select)
        self.radio_c.pack(side="left", padx=10)

        self.radio_d = tk.Radiobutton(self.rbdBtn_frame,
                                      text="Steak",
                                      value=4,
                                      variable=self.var,
                                      command=self.on_radio_select)
        self.radio_d.pack(side="left", padx=10)

        # --- Pack the frames ---
        self.img_frame.pack()
        self.rbdBtn_frame.pack()

        # --- Start tkinter main loop ---
        self.root.mainloop()

    def on_radio_select(self):
        choice = self.var.get()        # 1=Chicken, 2=Pie, 3=Pizza, 4=Steak
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)


if __name__ == "__main__":
    app = FoodViewer()
