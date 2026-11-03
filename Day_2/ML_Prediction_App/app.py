# import gradio as gr 
# import joblib
# import pandas as pd

# # load the model
# model = joblib.load('model/tiktok_model.joblib')

# # prediction fun
# def predict_views(video_like_count, video_comment_count, video_share_count, video_download_count, video_duration_sec):
#     input_data = pd.DataFrame(
#         {
#             'video_like_count': [video_like_count],
#             'video_comment_count': [video_comment_count],
#             'video_share_count': [video_share_count],
#             'video_download_count': [video_download_count],
#             'video_duration_sec': [video_duration_sec]     
#         }
#     )

#     prediction = model.predict(input_data)
#     return round(prediction[0], 2)

# # gradio interface
# demo = gr.Interface(
#     fn = predict_views,
#     inputs = [
#         gr.Number(label = "Video Like Count", value = 1000),
#         gr.Number(label = "Video Comment Count", value = 100),
#         gr.Number(label = "Video Share Count", value = 200),
#         gr.Number(label = "Video Download Count", value = 50),
#         gr.Number(label = "Video Duration (sec)", value = 30)
#     ],
#     outputs = gr.Number(label = "Predicted Video View Count"),
#     title = "Tiktok Video View Count Prediction App",
#     description = "Prediction of views by entering the values of Likes, Comments Shares, Downloads and Duration"
# )

# demo.launch()

import gradio as gr 
import joblib
import pandas as pd

# load the model
model = joblib.load('model/wine_model.joblib')

def predict_wine_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
    input_data = pd.DataFrame({
        'fixed acidity': [fixed_acidity],
        'volatile acidity': [volatile_acidity],
        'citric acid': [citric_acid],
        'residual sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free sulfur dioxide': [free_sulfur_dioxide],
        'total sulfur dioxide': [total_sulfur_dioxide],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol]
    })

    prediction = model.predict(input_data)
    return round(prediction[0], 2)

demo = gr.Interface(
    fn = predict_wine_quality,
    inputs=[
        gr.Number(label="Fixed Acidity", value=7.0),
        gr.Number(label="Volatile Acidity", value=0.27),
        gr.Number(label="Citric Acid", value=0.36),
        gr.Number(label="Residual Sugar", value=20.7),
        gr.Number(label="Chlorides", value=0.045),
        gr.Number(label="Free Sulfur Dioxide", value=45.0),
        gr.Number(label="Total Sulfur Dioxide", value=170.0),
        gr.Number(label="Density", value=1.001),
        gr.Number(label="pH", value=3.0),
        gr.Number(label="Sulphates", value=0.45),
        gr.Number(label="Alcohol", value=8.8)
    ],
    outputs = gr.Number(label = "Predicted Wine Quality Score"),
    title = "Wine Quality Prediction App",
    description = "Prediction of wine quality by entering the values of wines' chemical data"
)

demo.launch()