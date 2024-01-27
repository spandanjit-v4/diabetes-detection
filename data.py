import streamlit as st

@st.cache_data
def eda():

    st.header("Exploratory Data Analysis")
    st.markdown("---")

    st.subheader("Training dataset datatypes")
    st.image('assets/dtypes.png')
    st.markdown("---")

    st.subheader("Training dataset features")
    st.markdown("""
                The training dataset contains 22 features. The features and their meaning are explained below:

1. `Diabetes_012`: The target column. 0 = no diabetes, 1 = prediabetes, and 2 = diabetes
2. `HighBP`: Whether the person has high blood pressure or not. 0 = no high BP, 1 = high BP
3. `HighChol`: Whether the person has high cholesterol or not. 0 = no high cholesterol, 1 = high cholesterol
4. `CholCheck`: Whether the person has taken a cholesterol check in 5 years or not. 0 = no cholesterol check in 5 years, 1 = cholesterol check in 5 years was done
5. `BMI`: Body Mass Index of a person. It is given by the formula: Weight in kgs/(Height in metres)^2
6. `Smoker`: Has the person smoked at least 100 cigarettes in their entire life? [Note: 5 packs = 100 cigarettes] 0 = no, 1 = yes
7. `Stroke`: Has the person ever been told that they had a stroke? 0 = no, 1 = yes
8. `HeartDiseaseorAttack`: Has/Is the person suffered/ing from Coronary Heart Disease (CHD) or Myocardial Infarction (MI)? 0 = no, 1 = yes
9. `PhysActivity`: Has the person performed physical activity in past 30 days - not including their job? 0 = no, 1 = yes
10. `Fruits`: Does the person consumes fruits 1 or more times per day? 0 = no, 1 = yes
11. `Veggies`: Does the person consumes vegetables 1 or more times per day? 0 = no, 1 = yes
12. `HvyAlcoholConsump`: Is the person a heavy drinker(adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)? 0 = no, 1 = yes
13. `AnyHealthcare`: Does the person have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.? 0 = no, 1 = yes
14. `NoDocbcCost`: Was there a time in the past 12 months when the person needed to see a doctor but could not because of cost? 0 = no, 1 = yes
15. `GenHlth`: Where would the person say that in general their health is in the scale of 1-5? 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor
16. `MentHlth`: In regards to mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was the person's mental health not good on a scale of scale 1-30 days?
17. `PhysHlth`: In regards to physical health, which includes physical illness and injuries, for how many days during the past 30 days was their physical health not good on a scale of 1-30 days? 
18. `DiffWalk`: Does the person have serious difficulty walking or climbing stairs? 0 = no, 1 = yes
19. `Sex`: Sex of the person. 0 = female, 1 = male
20. `Age`: The age of the person on a scale of 1-13:
    - 1 = Age 18 to 24
    - 2 = Age 25 to 29
    - 3 = Age 30 to 34
    - 4 = Age 35 to 39
    - 5 = Age 40 to 44
    - 6 = Age 45 to 49
    - 7 = Age 50 to 54
    - 8 = Age 55 to 59
    - 9 = Age 60 to 64
    - 10 = Age 65 to 69
    - 11 = Age 70 to 74
    - 12 = Age 75 to 79
    - 13 = Age 80 or older
21. `Education`: The highest grade or year of school completed by the person on a scale of 1-6:
    - 1 = Never attended school or only kindergarten 
    - 2 = Grades 1 through 8 (Elementary) 
    - 3 = Grades 9 through 11 (Some high school) 
    - 4 = Grade 12 or GED (High school graduate) 
    - 5 = College 1 year to 3 years (Some college or technical school) 
    - 6 = College 4 years or more (College graduate)
22. `Income`: The annual household income from all sources of the family on a scale of 1-8:
    - 1 = Less than $10,000
    - 2 = Less than \$15,000 (\$10,000 to less than $15,000)
    - 3 = Less than \$20,000 (\$15,000 to less than $20,000) 
    - 4 = Less than \$25,000 (\$20,000 to less than $25,000)
    - 5 = Less than \$35,000 (\$25,000 to less than $35,000) 
    - 6 = Less than \$50,000 (\$35,000 to less than $50,000)
    - 7 = Less than \$75,000 (\$50,000 to less than $75,000)
    - 8 = $75,000 or more
                """)
    st.markdown("---")

    st.subheader("Distribution of types of diabetic patients by sex")
    st.image('assets/sex_distribution.png')
    st.markdown("---")
    
    st.subheader("Distribution of types of diabetic patients by age")
    st.image('assets/age_distribution.png')