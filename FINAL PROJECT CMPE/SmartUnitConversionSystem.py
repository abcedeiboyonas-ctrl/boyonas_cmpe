# ======================================
# Smart Unit Conversion System

import tkinter as tk

# UNIT DICTIONARIES (BASE UNITS)
# ======================================

# Length
length_units = {
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001
}

# Mass
mass_units = {
    "kg": 1000,
    "hg": 100,
    "dag": 10,
    "g": 1,
    "dg": 0.1,
    "cg": 0.01,
    "mg": 0.001
}

# Volume
volume_units = {
    "kl": 1000,
    "hl": 100,
    "dal": 10,
    "l": 1,
    "dl": 0.1,
    "cl": 0.01,
    "ml": 0.001
}

# Temperature units
temperature_units = {"c", "f", "k"}

# Conversion history
history = []



def detect_unit_type(unit):
    if unit in length_units:
        return "Length"
    elif unit in mass_units:
        return "Mass"
    elif unit in volume_units:
        return "Volume"
    elif unit in temperature_units:
        return "Temperature"
    else:
        return None


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius
    if from_unit == "f":
        value = (value - 32) * 5 / 9
    elif from_unit == "k":
        value -= 273.15

    # Convert from Celsius
    if to_unit == "f":
        return (value * 9 / 5) + 32
    elif to_unit == "k":
        return value + 273.15
    else:
        return value



# CONVERSION LOGI

def convert():
    user_input = entry.get().lower().strip()
    parts = user_input.split()

    if len(parts) != 4 or parts[2] != "to":
        result_label.config(text="Format: value unit to unit")
        return

    value_text, from_unit, _, to_unit = parts

    if not value_text.replace(".", "", 1).isdigit():
        result_label.config(text="Value must be numeric")
        return

    value = float(value_text)

    from_type = detect_unit_type(from_unit)
    to_type = detect_unit_type(to_unit)

    if from_type is None or to_type is None:
        result_label.config(text="Unsupported unit")
        return

    if from_type != to_type:
        result_label.config(text="Units must be same type")
        return

    # Perform conversion
    if from_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    else:
        if from_type == "Length":
            base = value * length_units[from_unit]
            result = base / length_units[to_unit]

        elif from_type == "Mass":
            base = value * mass_units[from_unit]
            result = base / mass_units[to_unit]

        elif from_type == "Volume":
            base = value * volume_units[from_unit]
            result = base / volume_units[to_unit]

    result = round(result, 6)
    output = f"{result} {to_unit}"

    result_label.config(text=f"Result: {output}")

    history.append(f"{value} {from_unit} → {output}")
    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)



# GUI SETUP USING TKINTER


window = tk.Tk()
window.title("Smart Metric Unit Converter")
window.geometry("460x520")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Smart Unit Conversion System",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

instructions = tk.Label(
    window,
    text="Format: value unit to unit\nExample: 500 g to kg | 2 l to ml | 30 c to f",
    font=("Arial", 9)
)
instructions.pack()

entry = tk.Entry(window, width=32, font=("Arial", 12))
entry.pack(pady=10)
entry.insert(0, "100 g to kg")

convert_btn = tk.Button(window, text="Convert", width=18, command=convert)
convert_btn.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 11))
result_label.pack(pady=10)

history_label = tk.Label(window, text="Conversion History")
history_label.pack()

history_box = tk.Listbox(window, width=52, height=10)
history_box.pack(pady=5)

exit_btn = tk.Button(window, text="Exit", width=18, command=window.destroy)
exit_btn.pack(pady=10)

window.mainloop()

#DONEDDDDDD
