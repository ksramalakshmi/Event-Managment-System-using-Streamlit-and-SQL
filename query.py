import streamlit as st
import pandas as pd
from functions import view_all_events

def query_page(conn, cursor):
    query = st.text_input('Input your query here:') 

    if st.button("Execute"):
        cursor.execute(query)
        conn.commit()

        data = cursor.fetchall()

        if query.lower() == 'select * from events;':
            df = view_all_events(cursor)
        else:
            df = pd.DataFrame(data)

        st.dataframe(df)
        st.success("Query execution successful!")
