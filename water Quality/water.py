import tkinter as tk
from tkinter import ttk
import pickle


def predict(pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    with open('water_model.pkl', 'rb') as file:
        model = pickle.load(file)
    dict1 = {
            1 : 'Safe to drink',
            0 : 'Unsafe to drink'
        }

    input_data = [[pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]]
    result = model.predict(input_data)
    return dict1[result[0]]

def on_predict():
    try:
        # Get input values
        ph_val = float(ph_entry.get())
        hardness_val = float(hardness_entry.get())
        solids_val = float(solids_entry.get())
        chloramines_val = float(chloramines_entry.get())
        sulfate_val = float(sulfate_entry.get())
        conductivity_val = float(conductivity_entry.get())
        organic_carbon_val = float(organic_carbon_entry.get())
        trihalomethanes_val = float(trihalomethanes_entry.get())
        turbidity_val = float(turbidity_entry.get())

        # Make prediction
        prediction = predict(ph_val, hardness_val, solids_val, chloramines_val, sulfate_val,
                             conductivity_val, organic_carbon_val, trihalomethanes_val, turbidity_val)

        # Display the result
        result_label.config(text=f"Prediction: {prediction}")
    except ValueError:
        result_label.config(text="Please enter valid numerical values")

# Create main window
root = tk.Tk()
root.title("Water Quality Prediction App")

# Create and place input labels and entry widgets
labels = ["pH", "Hardness", "Solids", "Chloramines", "Sulfate", "Conductivity", "Organic Carbon", "Trihalomethanes", "Turbidity"]
entries = []

for i, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entry = ttk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Create "Predict" button
predict_button = ttk.Button(root, text="Predict", command=on_predict)
predict_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Create label to display prediction result
result_label = ttk.Label(root, text="")
result_label.grid(row=len(labels) + 1, column=0, columnspan=2, pady=5)

# Start the main loop
root.mainloop()
