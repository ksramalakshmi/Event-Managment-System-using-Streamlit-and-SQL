import streamlit as st
import pandas as pd 
import functions

def attendee_event(conn, cursor):
    Event_menu = ["Attend Event", "View All Event Attendees", "View Event Attendees", "Edit Event Attendees", "Remove Event Attendees"]
    Event_choice = st.sidebar.selectbox("Menu", Event_menu)

    match Event_choice:
        case "Attend Event":
            df1 = functions.view_all_events(cursor)
            event_names = [i for i in df1.iloc[:, 1]]
            event_names.insert(0, "Select Event")
            e_name_choice = st.selectbox("Event Name", event_names)
            if (e_name_choice != "Select Event"):
                e_id = str(df1.loc[df1['Event Name'] == e_name_choice]['Event ID'].values[0])

            df2 = functions.view_all_attendees(cursor)
            attendee_names = [i for i in df2.iloc[:, 1]]
            attendee_names.insert(0, "Select Name")
            attendee_name_choice = st.selectbox("Attendee", attendee_names)
            if(attendee_name_choice != "Select Name"):
                attendee_id = str(df2.loc[df2['First Name'] == attendee_name_choice]['User ID'].values[0])

            if st.button("Attend Event"):
                query = ('INSERT INTO ATTENDED_BY (USER_ID, EVENT_ID) VALUES (%s, %s);')
                values = (e_id, attendee_id)
                cursor.execute(query, values)
                conn.commit()
                st.success("You are attending the event: {}!".format(e_name_choice))

        case "View All Event Attendees":            
            df = functions.view_all_attendees_events(cursor)
            st.dataframe(df)

        case "View Event Attendees":
            e_name = st.text_input("Event Name:")

            if st.button("View Event"):
                query = ('SELECT * FROM Events WHERE E_NAME = %s;')
                values = (e_name)
                cursor.execute(query, values)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Event ID', 'Event Name', 'Event Type', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Venue', 'Host ID'])
                st.dataframe(df)

        case "Remove Event Attendee":            
            df = functions.view_all_attendees_events(cursor)
            with st.expander('View all Event Attendees'):
                st.dataframe(df)
            
            list_of_Event =  [i for i in df.iloc[:, 0]]
            selected_Event = st.selectbox("Select Event ID to remove", list_of_Event)

            list_of_attendees =  [i for i in df.iloc[:, 2]]
            selected_attendee = st.selectbox("Select Event ID to remove", list_of_attendees)

            if st.button("Remove Event"):
                cursor.execute('DELETE FROM ATTENDED_BY WHERE Event_ID="{}" & User_ID = "{}"'.format(selected_Event, selected_attendee))
                conn.commit()
                st.success("Event has been removed successfully")
