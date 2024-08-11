import streamlit as st

# Give a title to our app
st.title('Welcome to BMI Calculator')
st.subheader("[Introduced By TSK]")

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0, step=0.1)

# TAKE HEIGHT INPUT
# Radio button to choose height format
status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

# Initialize bmi
bmi = None

# Compare status value
if status == 'cms':
    # Take height input in centimeters
    height = st.number_input('Enter your height (in cms)', min_value=0.0, step=0.1)
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

elif status == 'meters':
    # Take height input in meters
    height = st.number_input('Enter your height (in meters)', min_value=0.0, step=0.1)
    if height > 0:
        bmi = weight / (height ** 2)

else:
    # Take height input in feet
    height = st.number_input('Enter your height (in feet)', min_value=0.0, step=0.1)
    if height > 0:
        # 1 meter = 3.28 feet
        bmi = weight / (((height / 3.28)) ** 2)

# Check if the button is pressed or not
if st.button('Calculate BMI'):

    if bmi:
        # Print the BMI INDEX
        st.markdown(f"**Your BMI Index is _{bmi:.2f}_.**")

        # Interpretation and Recommendations
        st.markdown("### <span style='color:blue'>Recommendations for Better Health:</span>", unsafe_allow_html=True)
        if bmi < 16:
            st.error("You are Extremely Underweight")
            st.markdown("""
                - **Consult a Healthcare Provider**: Discuss underlying causes and create a weight-gain plan.
                - **Balanced Diet**: Focus on calorie-rich, nutrient-dense foods.
                - **Strength Training**: Engage in exercises to build muscle mass.
            """)
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
            st.markdown("""
                - **Dietitian Guidance**: Seek help for healthy weight gain.
                - **Nutrient-Dense Foods**: Prioritize foods high in calories and nutrients.
                - **Muscle Building**: Incorporate strength training.
            """)
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
            st.markdown("""
                - **Maintain Lifestyle**: Continue balanced diet and regular exercise.
                - **Regular Check-Ups**: Monitor health through periodic medical check-ups.
            """)
        elif 25 <= bmi < 30:
            st.warning("Overweight")
            st.markdown("""
                - **Increase Physical Activity**: Include more exercise in your routine.
                - **Healthy Diet**: Focus on fruits, vegetables, and lean proteins.
                - **Calorie Control**: Watch calorie intake to aid weight loss.
            """)
        elif bmi >= 30:
            st.error("Extremely Overweight")
            st.markdown("""
                - **Professional Help**: Consult healthcare providers for guidance.
                - **Diet and Exercise**: Adopt a healthier diet and increase physical activity.
                - **Support System**: Seek support from professionals or groups.
            """)
    else:
        st.text("Please enter a valid height and weight.")
