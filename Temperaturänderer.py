import tkinter as tk
import f_to_c
import c_to_f
import ttkbootstrap as ttk




#window
window = ttk.Window(themename="darkly")
window.title("Temperaturänderer")
window.geometry("400x150")

#Titel
titel_label = tk.Label(master=window, text="Temperaturänderer", font="Calibri 20")
titel_label.pack(pady=10)

#EingabeFeld
input_frame = tk.Frame(master=window, height=40)

entryInt = tk.IntVar()
entry = tk.Entry(master=input_frame, textvariable=entryInt, font="Calibri 16")
entry.grid(row=0, column=0, padx=10, pady=5, sticky="we")

knopf_cel = tk.Button(master=input_frame, text="zu Celsius", command=lambda: ouput_string.set(f_to_c.formel(entryInt.get())), font="Calibri 16")
knopf_cel.grid(row=0, column=1, padx=10, pady=5)

knopf_fah = tk.Button(master=input_frame, text="zu Fahrenheit", command=lambda: ouput_string.set(c_to_f.formel(num = entryInt.get())), font="Calibri 16")
knopf_fah.grid(row=0, column=2, padx=10, pady=5)

input_frame.columnconfigure(0, weight=1)
input_frame.pack()

#Ausgabe
ouput_string = tk.StringVar()
output_label = tk.Label(master=window, text="test", textvariable=ouput_string, font="Calibri 16")
output_label.pack(pady=10)

window.mainloop()
