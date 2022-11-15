import mysql.connector
import streamlit as st
import pandas as pd

def view_all_events(cursor):
    cursor.execute('SELECT * FROM Events')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Event_ID', 'Event Name', 'Event Type', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Venue', 'Host ID'], index=['Event_ID'])
    return df

def view_all_bills(cursor):
    cursor.execute('SELECT * FROM BILLS')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Bill ID', 'Dealer', 'Amount', 'Payment Status', 'Event ID', 'Host ID', 'Supplier ID'], index=['Bill_ID'])
    return df

def view_all_suppliers(cursor):
    cursor.execute('SELECT * FROM Supplier')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Supplier ID', 'Supplier Name', 'Department', 'Mail ID', 'Point of Contact', 'Mobile Number', 'Address'], index=['Supplier_ID'])
    return df

