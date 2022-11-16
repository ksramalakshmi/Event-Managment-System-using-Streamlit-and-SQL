import streamlit as st
import pandas as pd 
import functions

def attendees_page(conn, cursor):
    user_menu = ["Add User", "View All Users", "View User", "Edit User", "Remove User"]
    user_choice = st.sidebar.selectbox("Menu", user_menu)

    match user_choice:
        case "Add User":
            f_name = st.text_input("First Name:")
            l_name = st.text_input("Last Name:")
            num = st.text_input("Mobile Number:")
            mail_id = st.text_input("Mail ID:")
            dob = st.date_input("Date of Birth:")
            city = st.text_input("City:")
            state = st.text_input("State:")
            address = st.text_input('Address:')


            if st.button("Add User"):
                query = ('INSERT INTO ATTENDEES (F_NAME, L_NAME, MOBILE_NUMBER, MAIL_ID, DOB, CITY, STATE, ADDRESS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);')
                values = (f_name, l_name, num, mail_id, dob, city, state, address)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added User: {}".format(f_name+" "+l_name))

        case "View All Users":
            df = functions.view_all_attendees(cursor)
            st.dataframe(df)

        case "View User":
            f_name = st.text_input("First Name:")
            l_name = st.text_input("Last Name:")

            if st.button("View User"):
                query = ('SELECT * FROM ATTENDEES WHERE F_NAME = %s || L_NAME = %s;')
                values = (f_name, l_name)
                cursor.execute(query, values)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=["User ID", "First Name", "Last Name", "Mobile Number", "Mail ID", "Date of Birth", "City", "State", "Address"], index=['User_ID'])
                st.dataframe(df)

        case "Edit User":
            edit_menu = ["First Name", "Last Name", "Mobile Number", "Mail ID", "Date of Birth", "City", "State", "Address"]
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'First Name':
                user_id = st.text_input("User ID:")
                f_name = st.text_input("First Name:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET F_NAME = %s WHERE USER_ID = %s;')
                    values = (f_name, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'Last Name':
                user_id = st.text_input("User ID:")
                l_name = st.text_input("Last Name:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET L_NAME = %s WHERE USER_ID = %s;')
                    values = (l_name, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")

            if edit_choice == 'Mobile Number':
                user_id = st.text_input("User ID:")
                m_number = st.text_input("Mobile Number:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET MOBILE_NUMBER = %s WHERE USER_ID = %s;')
                    values = (m_number, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")

            if edit_choice == 'Mail ID':
                user_id = st.text_input("User ID:")
                mail_id = st.text_input("Mail ID:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET MAIL_ID = %s WHERE USER_ID = %s;')
                    values = (mail_id, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'Date of Birth':
                user_id = st.text_input("User ID:")
                dob = st.date_input("Date of Birth:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET DOB = %s WHERE USER_ID = %s;')
                    values = (dob, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")

            if edit_choice == 'City':
                user_id = st.text_input("User ID:")
                city = st.text_input("City:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET CITY = %s WHERE USER_ID = %s;')
                    values = (city, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'State':
                user_id = st.text_input("User ID:")
                state = st.text_input("State:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET STATE = %s WHERE USER_ID = %s;')
                    values = (state, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
            
            if edit_choice == 'Address':
                user_id = st.text_input("User ID:")
                address = st.text_input("Address:")

                if st.button("Update"):
                    query = ('UPDATE ATTENDEES SET ADDRESS = %s WHERE USER_ID = %s;')
                    values = (address, user_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated User")
        
        case "Remove User":
            df = functions.view_all_attendees(cursor)
            with st.expander('View all Users'):
                st.dataframe(df)
            
            list_of_users = [i for i in df.iloc[:, 0]]
            selected_user = st.selectbox("Select User ID to Delete", list_of_users)
            if st.button("Delete User"):
                cursor.execute('DELETE FROM ATTENDEES WHERE USER_ID={};'.format(selected_user))
                cursor.execute('ALTER TABLE ATTENDEES AUTO_INCREMENT=1')
                conn.commit()
                st.success("User has been deleted successfully")

