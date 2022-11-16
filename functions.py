import streamlit as st
import pandas as pd

def view_all_attendees(cursor):
    cursor.execute('SELECT * FROM ATTENDEES')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['User ID', 'First Name', 'Last Name', 'Mobile_Number', 'Mail ID', 'DOB', 'City', 'State', 'Address'], index=['User ID'])
    return df

def view_all_hosts(cursor):
    cursor.execute('SELECT * FROM HOSTS')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Host ID', 'Host Name', 'Mobile Number', 'Mail ID'], index=['Host ID'])
    return df
    

def view_all_events(cursor):
    cursor.execute('SELECT * FROM Events')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Event ID', 'Event Name', 'Event Type', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Venue', 'Host ID'], index=['Event ID'])
    return df

def view_all_bills(cursor):
    cursor.execute('SELECT * FROM BILLS')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Bill ID', 'Dealer', 'Amount', 'Payment Status', 'Event ID', 'Host ID', 'Supplier ID'], index=['Bill ID'])
    return df

def view_all_suppliers(cursor):
    cursor.execute('SELECT * FROM Supplier')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Supplier ID', 'Supplier Name', 'Department', 'Mail ID', 'Point of Contact', 'Mobile Number', 'Address'], index=['Supplier ID'])
    return df

