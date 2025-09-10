import tkinter as tk
from functools import partial


class RoomGUI:
    open_color = "green"
    closed_color = "red"
    button_list = []
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x500")

        label = tk.Label(self.window, text="Practice Rooms", font=('Times', 20, 'bold'))
        label.pack(pady=20)

        btn_frame = tk.Frame(self.window)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)

        self.room_btn1 = tk.Button(btn_frame, text="Room 1\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 1))
        self.room_btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn1)
        self.room_btn2 = tk.Button(btn_frame, text="Room 2\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 2))
        self.room_btn2.grid(row=1, column=0, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn2)
        self.room_btn3 = tk.Button(btn_frame, text="Room 3\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 3))
        self.room_btn3.grid(row=2, column=0, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn3)
        self.room_btn4 = tk.Button(btn_frame, text="Room 4\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 4))
        self.room_btn4.grid(row=0, column=1, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn4)
        self.room_btn5 = tk.Button(btn_frame, text="Room 5\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 5))
        self.room_btn5.grid(row=1, column=1, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn5)
        self.room_btn6 = tk.Button(btn_frame, text="Room 6\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 6))
        self.room_btn6.grid(row=2, column=1, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn6)
        self.room_btn7 = tk.Button(btn_frame, text="Room 7\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 7))
        self.room_btn7.grid(row=0, column=2, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn7)
        self.room_btn8 = tk.Button(btn_frame, text="Room 8\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 8))
        self.room_btn8.grid(row=1, column=2, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn8)
        self.room_btn9 = tk.Button(btn_frame, text="Room 9\nOpen", font=('Times', 16, 'bold'), background=RoomGUI.open_color, command=partial(self.clicked, 9))
        self.room_btn9.grid(row=2, column=2, sticky=tk.W + tk.E)
        RoomGUI.button_list.append(self.room_btn9)

        btn_frame.pack(fill='x')

        self.window.mainloop()

    def clicked(self, num):
        if RoomGUI.button_list[num-1].cget("bg") == self.open_color:
            RoomGUI.button_list[num-1].config(background=RoomGUI.closed_color, text="Room " + str(num) + "\nClosed")
        else:
            RoomGUI.button_list[num-1].config(background=RoomGUI.open_color, text="Room " + str(num) + "\nOpen")

RoomGUI()