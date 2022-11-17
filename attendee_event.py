import streamlit as st
import pandas as pd 
import functions

def attendee_event(conn, cursor):
    Event_menu = ["Attend Event", "View All Event Attendees", "View Event Attendees", "Attend Another Event", "Remove Event Attendee"]
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
                values = (attendee_id, e_id)
                cursor.execute(query, values)
                conn.commit()
                st.success("You are attending the event: {}!".format(e_name_choice))

        case "View All Event Attendees":            
            df = functions.view_all_attendees_events(cursor)
            st.dataframe(df)

        case "View Event Attendees":
            df = functions.view_all_events(cursor)
            events = [i for i in df.iloc[:, 1]]
            events.insert(0, "Select Event")
            event_choice = st.selectbox("Event Name", events)

            if st.button("View Attendees"):
                df = functions.view_all_attendees_events(cursor)
                st.dataframe(df.loc[df['Event Name']==event_choice])

        case "Attend Another Event":            
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
                values = (attendee_id, e_id)
                cursor.execute(query, values)
                conn.commit()
                st.success("You are now attending the event: {}".format(e_name_choice))


        case "Remove Event Attendee":            
            df = functions.view_all_attendees_events(cursor)
            with st.expander('View all Event Attendees'):
                st.dataframe(df)
            
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

            if st.button("Remove Event"):
                cursor.execute('DELETE FROM ATTENDED_BY WHERE Event_ID = "{}" AND User_ID = "{}";'.format(e_id, attendee_id))
                conn.commit()
                st.success("Event has been removed successfully")
