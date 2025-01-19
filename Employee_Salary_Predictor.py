import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

st.sidebar.image('salary.jpg', use_column_width=True)


# Load the trained model
with open('Employee_Salary.pkl', 'rb') as file:
    model = pickle.load(file)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Employee Salary Prediction System',
                          ['Salary Prediction'],
                          default_index=0)

# Title of the app
st.title('Employee Salary Prediction App')

job_titles = {'Software Engineer': 159,
 'Data Analyst': 17,
 'Senior Manager': 130,
 'Sales Associate': 101,
 'Director': 22,
 'Marketing Analyst': 81,
 'Product Manager': 93,
 'Sales Manager': 104,
 'Marketing Coordinator': 82,
 'Senior Scientist': 150,
 'Software Developer': 158,
 'HR Manager': 40,
 'Financial Analyst': 36,
 'Project Manager': 96,
 'Customer Service Rep': 13,
 'Operations Manager': 89,
 'Marketing Manager': 83,
 'Senior Engineer': 116,
 'Data Entry Clerk': 18,
 'Sales Director': 102,
 'Business Analyst': 3,
 'VP of Operations': 172,
 'IT Support': 44,
 'Recruiter': 98,
 'Financial Manager': 37,
 'Social Media Specialist': 157,
 'Software Manager': 160,
 'Junior Developer': 57,
 'Senior Consultant': 112,
 'Product Designer': 92,
 'CEO': 6,
 'Accountant': 1,
 'Data Scientist': 19,
 'Marketing Specialist': 84,
 'Technical Writer': 167,
 'HR Generalist': 39,
 'Project Engineer': 95,
 'Customer Success Rep': 16,
 'Sales Executive': 103,
 'UX Designer': 169,
 'Operations Director': 88,
 'Network Engineer': 85,
 'Administrative Assistant': 2,
 'Strategy Consultant': 162,
 'Copywriter': 10,
 'Account Manager': 0,
 'Director of Marketing': 29,
 'Help Desk Analyst': 41,
 'Customer Service Manager': 12,
 'Business Intelligence Analyst': 5,
 'Event Coordinator': 34,
 'VP of Finance': 171,
 'Graphic Designer': 38,
 'UX Researcher': 170,
 'Social Media Manager': 156,
 'Director of Operations': 30,
 'Senior Data Scientist': 115,
 'Junior Accountant': 47,
 'Digital Marketing Manager': 21,
 'IT Manager': 43,
 'Customer Service Representative': 14,
 'Business Development Manager': 4,
 'Senior Financial Analyst': 118,
 'Web Developer': 173,
 'Research Director': 99,
 'Technical Support Specialist': 166,
 'Creative Director': 11,
 'Senior Software Engineer': 153,
 'Human Resources Director': 42,
 'Content Marketing Manager': 9,
 'Technical Recruiter': 165,
 'Sales Representative': 106,
 'Chief Technology Officer': 8,
 'Junior Designer': 56,
 'Financial Advisor': 35,
 'Junior Account Manager': 46,
 'Senior Project Manager': 144,
 'Principal Scientist': 91,
 'Supply Chain Manager': 164,
 'Senior Marketing Manager': 134,
 'Training Specialist': 168,
 'Research Scientist': 100,
 'Junior Software Developer': 76,
 'Public Relations Manager': 97,
 'Operations Analyst': 87,
 'Product Marketing Manager': 94,
 'Senior HR Manager': 122,
 'Junior Web Developer': 80,
 'Senior Project Coordinator': 143,
 'Chief Data Officer': 7,
 'Digital Content Producer': 20,
 'IT Support Specialist': 45,
 'Senior Marketing Analyst': 131,
 'Customer Success Manager': 15,
 'Senior Graphic Designer': 120,
 'Software Project Manager': 161,
 'Supply Chain Analyst': 163,
 'Senior Business Analyst': 110,
 'Junior Marketing Analyst': 62,
 'Office Manager': 86,
 'Principal Engineer': 90,
 'Junior HR Generalist': 61,
 'Senior Product Manager': 141,
 'Junior Operations Analyst': 66,
 'Senior HR Generalist': 121,
 'Sales Operations Manager': 105,
 'Senior Software Developer': 152,
 'Junior Web Designer': 79,
 'Senior Training Specialist': 154,
 'Senior Research Scientist': 146,
 'Junior Sales Representative': 73,
 'Junior Marketing Manager': 64,
 'Junior Data Analyst': 54,
 'Senior Product Marketing Manager': 142,
 'Junior Business Analyst': 49,
 'Senior Sales Manager': 148,
 'Junior Marketing Specialist': 65,
 'Junior Project Manager': 70,
 'Senior Accountant': 109,
 'Director of Sales': 32,
 'Junior Recruiter': 71,
 'Senior Business Development Manager': 111,
 'Senior Product Designer': 139,
 'Junior Customer Support Specialist': 53,
 'Senior IT Support Specialist': 129,
 'Junior Financial Analyst': 59,
 'Senior Operations Manager': 138,
 'Director of Human Resources': 28,
 'Junior Software Engineer': 77,
 'Senior Sales Representative': 149,
 'Director of Product Management': 31,
 'Junior Copywriter': 52,
 'Senior Marketing Coordinator': 132,
 'Senior Human Resources Manager': 125,
 'Junior Business Development Associate': 50,
 'Senior Account Manager': 108,
 'Senior Researcher': 147,
 'Junior HR Coordinator': 60,
 'Director of Finance': 25,
 'Junior Marketing Coordinator': 63,
 'Junior Data Scientist': 55,
 'Senior Operations Analyst': 136,
 'Senior Human Resources Coordinator': 124,
 'Senior UX Designer': 155,
 'Junior Product Manager': 69,
 'Senior Marketing Specialist': 135,
 'Senior IT Project Manager': 128,
 'Senior Quality Assurance Analyst': 145,
 'Director of Sales and Marketing': 33,
 'Senior Account Executive': 107,
 'Director of Business Development': 23,
 'Junior Social Media Manager': 74,
 'Senior Human Resources Specialist': 126,
 'Senior Data Analyst': 113,
 'Director of Human Capital': 27,
 'Junior Advertising Coordinator': 48,
 'Junior UX Designer': 78,
 'Senior Marketing Director': 133,
 'Senior IT Consultant': 127,
 'Senior Financial Advisor': 117,
 'Junior Business Operations Analyst': 51,
 'Junior Social Media Specialist': 75,
 'Senior Product Development Manager': 140,
 'Junior Operations Manager': 68,
 'Senior Software Architect': 151,
 'Junior Research Scientist': 72,
 'Senior Financial Manager': 119,
 'Senior HR Specialist': 123,
 'Senior Data Engineer': 114,
 'Junior Operations Coordinator': 67,
 'Director of HR': 26,
 'Senior Operations Coordinator': 137,
 'Junior Financial Advisor': 58,
 'Director of Engineering': 24}

# Input fields for user data
age = st.number_input('Age', min_value=18, max_value=65)
gender = st.selectbox('Gender', ['Male', 'Female'])
education_level = st.selectbox('Education Level', ['Bachelors', 'Masters', 'PhD'])
job_title = st.selectbox('Job Title', job_titles, format_func=lambda x: x)
years_of_experience = st.number_input('Years of Experience')

# Encoding user input
gender_dict = {'Male': 1, 'Female': 0}
education_dict = {'Bachelors': 0, 'Masters': 1, 'PhD': 2}

gender_encoded = gender_dict[gender]
education_encoded = education_dict[education_level]
job_title_encoded = job_titles[job_title]

# Creating a DataFrame from the user input
input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [gender_encoded],
    'Education Level': [education_encoded],
    'Job Title': [job_title_encoded],
    'Years of Experience': [years_of_experience]
})

# Predicting the salary
if st.button('Predict Salary'):
    prediction = model.predict(input_data)[0]
    st.title('Employee Details')
    st.write(f'Age : {age}')
    st.write(f'Gender : {gender}' )
    st.write(f'Education Degree : {education_level}')
    st.write(f'Job Title : {job_title}')
    st.write(f'Year of Experience : {years_of_experience}')
    st.success(f'Employee Monthly Salary : {int( prediction )//12}')
    st.success(f'Employee Salary Package for Year : {int(prediction)}')



