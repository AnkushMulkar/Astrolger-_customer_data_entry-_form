import streamlit as st
import pandas as pd

# Define the path to the Excel file
EXCEL_FILE = 'astrology_customers.xlsx'
PASSWORD = 'password123'

# Define the column names for the customer information
COLUMNS = ['Name','Date of visit','Time of visit','Number of Visits','New/Old customer','Gender', 'Birthdate', 'Birthplace', 'Birth Time', 'Address', 'City', 'State', 'Country', 'Occupation', 'Type of Question', 'Number of Questions','Fees per question','Total Amount']

# Define a function to add a new customer to the Excel file
def add_customer(name,date_visit,time_visit,number_visit,new_old_customer,gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, type_of_question, number_of_questions,fees_per_question,total_amount):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame(columns=COLUMNS)

    # Add the new customer to the DataFrame
    new_customer = pd.DataFrame([[name,date_visit,time_visit,number_visit,new_old_customer,gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, type_of_question, number_of_questions,fees_per_question,total_amount]], columns=COLUMNS)
    df = df.append(new_customer, ignore_index=True)

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

    # Prompt the user to enter customer information
    if action == 'Add Customer':
        name = st.text_input('Enter Customer Name')
        date_visit = st.date_input('Enter Date of visit', key='date_visit')
        time_visit = st.text_input('Enter visit time', key='time_visit')
        number_visit = st.text_input('Enter Number of visits')
        new_old_customer = st.selectbox('Select New/Old customer', ['New','Old'])
        gender = st.selectbox('Select customer Gender', ['Male', 'Female', 'Other'])
        birthdate = st.date_input('Enter customer Birthdate', key='birthdate')
        birthplace = st.text_input('Enter customer Birthplace')
        birth_time = st.text_input('Enter customer Birth time', key='birth_time')
        address = st.text_input('Enter customer Address')
        city = st.text_input('Enter customer City')
        state = st.text_input('Enter customer State')
        country = st.text_input('Enter customer country')
        occupation = st.text_input('Enter customer Occupation')
        type_of_question = st.selectbox('Select customer Type of question',['Job','marriage', 'business','family related', 'Ratn','Vastushastra','career'])
        number_of_questions = st.number_input('Enter Number of Questions', value=1)
        fees_per_question = st.selectbox('Select Fees', ['100','200','300','400','500','600','700','800','900','1000','1500','2000','2500','3000'])
        total_amount = int(number_of_questions) * int(fees_per_question)

    # Add the new customer when the "Add Customer" button is clicked
    if st.button('Add Customer'):
        message = add_customer(name,date_visit,time_visit,number_visit,new_old_customer,gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, type_of_question, number_of_questions,fees_per_question,total_amount)
        st.write(message)
        
    if action == 'Delete Customer':
        name = st.text_input('Enter customer name')
        
    # Delete the customer when the "Delete Customer" button is clicked
    if st.button('Delete Customer'):
        message = delete_customer(name,date_visit,time_visit,number_visit,new_old_customer,gender, birthdate, birthplace, birth_time, address, city, state, country, occupation, type_of_question, number_of_questions,fees_per_question,total_amount)
        st.write(message)

