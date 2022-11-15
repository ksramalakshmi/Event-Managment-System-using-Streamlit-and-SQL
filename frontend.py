import mysql.connector
from pathlib import Path 
import streamlit as st
import pandas as pd
from events import event_page 
from attendees import attendees_page
from hosts import host_page
from bills import bills_page
from supplier import supplier_page

conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='event_project')

sql_path = Path('tables.sql')

cursor = conn.cursor()
cursor.execute(sql_path.read_text())

st.title("Event Management")

table_menu = ["Events", "Hosts", "Attendees", "Bills", "Supplier"]
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