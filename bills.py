import streamlit as st
import pandas as pd 
import functions

def bills_page(conn, cursor):
    bills_menu = ["Add Bill", "View All Bills", "View Bill", "Edit Bill", "Remove Bill"]
    bills_choice = st.sidebar.selectbox("Menu", bills_menu)

    match bills_choice:
        case "Add Bills":
            bill_id = st.text_input("Bill ID")
            dealer = st.text_input("Dealer:")
            amt = st.text_input("Amount:")
            status = st.text_input("Payment Status:")
            event_id = st.text_input("Event ID:")
            host_id = st.text_input("Host ID:")
            supplier = st.text_input("Supplier ID:")

            if st.button("Add Bill"):
                query = ('INSERT INTO BILLS (BILL_ID, DEALER, AMOUNT, PAYMENT_STATUS, EVENT_ID, HOST_ID, SUPPLIER_ID) VALUES (%s, %s, %s, %s, %s, %s, %s);')
                values = (bill_id, dealer, amt, status, event_id, host_id, supplier)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added Bills: {}".format(dealer))

        case "View All Bills":
            df = functions.view_all_bills(cursor)
            st.dataframe(df)

        case "View Bill":
            dealer = st.text_input("Dealer:")

            if st.button("View Bills"):
                query = ('SELECT * FROM BILLS WHERE DEALER = %s;')
                values = (dealer)
                cursor.execute(query, values)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Bill ID', 'Dealer', 'Amount', 'Payment Status', 'Event ID', 'Host ID', 'Supplier ID'], index=['Bill_ID'])
                st.dataframe(df)

        case "Edit Bill":
            edit_menu = ['Dealer', 'Amount', 'Payment Status', 'Event ID', 'Host ID', 'Supplier ID']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'Dealer':
                Bill_id = st.text_input("Bill ID:")
                dealer = st.text_input("Dealer:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET DEALER = %s WHERE Bill_ID = %s;')
                    values = (dealer, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

            if edit_choice == 'Amount':
                Bill_id = st.text_input("Bill ID:")
                amt = st.text_input("Amount:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET AMOUNT = %s WHERE BILL_ID = %s;')
                    values = (amt, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

            if edit_choice == 'Payment Status':
                Bill_id = st.text_input("Bill ID:")
                status = st.text_input("Payment Status:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET PAYMENT_STATUS = %s WHERE BILL_ID = %s;')
                    values = (status, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")
            
            if edit_choice == 'Event ID':
                Bill_id = st.text_input("Bill ID:")
                event_id = st.text_input("Event ID:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET EVENT_ID = %s WHERE BILL_ID = %s;')
                    values = (event_id, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")
            
            if edit_choice == 'Host ID':
                Bill_id = st.text_input("Bill ID:")
                host_id = st.text_input("Host ID:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET HOST_ID = %s WHERE BILL_ID = %s;')
                    values = (host_id, Bill_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Bill")

            if edit_choice == 'Supplier ID':
                Bill_id = st.text_input("Bill ID:")
                supplier = st.text_input("Supplier ID:")

                if st.button("Update"):
                    query = ('UPDATE BILLS SET SUPPLIER_ID = %s WHERE BILL_ID = %s;')
                    values = (supplier, Bill_id)
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
                cursor.execute('DELETE FROM BILL WHERE Bill_ID={}'.format(selected_Bill))
                conn.commit()
                st.success("Bill has been deleted successfully")
