from customtkinter import *
set_appearance_mode("light")
set_default_color_theme("blue")

app = CTk()
app.geometry("500x500")
app.minsize(500,500)
app.maxsize(600,600)
app.title("Calculator")
label_frame = CTkFrame(app, fg_color="#D9E76C", height=500, width=500, corner_radius=0.5)
label_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1) 

label = CTkLabel(label_frame, text="Calculator", text_color="black", font=("San Francisc", 35,"bold"))
label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#function

#on click function
def button_click(value):
    try:
        if value == '=':
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(0, result)
        elif value == 'C':
            entry.delete(0, END)
        elif value == 'backspace':
            current_text = entry.get()
            entry.delete(0, END)
            entry.insert(0, current_text[:-1]) 
        else:
            entry.insert(END, value)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

#entry
entry = CTkEntry(label_frame, placeholder_text="enter number here", width=400, height=50, corner_radius=7, font=("Arial", 25, "bold"))
entry.grid(pady=20,padx=40, columnspan=4, row=1)

#buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'backspace' 
]
row=2
col=0
for btn in buttons:
    
    button = CTkButton(label_frame, text=btn, font=("Arial", 15,"bold"), height=50, width=100, command=lambda b=btn: button_click(b)).grid(row=row, column=col,padx=5,pady=5,sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()