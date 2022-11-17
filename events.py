import streamlit as st
import pandas as pd 
import functions

def event_page(conn, cursor):
    Event_menu = ["Add Event", "View All Events", "View Event", "Edit Event", "Remove Event"]
    Event_choice = st.sidebar.selectbox("Menu", Event_menu)

    match Event_choice:
        case "Add Event":
            e_name = st.text_input("Event Name:")
            e_type = st.text_input("Event Type:")
            e_date_start = st.date_input("Event Start Date:")
            e_date_end = st.date_input("Event End Date:")
            venue = st.text_input("Venue:")
            start_time = st.time_input("Event Start Time:")
            end_time = st.time_input("Event End Time:")
            host_id = st.text_input("Host ID:")

            if st.button("Add Event"):
                query = ('INSERT INTO Events (EVENT_NAME, EVENT_TYPE, EVENT_DATE_START, EVENT_DATE_END, EVENT_TIME_START, EVENT_TIME_END, VENUE, HOST_ID) VALUES (%s, %s, %s, %s, %s, %s,%s, %s);')
                values = (e_name, e_type, e_date_start, e_date_end, start_time, end_time, venue, host_id)
                cursor.execute(query, values)
                conn.commit()
                st.success("Successfully added Event: {}".format(e_name))

        case "View All Events":            
            df = functions.view_all_events(cursor)
            st.dataframe(df)

        case "View Event":
            e_name = st.text_input("Event Name:")

            if st.button("View Event"):
                query = ('SELECT * FROM Events WHERE E_NAME = %s;')
                values = (e_name)
                cursor.execute(query, values)
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=['Event ID', 'Event Name', 'Event Type', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Venue', 'Host ID'])
                st.dataframe(df)

        case "Edit Event":
            edit_menu = ['Event Name', 'Event Type', 'Start Date', 'End Date', 'Start Time', 'End Time', 'Venue', 'Host ID']
            edit_choice = st.selectbox("Menu", edit_menu)

            if edit_choice == 'Event Name':
                Event_id = st.text_input("Event ID:")
                e_name = st.text_input("Event Name:")

                if st.button("Update"):
                    query = ('UPDATE Events SET Event_NAME = %s WHERE Event_ID = %s;')
                    values = (e_name, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")

            if edit_choice == 'Event Type':
                Event_id = st.text_input("Event ID:")
                e_type = st.text_input("Event Type:")

                if st.button("Update"):
                    query = ('UPDATE Events SET Event_type = %s WHERE Event_ID = %s;')
                    values = (e_type, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")

            if edit_choice == 'Start Date':
                Event_id = st.text_input("Event ID:")
                start = st.date_input("Start Date:")

                if st.button("Update"):
                    query = ('UPDATE Events SET event_date_start = %s WHERE Event_ID = %s;')
                    values = (start, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")
            
            if edit_choice == 'End Date':
                Event_id = st.text_input("Event ID:")
                end = st.date_input("End Date:")

                if st.button("Update"):
                    query = ('UPDATE Events SET event_date_end = %s WHERE Event_ID = %s;')
                    values = (end, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")
            
            if edit_choice == 'Start Time':
                Event_id = st.text_input("Event ID:")
                start_t = st.time_input("Start Time:")

                if st.button("Update"):
                    query = ('UPDATE Events SET event_time_start = %s WHERE Event_ID = %s;')
                    values = (start_t, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")
            
            if edit_choice == 'End Time':
                Event_id = st.text_input("Event ID:")
                end_t = st.time_input("End Time:")

                if st.button("Update"):
                    query = ('UPDATE Events SET event_time_end = %s WHERE Event_ID = %s;')
                    values = (end_t, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")

            if edit_choice == 'Venue':
                Event_id = st.text_input("Event ID:")
                venue = st.text_input("Venue:")

                if st.button("Update"):
                    query = ('UPDATE Events SET venue = %s WHERE Event_ID = %s;')
                    values = (venue, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")
            
            if edit_choice == 'Host ID':
                Event_id = st.text_input("Event ID:")
                h_id = st.text_input("Host ID:")

                if st.button("Update"):
                    query = ('UPDATE Events SET host_id = %s WHERE Event_ID = %s;')
                    values = (h_id, Event_id)
                    cursor.execute(query, values)
                    conn.commit()
                    st.success("Successfully Updated Event")

        case "Remove Event":            
            df = functions.view_all_events(cursor)
            with st.expander('View all Events'):
                st.dataframe(df)
            
            list_of_Event =  [i for i in df.iloc[:, 0]]
            selected_Event = st.selectbox("Select Event ID to Delete", list_of_Event)
            if st.button("Delete Event"):
                cursor.execute('DELETE FROM Event WHERE Event_ID="{}"'.format(selected_Event))
                conn.commit()
                st.success("Event has been deleted successfully")
