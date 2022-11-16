import streamlit as st
import pandas as pd 
import functions

def host_page(conn, cursor):
    Host_menu = ["Add Host", "View All Hosts", "View Host", "Edit Host", "Remove Host"]
    Host_choice = st.sidebar.selectbox("Menu", Host_menu)

    match Host_choice:
        case "Add Host":
            h_name = st.text_input("Host Name:")
            num = st.text_input("Mobile Number:")
            mail_id = st.text_input("Mail ID:")

            if st.button("Add Host"):
                query = ('INSERT INTO HOSTS (HOST_NAME, MOBILE_NUMBER, MAIL_ID) VALUES (%s, %s, %s);')
                values = (h_name, num, mail_id)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added Host: {}".format(h_name))

        case "View All Hosts":
            df = functions.view_all_hosts(cursor)
            st.dataframe(df)

        case "View Host":
            h_name = st.text_input("Host Name:")

            if st.button("View Host"):
                query = ('SELECT * FROM HOSTS WHERE H_NAME = %s;')
                values = (h_name)
                cursor.execute(query, values)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Host ID', 'Host Name', 'Mobile_Number', 'Mail_ID'], index=['Host ID'])
                st.dataframe(df)

        case "Edit Host":
            edit_menu = ['Host Name', 'Mobile Number', 'Mail ID']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'Host Name':
                Host_id = st.text_input("Host ID:")
                h_name = st.text_input("Host Name:")

                if st.button("Update"):
                    query = ('UPDATE HOSTS SET HOST_NAME = %s WHERE Host_ID = %s;')
                    values = (h_name, Host_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Host")

            if edit_choice == 'Mobile Number':
                Host_id = st.text_input("Host ID:")
                m_number = st.text_input("Mobile Number:")

                if st.button("Update"):
                    query = ('UPDATE HOSTS SET MOBILE_NUMBER = %s WHERE Host_ID = %s;')
                    values = (m_number, Host_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Host")

            if edit_choice == 'Mail ID':
                Host_id = st.text_input("Host ID:")
                mail_id = st.text_input("Mail ID:")

                if st.button("Update"):
                    query = ('UPDATE HOSTS SET MAIL_ID = %s WHERE Host_ID = %s;')
                    values = (mail_id, Host_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Host")
            
        case "Remove Host":
            df = functions.view_all_hosts(cursor)
            with st.expander('View all Hosts'):
                st.dataframe(df)
            
            list_of_Hosts =  [i for i in df.iloc[:, 0]]
            selected_Host = st.selectbox("Select Host ID to Delete", list_of_Hosts)
            if st.button("Delete Host"):
                st.warning("Do you want to delete ::{}".format(list_of_Hosts))
                cursor.execute('DELETE FROM HOSTS WHERE Host_ID="{}"'.format(selected_Host))
                conn.commit()
                st.success("Host has been deleted successfully")
