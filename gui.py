import tkinter as tk 

def create_window(get_weather_data):
    root = tk.Tk()
    root.title("Hava Durumu")

    label = tk.Label(root, text="Şehir adı girin")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    result_label = tk.Label(root)
    result_label.pack()

    def on_button_click():
        city = entry.get()
        data = get_weather_data(city)
        result_label.config(text=data)

    
    button = tk.Button(root, text="Hava durumunu Getir", command=on_button_click)
    button.pack()

    root.mainloop()