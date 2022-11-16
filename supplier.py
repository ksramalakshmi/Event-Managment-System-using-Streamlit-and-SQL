import streamlit as st
import pandas as pd 
import functions

def supplier_page(conn, cursor):
    Supplier_menu = ["Add Supplier", "View All Suppliers", "View Supplier", "Edit Supplier", "Remove Supplier"]
    Supplier_choice = st.sidebar.selectbox("Menu", Supplier_menu)

    match Supplier_choice:
        case "Add Supplier":
            s_name = st.text_input("Supplier Name:")
            dept = st.text_input("Department:")
            mail_id = st.text_input("Mail ID:")
            poc_name = st.text_input("Point of Contact:")
            m_number = st.text_input("Mobile Number:")
            address = st.text_input("Address:")

            if st.button("Add Supplier"):
                query = ('INSERT INTO Supplier (SUPPLIER_NAME, DEPARTMENT, MAIL_ID, POINT_OF_CONTACT, MOBILE_NO, ADDRESS) VALUES (%s, %s, %s, %s, %s, %s);')
                values = (s_name, dept, mail_id, poc_name, m_number, address)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added Supplier: {}".format(s_name))

        case "View All Suppliers":
            df = functions.view_all_suppliers(cursor)
            st.dataframe(df)

        case "View Supplier":
            s_name = st.text_input("Supplier Name:")

            if st.button("View Supplier"):
                query = ('SELECT * FROM Suppliers WHERE SUPPLIER_NAME = %s;')
                values = (s_name)
                cursor.execute(query, values)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Supplier ID', 'Supplier Name', 'Department', 'Mail ID', 'Point of Contact', 'Mobile Number', 'Address'], index=['Supplier_ID'])
                st.dataframe(df)

        case "Edit Supplier":
            edit_menu = ['Supplier Name', 'Department', 'Mail ID', 'Point of Contact', 'Mobile Number', 'Address']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'Supplier Name':
                Supplier_id = st.text_input("Supplier ID:")
                s_name = st.text_input("Supplier Name:")

                if st.button("Update"):
                    query = ('UPDATE Supplier SET Supplier_NAME = %s WHERE Supplier_ID = %s;')
                    values = (s_name, Supplier_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Supplier")

            if edit_choice == 'Department':
                Supplier_id = st.text_input("Supplier ID:")
                dept = st.text_input("Department:")

                if st.button("Update"):
                    query = ('UPDATE Supplier SET DEPARTMENT = %s WHERE Supplier_ID = %s;')
                    values = (dept, Supplier_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Supplier")

            if edit_choice == 'Mail ID':
                Supplier_id = st.text_input("Supplier ID:")
                mail_id = st.text_input("Mail ID")

                if st.button("Update"):
                    query = ('UPDATE Supplier SET MAIL_ID = %s WHERE Supplier_ID = %s;')
                    values = (mail_id, Supplier_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Supplier")

            if edit_choice == 'Point of Contact':
                Supplier_id = st.text_input("Supplier ID:")
                poc = st.text_input("Point of Contact")

                if st.button("Update"):
                    query = ('UPDATE Supplier SET POINT_OF_CONTACT = %s WHERE Supplier_ID = %s;')
                    values = (poc, Supplier_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Supplier")
            
            if edit_choice == 'Mobile Number':
                Supplier_id = st.text_input("Supplier ID:")
                m_number = st.text_input("Mobile Number:")

                if st.button("Update"):
                    query = ('UPDATE Supplier SET MOBILE_NO = %s WHERE Supplier_ID = %s;')
                    values = (m_number, Supplier_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Supplier")
            
            if edit_choice == 'Address':
                Supplier_id = st.text_input("Supplier ID:")
                address = st.text_input("Address:")

                if st.button("Update"):
                    query = ('UPDATE Supplier SET ADDRESS = %s WHERE Supplier_ID = %s;')
                    values = (address, Supplier_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Supplier")

        case "Remove Supplier": 
            df = functions.view_all_suppliers(cursor)
            with st.expander('View all Suppliers'):
                st.dataframe(df)
            
            list_of_Supplier =  [i for i in df.iloc[:, 0]]
            selected_Supplier = st.selectbox("Select Supplier ID to Delete", list_of_Supplier)
            if st.button("Delete Supplier"):
                cursor.execute('DELETE FROM Supplier WHERE Supplier_ID={}'.format(selected_Supplier['Supplier_ID']))
                conn.commit()
                st.success("Supplier has been deleted successfully")
