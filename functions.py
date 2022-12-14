import streamlit as st
import pandas as pd

def view_all_attendees_events(cursor):
    cursor.execute('SELECT EVENT_ID, EVENT_NAME, USER_ID, F_NAME, L_NAME FROM (ATTENDED_BY NATURAL JOIN ATTENDEES NATURAL JOIN EVENTS)')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Event ID', 'Event Name', 'User ID', 'First Name', 'Last Name'])
    return df

def view_all_attendees(cursor):
    cursor.execute('SELECT * FROM ATTENDEES')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['User ID', 'First Name', 'Last Name', 'Mobile_Number', 'Mail ID', 'DOB', 'City', 'State', 'Address'])
    return df

def view_all_hosts(cursor):
    cursor.execute('SELECT * FROM HOSTS')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Host ID', 'Host Name', 'Mobile Number', 'Mail ID'])
    return df
    

def view_all_events(cursor):
    cursor.execute('SELECT * FROM Events')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Event ID', 'Event Name', 'Event Type', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Venue', 'Host ID'])
    df["Start Time"] = df["Start Time"].values.astype('datetime64[ns]')
    df["End Time"] = df["End Time"].values.astype('datetime64[ns]')
    return df

def view_all_bills(cursor):
    query = 'CALL RETURN_ALL_BILLS();'
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Bill ID', 'Supplier Name', 'Host Name', 'Event Name', 'Amount', 'Payment Status'])
    return df

def view_all_suppliers(cursor):
    cursor.execute('SELECT * FROM Supplier')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Supplier ID', 'Supplier Name', 'Department', 'Mail ID', 'Point of Contact', 'Mobile Number', 'Address'])
    return df

