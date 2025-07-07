import customtkinter  as ctk

USD = 5.46
JPN = 0.037
EUR = 6.41

# appearence mode function
def setmode(var1):
     ctk.set_appearance_mode(var1)

font = ctk.CTkFont = "Monospace", 24
resultfont = ctk.CTkFont = "Calibri", 18

# conversion function
def convert(cur):
     if cur == "USD":
          result = int(origincoinentry.get()) / USD
     elif cur == "JPN":
          result = int(origincoinentry.get()) / JPN
     elif cur == "EUR":
          result = int(origincoinentry.get()) / EUR
     resulttext = "{:.2f}".format(result)
     currencyresultlabel.configure(text=resulttext)


# setting the window
app = ctk.CTk()
app.geometry("300x400")
app.title("Currency Converter")

titlelabel = ctk.CTkLabel(app, text="Currency Converter", font=font)
titlelabel.pack(pady=10)

# setting the mode
modebox = ctk.CTkComboBox(
    app,
    values = ["Light", "Dark"],
    command = setmode
)
modetitlelabel = ctk.CTkLabel(app, text="Set Appearece Mode:")
modetitlelabel.pack(pady=10)
modebox.pack(pady = .1)

# Currency label/entry
origincoinlabel  = ctk.CTkLabel(app, text="Insert the origin Currency:")
origincoinentry = ctk.CTkEntry(app, placeholder_text="Insert the value")

destinycoinlabel = ctk.CTkLabel(app, text="Destiny Currency:")
currencyresultlabel = ctk.CTkLabel(app, text = "", font=resultfont)

origincoinlabel.pack(pady=10)
origincoinentry.pack(pady=10)

destinycoinlabel.pack(pady=10)
currencyresultlabel.pack(pady=22)

# Currency Selection Box
currencybox = ctk.CTkComboBox(
     app,
     values = ["USD", "JPN", "EUR"],
     command = convert
)
currencybox.pack(pady=10)

# running the app
app.mainloop()