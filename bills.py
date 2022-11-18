import streamlit as st
import pandas as pd 
import functions

def bills_page(conn, cursor):
    bills_menu = ["Add Bill", "View All Bills", "View Bill", "Edit Bill", "Get Pending Bills", "Remove Bill"]
    bills_choice = st.sidebar.selectbox("Menu", bills_menu)

    match bills_choice:
        case "Add Bill":
            df1 = functions.view_all_suppliers(cursor)
            list_of_Supplier =  [i for i in df1.iloc[:, 1]]
            selected_Supplier = st.selectbox("Select Supplier", list_of_Supplier)
            supplier = str(df1.loc[df1['Supplier Name'] == selected_Supplier]['Supplier ID'].values[0])

            df2 = functions.view_all_hosts(cursor)
            list_of_hosts =  [i for i in df2.iloc[:, 1]]
            selected_host = st.selectbox("Select Host", list_of_hosts)
            host_id = str(df2.loc[df2['Host Name'] == selected_host]['Host ID'].values[0])

            df3 = functions.view_all_events(cursor)
            list_of_events =  [i for i in df3.iloc[:, 1]]
            selected_event = st.selectbox("Select Event", list_of_events)
            event_id = str(df3.loc[df3['Event Name'] == selected_event]['Event ID'].values[0])

            amt = st.text_input("Amount:")

            payment_status =  ['Pending', 'Completed']
            status = st.selectbox("Payment Status", payment_status)

            if st.button("Add Bill"):
                query = ('INSERT INTO BILLS (SUPPLIER_ID, HOST_ID, EVENT_ID, AMOUNT, PAYMENT_STATUS) VALUES (%s, %s, %s, %s, %s);')
                values = (supplier, host_id, event_id, amt, status)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added Bills: {}".format(selected_event))

        case "View All Bills":
            df = functions.view_all_bills(cursor)
            st.dataframe(df)

        case "View Bill":
            df = functions.view_all_bills(cursor)
            list_of_events =  [i for i in df.iloc[:, 3]]
            list_of_events = set(list(list_of_events))
            selected_event = st.selectbox("Select Event", list_of_events)

            if st.button("View Bills"):
                st.dataframe(df.loc[df['Event Name'] == selected_event])

        case "Edit Bill":
            df = functions.view_all_bills(cursor)
            with st.expander('View all Bills'):
                st.dataframe(df)

            edit_menu = ['Select Option','Supplier Name', 'Host Name', 'Event Name', 'Amount', 'Payment Status']
            edit_choice = st.selectbox("Menu", edit_menu)

            Bill_id = st.text_input("Bill ID:")

            if edit_choice == 'Supplier Name':
                df = functions.view_all_suppliers(cursor)
                list_of_supplier =  [i for i in df.iloc[:, 1]]
                list_of_supplier.insert(0, "Select Supplier")
                selected_Supplier = st.selectbox("Select Supplier", list_of_supplier)

                if selected_Supplier != 'Select Supplier':
                    supplier = str(df.loc[df['Supplier Name'] == selected_Supplier]['Supplier ID'].values[0])
                    print("Supplier =", supplier)

                    if st.button("Update"):
                        query = ('UPDATE BILLS SET SUPPLIER_ID = %s WHERE Bill_ID = %s;')
                        values = (supplier, Bill_id)
                        cursor.execute(query, values)
                        conn.commit()
                        st.success("Successfully Updated Bill")
            
            if edit_choice == 'Host Name':
                df = functions.view_all_hosts(cursor)
                list_of_hosts =  [i for i in df.iloc[:, 2]]
                selected_host = st.selectbox("Select Host", list_of_hosts)

                host_id = str(df.loc[df['Host Name'] == selected_host]['Host ID'].values[0])

                if st.button("Update"):
                    query = ('UPDATE BILLS SET HOST_ID = %s WHERE Bill_ID = %s;')
                    values = (host_id, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

            if edit_choice == 'Event Name':
                df = functions.view_all_events(cursor)
                list_of_events =  [i for i in df.iloc[:, 3]]
                selected_event = st.selectbox("Select Event", list_of_events)

                event_id = str(df.loc[df['Event Name'] == selected_event]['Event ID'].values[0])

                if st.button("Update"):
                    query = ('UPDATE BILLS SET EVENT_ID = %s WHERE Bill_ID = %s;')
                    values = (event_id, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

            if edit_choice == 'Amount':
                amt = st.text_input("Amount:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET AMOUNT = %s WHERE BILL_ID = %s;')
                    values = (amt, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

            if edit_choice == 'Payment Status':
                status =  ['Pending', 'Completed']
                selected_status = st.selectbox("Payment Status", status)

                if st.button("Update"):
                    query = ('UPDATE BILLS SET PAYMENT_STATUS = %s WHERE BILL_ID = %s;')
                    values = (selected_status, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

        case "Remove Bill":
            df = functions.view_all_bills(cursor)
            with st.expander('View all Bills'):
                st.dataframe(df)
            
            list_of_Bills = [i for i in df.iloc[:, 0]]
            selected_Bill = st.selectbox("Select Bill ID to Delete", list_of_Bills)
            if st.button("Delete Bill"):
                cursor.execute('DELETE FROM BILLS WHERE Bill_ID={}'.format(selected_Bill))
                conn.commit()
                st.success("Bill has been deleted successfully")

        case "Get Pending Bills":
            df = functions.view_all_bills(cursor)
            event_names = [i for i in df.iloc[:, 3]]
            event_names.insert(0, "Select Event")
            e_name_choice = st.selectbox("Event Name", event_names)
            
            if (e_name_choice != "Select Event"):            
                df1 = df.loc[df["Event Name"] == e_name_choice] 
                df2 = df.loc[df["Payment Status"] == "Pending"]

                df = pd.merge(df1, df2, how='inner')

                if df.empty:
                    st.success("No Pending Bills!")
                else:
                    st.dataframe(df)
