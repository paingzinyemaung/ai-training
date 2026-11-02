import gradio as gr 
import joblib
import pandas as pd

model = joblib.load('model/exam_model.joblib')

def predict(study_hours, attendance):
    if study_hours < 0:
        return "Study hours cannot be negative"
    
    if not 0 <= attendance <= 100:
        return "Attendance must be between 0 and 100"
    input_data = pd.DataFrame(
        {
            'study_hours': [study_hours],
            'attendance': [attendance]
        }
    )

    predictionResult = model.predict(input_data)

    return f"Predicted exam score: {predictionResult[0]:.2f}"

demo = gr.Interface(
    fn = predict,
    inputs = [
        gr.Number(
            label = "Study Hours",
            minimum = 0,
            value = 4
        ),
        gr.Number(
            label = "Attendance",
            minimum = 0,
            maximum = 100,
            value = 80
            )
    ],
    outputs = gr.Textbox(label = "Prediction Result"),
    title = "StudentExam Score Prediction",
    description = (
        "Enter the study hours and attendance to estimate the exam score."
    )
)

demo.launch()