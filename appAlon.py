import tkinter as tk
from tkinter import ttk
import csv

class MyApp_alon:
    def __init__(self, root, ls):
        self.root = root
        self.root.title("My App")
        self.root.geometry("320x200")

        tpis = []
        with open('data/imgs.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            tpis = [row[0] for row in reader]

        # Initialize data
        self.languages = (tpis)
        self.option_var = tk.StringVar(self.root)

        self.file_headers = {}
        self.counter = 0
        self.ls = ls

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        defName = self.ls[self.counter].split('\\')[-1].split('.')[0]
        self.label = ttk.Label(self.root, text="נא הכנס את הפרטים בשביל המאמר:\n" + defName)
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Label for the first field
        self.label1 = ttk.Label(self.root, text="שם מאמר")
        self.label1.grid(row=1, column=1, padx=5, pady=5)
        #label1.pack()

        # Entry field for the first input
        self.entry1 = ttk.Entry(self.root)
        #defName = self.ls[self.counter].split('\\')[-1].split('.')[0]
        self.entry1.insert(0, defName)
        self.entry1.grid(row=1, column=0, padx=5, pady=5)
        #entry1.pack()

        # Label for the second field
        self.label2 = ttk.Label(self.root, text="שם הכותב")
        self.label2.grid(row=2, column=1, padx=5, pady=5)

        #label2.pack()

        # Entry field for the second input
        self.entry2 = ttk.Entry(self.root)
        self.entry2.insert(0, "האיש החשוב")
        self.entry2.grid(row=2, column=0, padx=5, pady=5)

        #entry2.pack()

        # Label for the third field (List)
        self.label3 = ttk.Label(self.root, text="סוג המאמר")
        self.label3.grid(row=3, column=1, padx=5, pady=5)
        #label3.pack()

        # Listbox (dropdown menu) for selecting a language
        self.option_menu = ttk.OptionMenu(self.root, self.option_var, self.languages[0], *self.languages)
        self.option_menu.grid(row=3, column=0, padx=5, pady=5)

        #option_menu.pack()


        # OK button
        self.ok_button = tk.Button(self.root, text="OK", command=self.on_ok)
        self.ok_button.grid(row=5,column=1, padx=5, pady=5)

    def on_ok(self):
        # Get values from entry fields
        value1 = self.entry1.get()
        value2 = self.entry2.get()

        # Get selected item from listbox
        selected_item = self.option_var.get()

        self.file_headers[self.ls[self.counter]] = [value1, value2, selected_item]
        print(selected_item)

        self.counter += 1
        if self.counter < len(self.ls):
            defName = self.ls[self.counter].split('\\')[-1].split('.')[0]
            self.label['text'] = "נא הכנס את הפרטים בשביל המאמר:\n" + defName
            self.entry1.delete(0, tk.END)  # Clear existing text
            self.entry1.insert(0, defName)

        else:
            self.root.quit()

        # Display the values


    def on_ok1(self):
        # Get values from entry fields
        value1 = self.entry1.get()
        value2 = self.entry2.get()
        value3 = self.entry3.get()
        value4 = self.entry4.get()


        self.pirtey = [value1, value2, value3, value4]

        self.root.quit()

        # Display the values
    def on_ok2(self):
        # Get values from entry fields
        value1 = self.entry1.get()
        value2 = self.entry2.get()

        self.font = [value1, int(value2)]

        for ele in self.root.winfo_children():
            ele.destroy()

        self.root.quit()

        # Display the values


    def pirtey_alon(self):
        for ele in self.root.winfo_children():
            ele.destroy()

        self.label = ttk.Label(self.root, text="הכנס את פרטי העלון")
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.label1 = ttk.Label(self.root, text="מספר עלון")
        self.label2 = ttk.Label(self.root, text="פרשה")
        self.label3 = ttk.Label(self.root, text="תאריך")
        self.label4 = ttk.Label(self.root, text="נושא")

        self.label1.grid(row=1, column=1, padx=5, pady=5)
        self.label2.grid(row=2, column=1, padx=5, pady=5)
        self.label3.grid(row=3, column=1, padx=5, pady=5)
        self.label4.grid(row=4, column=1, padx=5, pady=5)

        self.entry1 = ttk.Entry(self.root)
        self.entry2 = ttk.Entry(self.root)
        self.entry3 = ttk.Entry(self.root)
        self.entry4 = ttk.Entry(self.root)

        self.entry1.insert(0, 999)
        self.entry2.insert(0, "פרשה")
        self.entry3.insert(0, "תאריך")
        self.entry4.insert(0, "נושא")

        self.entry1.grid(row=1, column=0, padx=5, pady=5)
        self.entry2.grid(row=2, column=0, padx=5, pady=5)
        self.entry3.grid(row=3, column=0, padx=5, pady=5)
        self.entry4.grid(row=4, column=0, padx=5, pady=5)

        self.ok_button = tk.Button(self.root, text="OK", command=self.on_ok1)
        self.ok_button.grid(row=5,column=1, padx=5, pady=5)

    def Font(self):
        for ele in self.root.winfo_children():
            ele.destroy()

        self.label = ttk.Label(self.root, text="הכנס את הפונט הרצוי")
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.label1 = ttk.Label(self.root, text="פונט")
        self.label2 = ttk.Label(self.root, text="גודל")

        self.label1.grid(row=1, column=1, padx=5, pady=5)
        self.label2.grid(row=2, column=1, padx=5, pady=5)

        self.entry1 = ttk.Entry(self.root)
        self.entry2 = ttk.Entry(self.root)

        self.entry1.insert(0, "Assistant")
        self.entry2.insert(0, 10)

        self.entry1.grid(row=1, column=0, padx=5, pady=5)
        self.entry2.grid(row=2, column=0, padx=5, pady=5)

        self.ok_button = tk.Button(self.root, text="OK", command=self.on_ok2)
        self.ok_button.grid(row=5,column=1, padx=5, pady=5)



