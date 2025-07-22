import streamlit as st

st.title("Welcome to BMI Calculator")

# Initialize session state for form values
if 'weight' not in st.session_state:
    st.session_state.weight = 0.0
if 'height' not in st.session_state:
    st.session_state.height = 0.0
if 'status' not in st.session_state:
    st.session_state.status = 'cms'

weight = st.number_input("Enter you weight (in kgs)", value=st.session_state.weight, key="weight_input")

status = st.radio("Select you height format: ", ('cms', 'm', 'feet'), index=['cms', 'm', 'feet'].index(st.session_state.status), key="status_input")

if (status == 'cms'):
    height = st.number_input("Centimeters", value=st.session_state.height, key="height_input")

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.error("Enter some value of height")
elif(status == 'm'):
    height = st.number_input("Meters", value=st.session_state.height, key="height_input")

    try:
        bmi = weight / (height**2)
    except:
        st.error("Enter some value of height")
else:
    height = st.number_input("feet", value=st.session_state.height, key="height_input")

    try:
        bmi = weight / ((height/3.28)**2)
    except:
        st.error("Enter some value of height")

# Create columns for buttons to imporove UI
col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate BMI"):
        st.text(f"Your BMI Index is {bmi}")

        if(bmi < 16):
            st.error("You are Extremely Underweight")
        elif(bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif(bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif(bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif(bmi >= 30):
            st.error("Extremely Overweight")

with col2:
    if st.button("Reset"):
        st.session_state.weight = 0.0
        st.session_state.height = 0.0
        st.session_state.status = 'cms'
        st.rerun()
