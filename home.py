import streamlit as st

@st.cache_data
def home():
    st.header("Home")
    st.markdown("This is a sample project by Spandanjit Mondal(Hi!) to showcase their Machine Learning skills. It predicts whether a person has diabetes, prediabetes, or none of those, based on certain parameters. The ML model is trained on a cleaned and consolidated dataset of the [BRFSS 2015 Codebook](https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf) by Alex Teboul on [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset).")
    st.write("""The app has 4 sections: \n
- This homepage \n
- A section on Exploratory Data Analysis \n
- A section analysing the models I tried and trained \n
- A section to predict whether you have diabetes or not""")
    st.error('Please note that this project application is created by someone to showcase their Machine Learning skills, not their medical ones. Always refer to a doctor or a trained medical professional if you\'re feeling unwell.')
