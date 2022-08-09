


import pickle
from select import select
import streamlit as st
from streamlit_option_menu import option_menu



models_path_knn = pickle.load(open("../dashboard/model_3_knn", "rb"))

st.title("Disease porrtal diagnosis")
# sidebar

with st.sidebar:
    select = option_menu("Cancer Disease Classification", 
                        ["KNN", "SVM", "Random Forest", "Logistic Regression", "Naive Bayes", "Decision Tree"],
                         )
                        

# select for model prediction

if select == "KNN":
    st.write("KNN")
    st.title("Disease prediction using Knn")
    
    
if select == "SVM":
    # model = models_path_knn["svm"]
    st.title("Disease prediction using SVM")

# if select == "Random Forest":
#     model = models_path_knn["rf"]
#     st.title("Disease prediction using Random Forest")