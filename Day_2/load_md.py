import joblib
import pandas as pd

loaded_model = joblib.load('model/model.joblib')

# print("Loaded successfully")

# unseen data
new_student = pd.DataFrame({'study_hours': [7], 'attendance': [80]})

predict = loaded_model.predict(new_student)

print('Exam Score: ', predict[0])
