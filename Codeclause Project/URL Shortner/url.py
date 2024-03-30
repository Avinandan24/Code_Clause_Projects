import tkinter as tk
from tkinter import ttk, messagebox
import pyshorteners

def save_to_file(url, short_url):
    with open('urls.txt', 'a') as file:
        file.write(f"{url} : {short_url}\n")

def shorten_url():
    url = url_entry.get()
    try:
        short_url = pyshorteners.Shortener().tinyurl.short(url)
        result_label.config(text=f"Shortened URL: {short_url}", foreground="green")
        save_to_file(url, short_url)
    except pyshorteners.exceptions.ShorteningErrorException as e:
        messagebox.showerror("Error", f"Error occurred while shortening URL: {e}")

# Create a Tkinter window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x200")
window.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="blue", font=("Arial", 12))
style.map("TButton", background=[("active", "light blue")])
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Create and pack widgets
title_label = ttk.Label(window, text="URL Shortener")
title_label.pack(pady=10)

url_label = ttk.Label(window, text="Enter URL:")
url_label.pack()

url_entry = ttk.Entry(window, width=40)
url_entry.pack(pady=5)

shorten_button = ttk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=5)

result_label = ttk.Label(window, text="")
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
