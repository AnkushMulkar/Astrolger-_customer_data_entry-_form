import streamlit as st
import pandas as pd

# Define the path to the Excel file
EXCEL_FILE = 'astrology_customers.xlsx'
PASSWORD = 'password123'

# Define the column names for the customer information
COLUMNS = ['Name', 'Gender', 'Birthdate', 'Birthplace', 'Birth Time', 'Address', 'City', 'State', 'Country', 'Occupation', 'Times of Visit', 'Type of Question', 'Number of Questions']

# Define a function to add a new customer to the Excel file
def add_customer(name, gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, times_of_visit, type_of_question, number_of_questions):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame(columns=COLUMNS)

    # Add the new customer to the DataFrame
    new_customer = pd.DataFrame([[name, gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, times_of_visit, type_of_question, number_of_questions]], columns=COLUMNS)
    df = pd.concat([df, new_customer], ignore_index=True)
    # Write the updated DataFrame back to the Excel file
    with pd.ExcelWriter(EXCEL_FILE) as writer:
        df.to_excel(writer, index=False)

    # Return a success message
    return f'Added customer {name} to Excel file'


# Define a function to delete an existing customer from the Excel file
def delete_customer(name):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        return 'No customer data found'

    # Remove the customer from the DataFrame
    df = df[df['Name'] != name]

    # Write the updated DataFrame back to the Excel file
    with pd.ExcelWriter(EXCEL_FILE) as writer:
        df.to_excel(writer, index=False)

    # Return a success message
    return f'Deleted customer {name} from Excel file'


# Define a function to check the password
def check_password(password):
    return password == PASSWORD


# Create the Streamlit app
st.title('Astrology Customer Information')

# Display the current contents of the Excel file
try:
    df = pd.read_excel(EXCEL_FILE)
    st.write(df)
except:
    st.write('No customer data found')

# Prompt the user to enter the password
password = st.text_input('Enter password', type='password')

# Check the password
if check_password(password):
    # Prompt the user to select an action
    action = st.selectbox('Select an action', ['Add Customer', 'Delete Customer'])
    # Check the password
if check_password(password):
    # Prompt the user to select an action
    action = st.selectbox('Select an action', ['Add Customer', 'Delete Customer'])

    # Prompt the user to enter customer information
    if action == 'Add Customer':
        name = st.text_input('Enter customer name')
        gender = st.selectbox('Select customer gender', ['Male', 'Female', 'Other'])
        birthdate = st.date_input('Enter customer birthdate')
        birthplace = st.text_input('Enter customer birthplace')
        birth_time = st.text_input('Enter customer birth time')
        address = st.text_input('Enter customer address')
        city = st.text_input('Enter customer city')
        state = st.text_input('Enter customer state')
        country = st.text_input('Enter customer country')
        occupation = st.text_input('Enter customer occupation')
        times_of_visit = st.text_input('Enter customer times of visit')
        type_of_question = st.selectbox('Select customer type of question',['Job','marriage', 'business','family related', 'Ratn','Vastushastra','career','other'])
        number_of_questions = st.number_input('Enter number of questions', value=1)
    elif action == 'Delete Customer':
        name = st.text_input('Enter the name of the customer you want to delete')
      
    # Add the new customer when the "Add Customer" button is clicked
    if action == 'Add Customer' and st.button('Add Customer'):
        message = add_customer(name, gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, times_of_visit, type_of_question, number_of_questions)
        st.write(message)
    # Delete the customer when the "Delete Customer" button is clicked
    elif action == 'Delete Customer' and st.button('Delete Customer'):
        message = delete_customer(name)
        st.write(message)

    # Prompt the user to enter customer information
    if action == 'Add Customer':
        name = st.text_input('Enter customer name')
        gender = st.selectbox('Select customer gender', ['Male', 'Female', 'Other'])
        birthdate = st.date_input('Enter customer birthdate')
        birthplace = st.text_input('Enter customer birthplace')
        birth_time = st.text_input('Enter customer birth time')
        address = st.text_input('Enter customer address')
        city = st.text_input('Enter customer city')
        state = st.text_input('Enter customer state')
        country = st.text_input('Enter customer country')
        occupation = st.text_input('Enter customer occupation')
        times_of_visit = st.text_input('Enter customer times of visit')
        type_of_question = st.selectbox('Select customer type of question',['Job','marriage', 'business','family related', 'Ratn','Vastushastra','career','other'])
        number_of_questions = st.number_input('Enter number of questions', value=1)

    # Add the new customer when the "Add Customer" button is clicked
    if st.button('Add Customer'):
        message = add_customer(name, gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, times_of_visit, type_of_question, number_of_questions)
        st.write(message)
  
    
