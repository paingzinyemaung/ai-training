import gradio as gr
import joblib
import pandas as pd

model = joblib.load('model/classification_model.joblib')

def display(review):
    input_data = pd.DataFrame({
        'texts': [review],  
    })

    prediction = model.predict(input_data)
    return prediction[0]

demo = gr.Interface(
    fn = display,
    inputs = gr.Textbox(label = "Enter the new review"),
    outputs = gr.Textbox(label = "Classification Result"),
    title = "Classification App"
)

demo.launch()