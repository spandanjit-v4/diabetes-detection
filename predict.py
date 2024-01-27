import streamlit as st
import pandas as pd
import numpy as np 
import joblib
import os

# Map the data to be gathered from the user to be encoded

label_dict = {"No": 0, "Yes": 1}
age_map = {'Age 18 to 24': 1,
           'Age 25 to 29': 2,
           'Age 30 to 34': 3,
           'Age 35 to 39': 4,
           'Age 40 to 44': 5,
           'Age 45 to 49': 6,
           'Age 50 to 54': 7,
           'Age 55 to 59': 8,
           'Age 60 to 64': 9,
           'Age 65 to 69': 10,
           'Age 70 to 74': 11,
           'Age 75 to 79': 12,
           'Age 80 or older': 13}
sex_map = {"Female": 0, "Male": 1}
health_map = {"Excellent": 1, "Very Good": 2, "Good": 3, "Fair": 4, "Poor": 5}
edu_map = {"Never attended school or only kindergarten": 1,
           "Grades 1 through 8 (Elementary)": 2,
           "Grades 9 through 11 (Some high school)": 3,
           "Grade 12 or GED (High school graduate)": 4,
           "College 1 year to 3 years (Some college or technical school)": 5,
           "College 4 years or more (College graduate)": 6}
income_map = {'Less than $10,000': 1,
              '\$10,000 to less than $15,000': 2,
              '\$15,000 to less than $20,000': 3,
              '\$20,000 to less than $25,000': 4,
              '\$25,000 to less than $35,000': 5,
              '\$35,000 to less than $50,000': 6,
              '\$50,000 to less than $75,000': 7,
              '\$75,000 or more': 8}
target_label_map = {"No Diabetes": 0, "Prediabetes": 1, "Diabetes": 2}

def get_fvalue(val):
    feature_dict = {"No": 0, "Yes": 1}
    for key, value in feature_dict.items():
        if val == key:
            return value
        
def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value
                
@st.cache_resource
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def diabetes_predict():

    loaded_model = load_model("models/hist5")

    st.header('Predict whether you have diabetes or not')
    st.error('Please note that this project application is created by someone to showcase their Machine Learning skills, not their medical ones. Always refer to a doctor or a trained medical professional if you\'re feeling unwell.')

    Age = st.radio("Which age group do you fall in?", 
                   ['Age 18 to 24',
                    'Age 25 to 29',
                    'Age 30 to 34',
                    'Age 35 to 39',
                    'Age 40 to 44',
                    'Age 45 to 49',
                    'Age 50 to 54',
                    'Age 55 to 59',
                    'Age 60 to 64',
                    'Age 65 to 69',
                    'Age 70 to 74',
                    'Age 75 to 79',
                    'Age 80 or older'])
    
    Sex = st.radio("What is your sex?", ['Female', 'Male'])
    HighBP = st.radio("Do you have high blood pressure?", ['Yes', 'No'])
    CholCheck = st.radio("Did you check you cholesterol in the last 5 years?", ['Yes', 'No'])
    HighChol = st.radio("Do you have high cholesterol?", ['Yes', 'No'])
    BMI = st.number_input("What is your Body Mass Index(BMI)?", 10, 100)
    Smoker = st.radio("Have you smoked at least 100 cigarettes in their entire life? [Note: 5 packs = 100 cigarettes]", ['Yes', 'No'])
    Stroke = st.radio("Have you ever been told that you had a stroke?", ['Yes', 'No'])
    HeartDiseaseorAttack = st.radio("Are you suffering/Did you suffer from Coronary Heart Disease (CHD) or Myocardial Infarction (MI)?", ['Yes', 'No'])
    PhysActivity = st.radio("Have you performed physical activity in the past 30 days, not including your job?", ['Yes', 'No'])
    Fruits = st.radio("Do you consume fruits 1 or more times per day?", ['Yes', 'No'])
    Veggies = st.radio("Do you consume vegetables 1 or more times per day?", ['Yes', 'No'])
    HvyAlcoholConsump = st.radio("Are you a heavy drinker(adult male having more than 14 drinks per week and adult female having more than 7 drinks per week)?", ['Yes', 'No'])
    DiffWalk = st.radio("Do you have serious difficulty walking or climbing stairs?", ['Yes', 'No'])
    AnyHealthcare = st.radio("Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.?", ['Yes', 'No'])
    NoDocbcCost = st.radio("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?", ['Yes', 'No'])
    GenHlth = st.select_slider("Where would you say that in general your health is in the scale of 1-5?", ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor'])
    MentHlth = st.number_input("In regards to mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good on a scale of scale 1-30 days?", 1, 30)
    PhysHlth = st.number_input("In regards to physical health, which includes physical illness and injuries, for how many days during the past 30 days was your physical health not good on a scale of 1-30 days?", 1, 30)
    
    Education = st.radio("What was the highest grade or year of school completed by you?",
                         ['Never attended school or only kindergarten',
                          'Grades 1 through 8 (Elementary)',
                          'Grades 9 through 11 (Some high school)',
                          'Grade 12 or GED (High school graduate)',
                          'College 1 year to 3 years (Some college or technical school)',
                          'College 4 years or more (College graduate)'])
    Income = st.radio("Which income group do you fall in?(Income in USD)",
                      ['Less than $10,000',
                       '\$10,000 to less than $15,000',
                       '\$15,000 to less than $20,000',
                       '\$20,000 to less than $25,000',
                       '\$25,000 to less than $35,000',
                       '\$35,000 to less than $50,000',
                       '\$50,000 to less than $75,000',
                       '\$75,000 or more'])
    
    
    result = {'HighBP': HighBP,
              'HighChol': HighChol,
              'CholCheck': CholCheck,
              'BMI': BMI,
              'Smoker': Smoker,
              'Stroke': Stroke,
              'HeartDiseaseorAttack': HeartDiseaseorAttack,
              'PhysActivity': PhysActivity,
              'Fruits': Fruits,
              'Veggies': Veggies, 
              'HvyAlcoholConsump': HvyAlcoholConsump,
              'AnyHealthcare': AnyHealthcare,
              'NoDocbcCost': NoDocbcCost,
              'GenHlth': GenHlth,
              'MentHlth': MentHlth,
              'PhysHlth': PhysHlth,
              'DiffWalk': DiffWalk,
              'Sex': Sex,
              'Age': Age,
              'Education': Education,
              'Income': Income}
    
    # Encode the data gathered from the user
    
    encoded_result = []
    for i in result.values():
            if type(i) == int:
                encoded_result.append(i)
            elif i in ['Female', 'Male']:
                res1 = get_value(i, sex_map)
                encoded_result.append(res1)
            elif i in ['Age 80 or older',
                    'Age 75 to 79',
                    'Age 70 to 74',
                    'Age 65 to 69',
                    'Age 60 to 64',
                    'Age 55 to 59',
                    'Age 50 to 54',
                    'Age 45 to 49',
                    'Age 40 to 44',
                    'Age 35 to 39',
                    'Age 30 to 34',
                    'Age 25 to 29',
                    'Age 18 to 24']:
                res2 = get_value(i, age_map)
                encoded_result.append(res2)
            elif i in ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']:
                res3 = get_value(i, health_map)
                encoded_result.append(res3)
            elif i in ['Never attended school or only kindergarten',
                    'Grades 1 through 8 (Elementary)',
                    'Grades 9 through 11 (Some high school)',
                    'Grade 12 or GED (High school graduate)',
                    'College 1 year to 3 years (Some college or technical school)',
                    'College 4 years or more (College graduate)']:
                res4 = get_value(i, edu_map)
                encoded_result.append(res4)
            elif i in ['Less than $10,000',
                    '\$10,000 to less than $15,000',
                    '\$15,000 to less than $20,000',
                    '\$20,000 to less than $25,000',
                    '\$25,000 to less than $35,000',
                    '\$35,000 to less than $50,000',
                    '\$50,000 to less than $75,000',
                    '\$75,000 or more']:
                res5 = get_value(i, income_map)
                encoded_result.append(res5)
            else:
                encoded_result.append(get_fvalue(i))

    single_sample = np.array(encoded_result).reshape(1, -1)
    pred = loaded_model.predict(single_sample)

    if pred == 0:
        st.success("You likely don't have diabetes/prediabetes.")
        st.error("This is not medical advice. Please consult a doctor, or a trained medical professional if you're feeling unwell.")
    elif pred ==1:
        st.warning("You likely have prediabetes.")
        st.error("This is not medical advice. Please consult a doctor, or a  trained medical professional if you're feeling unwell.")
    elif pred ==2:
        st.error("You likely have diabetes.")
        st.error("This is not medical advice. Please consult a doctor, or a trained medical professional if you're feeling unwell.")
