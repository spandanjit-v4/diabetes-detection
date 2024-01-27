import streamlit as st 
import streamlit.components.v1 as stc 
from streamlit_option_menu import option_menu
from home import home
from data import eda
from model import model
from predict import diabetes_predict

st.set_page_config(page_title = "GlucoMatrice",
				   page_icon = ":chocolate_bar:",
                   layout = "wide",
                   initial_sidebar_state = "expanded")

def main():

	with st.sidebar:
		choice = option_menu(None, 
					   		['Home', 'Data Analysis', 'Model Analysis', 'Predict Diabetes'], 
							icons = ['house', 'graph-up', 'robot', 'clipboard2-pulse'], 
							menu_icon = 'list', 
							default_index = 0)

	
	if choice == "Home":
		home()
	elif choice == "Data Analysis":
		eda()
	elif choice == "Model Analysis":
		model()
	elif choice == "Predict Diabetes":
		diabetes_predict()

if __name__ == '__main__':
	main()