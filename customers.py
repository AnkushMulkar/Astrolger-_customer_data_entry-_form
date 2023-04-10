import streamlit as st
import pandas as pd

# Define the path to the Excel file
EXCEL_FILE = 'astrology_customers.xlsx'
PASSWORD = 'password123'

# Define the column names for the customer information
COLUMNS = ['Name','Date of Visit', 'Times of Visit','New/Old Customer', 'Gender', 'Birthdate', 'Birthplace', 'Birth Time', 'Address', 'City', 'State', 'Country', 'Occupation', 'Type of Question', 'Number of Questions','Fees per Question' ,'Total Amount']

# Define a function to add a new customer to the Excel file
def add_customer(Name,Date of Visit, Times of Visit ,New/Old Customer, Gender, Birthdate, Birthplace, Birth Time, Address, City, State, Country, Occupation, Type of Question, Number of Questions,Fees per Question ,Total Amount):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        df = pd.DataFrame(columns=COLUMNS)

    # Add the new customer to the DataFrame
    new_customer = pd.DataFrame([[Name,Date of Visit, Times of Visit,New/Old Customer, Gender, Birthdate, Birthplace, Birth Time, Address, City, State, Country, Occupation, Type of Question, Number of Questions,Fees per Question ,Total Amount]], columns=COLUMNS)
    df = df.append(new_customer, ignore_index=True)

    # Write the updated DataFrame back to the Excel file
    with pd.ExcelWriter(EXCEL_FILE) as writer:
        df.to_excel(writer, index=False)

    # Return a success message
    return f'Added customer {Name} to Excel file'


# Define a function to delete an existing customer from the Excel file
def delete_customer(Name):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(EXCEL_FILE)
    except:
        return 'No customer data found'

    # Remove the customer from the DataFrame
    df = df[df['Name'] != Name]

    # Write the updated DataFrame back to the Excel file
    with pd.ExcelWriter(EXCEL_FILE) as writer:
        df.to_excel(writer, index=False)

    # Return a success message
    return f'Deleted customer {Name} from Excel file'


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
        Name = st.text_input('Enter customer name')
        Date of Visit = st.date_input('Enter customer Date of Visit')
        Timee of Visit = st.time_input('Enter customer Time of Visit')
        New/Old Customer = st.selectbox('Select', ['New' , 'Old'])
        Gender = st.selectbox('Select customer gender', ['Male', 'Female', 'Other'])
        Birthdate = st.date_input('Enter customer birthdate')
        Birthplace = st.text_input('Enter customer birthplace')
        Birth_time = st.text_input('Enter customer birth time')
        Address = st.text_input('Enter customer address')
        City = st.text_input('Enter customer city')
        State = st.text_input('Enter customer state')
        Country = st.text_input('Enter customer country')
        Occupation = st.text_input('Enter customer occupation')
        Type_of_question = st.selectbox('Select customer type of question',['Job','marriage', 'business','family related', 'Ratn','Vastushastra','career'])
        Number_of_questions = st.number_input('Enter number of questions', value=1)
        Fees per Question = st.selectbox('Select', ['100','200','300', '400','500','1000','1500','2000'])
        Total Amount = int(number_of_questions) * int(Fees per Question)

    # Add the new customer when the "Add Customer" button is clicked
    if st.button('Add Customer'):
        message = add_customer(Name,Date of Visit, Timee of Visit , Gender, Birthdate, Birthplace, Birth Time, Address, City, State, Country, Occupation, Type of Question, Number of Questions,Fees per Question ,Total Amount)
        st.write(message)
        
    if action == 'Delete Customer':
        name = st.text_input('Enter customer Name')
       

    # Add the new customer when the "Add Customer" button is clicked
    if st.button('Delete Customer'):
        message = delete_customer(Name)
        st.write(message)    
