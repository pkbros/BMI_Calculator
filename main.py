import streamlit as st

st.title("Welcome to BMI Calculator")

weight = st.number_input("Enter you weight (in kgs)")

status = st.radio("Select you height format: ", ('cms', 'm', 'feet'))

if (status == 'cms'):
    height = st.number_input("Centimeters")

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.error("Enter some value of height")
elif(status == 'm'):
    height = st.number_input("Meters")

    try:
        bmi = weight / (height**2)
    except:
        st.error("Enter some value of height")
else:
    height = st.number_input("feet")

    try:
        bmi = weight / ((height/3.28)**2)
    except:
        st.error("Enter some value of height")

if(st.button("Calculate BMI")):
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