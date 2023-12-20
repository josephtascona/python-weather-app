import requests
from dotenv import load_dotenv
load_dotenv()
import os
import tkinter as tk

def get_weather(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    data = response.json()
    # Parse and print relevant data
    temperature = data['current']['temperature']
    return f"Current temperature in {city} is: {temperature}°C"

def update_text_box():
    city = input_box.get()
    text_box.config(state='normal')
    text_box.delete("1.0", tk.END)
    try:
        text_box.insert(tk.END, get_weather(city))
    except KeyError:
        text_box.insert(tk.END, "Invalid City")
    text_box.config(state='disabled')
    input_box.delete(0, tk.END)  # Clear the input box

if __name__ == "__main__":
    # Create a tkinter window
    window = tk.Tk()
    window.title("Weather App")

    # Create a Text widget
    text_box = tk.Text(window, height=10, width=40)
    text_box.config(state='disabled')
    text_box.pack()

    input_box = tk.Entry(window, width=40)
    input_box.pack()

    get_weather_button = tk.Button(window, text="Get Weather", command=update_text_box)
    get_weather_button.pack()

    # Start the tkinter main loop
    window.mainloop()
