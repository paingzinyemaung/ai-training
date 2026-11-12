import gradio as gr
import joblib

sentiment_model = joblib.load('model/sentiment_model.joblib')
category_model = joblib.load('model/category_model.joblib')

def sentiment_prediction(feedback):
    sen_prediction = sentiment_model.predict([feedback])
    return sen_prediction

def category_prediction(feedback):
    cate_prediction = category_model.predict([feedback])
    return cate_prediction

def prediction(feedback):
    sentiment = sentiment_prediction(feedback)
    category = category_prediction(feedback)
    return sentiment, category

demo = gr.Interface(
    fn = prediction,
    inputs = gr.TextArea(
        label = "Enter your feedback"
    ),
    outputs = [
        gr.Textbox(
            label = "Sentiment Prediction",
        ),
        gr.Textbox(
            label = "Category Prediction",
        )
    ],
    title = "Student Feedback Sentiment Prediction"
)

demo.launch()