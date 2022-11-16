import streamlit as st
from events import event_page 
from attendees import attendees_page
from hosts import host_page
from bills import bills_page
from supplier import supplier_page
import mariadb

conn =  mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="event_project"
) 

cursor = conn.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS HOSTS ('
    'HOST_ID INT(10) AUTO_INCREMENT NOT NULL,'
    'HOST_NAME VARCHAR(255),'
    'MOBILE_NUMBER VARCHAR(10),'
    'MAIL_ID VARCHAR(25),'
	'PRIMARY KEY (HOST_ID))'
    )

    cursor.execute('CREATE TABLE IF NOT EXISTS EVENTS('
	'EVENT_ID INT(10) AUTO_INCREMENT NOT NULL,'
    'EVENT_NAME VARCHAR(255),'
    'EVENT_TYPE VARCHAR(255),'
    'EVENT_DATE_START DATE,'
    'EVENT_DATE_END DATE,'
    'EVENT_TIME_START TIME,'
    'EVENT_TIME_END TIME,'
    'VENUE VARCHAR(255),'
    'HOST_ID INT(10),'
    'PRIMARY KEY (EVENT_ID),'
    'FOREIGN KEY (HOST_ID) REFERENCES HOSTS(HOST_ID))'
    )

    cursor.execute('CREATE TABLE IF NOT EXISTS SUPPLIER('
    'SUPPLIER_ID INT(10) AUTO_INCREMENT NOT NULL,'
    'SUPPLIER_NAME VARCHAR(255), '
    'DEPARTMENT VARCHAR(255),'
    'MAIL_ID VARCHAR(255),'
    'POINT_OF_CONTACT VARCHAR(255),'
    'MOBILE_NO VARCHAR(25),'
    'ADDRESS VARCHAR(255),'
    'PRIMARY KEY (SUPPLIER_ID))'
    )

    cursor.execute('CREATE TABLE IF NOT EXISTS BILLS('
    'BILL_ID INT(10) NOT NULL,'
    'DEALER VARCHAR(255),'
    'AMOUNT INT(10), '
    'PAYMENT_STATUS VARCHAR(25),'
    'EVENT_ID INT(10), '
    'HOST_ID INT(10), '
    'SUPPLIER_ID INT(10),'
    'PRIMARY KEY (BILL_ID),'
    'FOREIGN KEY (EVENT_ID) REFERENCES EVENTS(EVENT_ID),'
    'FOREIGN KEY (HOST_ID) REFERENCES HOSTS(HOST_ID),'
    'FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID))'
    )

    cursor.execute('CREATE TABLE IF NOT EXISTS SUPPLIED_FOR('
    'EVENT_ID INT(10),'
    'SUPPLIER_ID INT(10),' 
    'FOREIGN KEY (EVENT_ID) REFERENCES EVENTS(EVENT_ID),'
    'FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID))'
    )

    cursor.execute('CREATE TABLE IF NOT EXISTS ATTENDEES('
    'USER_ID INT(10) NOT NULL AUTO_INCREMENT, '
    'F_NAME VARCHAR(255),'
    'L_NAME VARCHAR(255),'
    'MOBILE_NUMBER INT(10),' 
    'MAIL_ID VARCHAR(255),'
    'DOB DATE, '
    'CITY VARCHAR(255),'
    'STATE VARCHAR(255),'
    'ADDRESS VARCHAR(255),' 
    'PRIMARY KEY (USER_ID))'
    )

    cursor.execute('CREATE TABLE IF NOT EXISTS ATTENDED_BY('
    'USER_ID INT(10), '
    'EVENT_ID INT(10), '
    'FOREIGN KEY (USER_ID) REFERENCES ATTENDEES(USER_ID),'
    'FOREIGN KEY (EVENT_ID) REFERENCES EVENTS(EVENT_ID))'
    )



def main():
    create_table()

    st.title("Event Management")

    table_menu = ["Attendees", "Hosts", "Events", "Bills", "Supplier"]
    table_choice = st.sidebar.selectbox("Table", table_menu)

    match table_choice:
        case "Events":
            event_page(conn, cursor)
    
        case "Attendees":
            attendees_page(conn, cursor)
    
        case "Hosts":
            host_page(conn, cursor)
    
        case "Bills":
            bills_page(conn, cursor)
    
        case "Supplier":
            supplier_page(conn, cursor)

    conn.close()

if __name__ == '__main__':
    main()