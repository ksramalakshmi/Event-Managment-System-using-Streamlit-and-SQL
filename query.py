import streamlit as st
import pandas as pd

def query_page(conn, cursor):
    query = st.text_input('Input your query here:') 

    if st.button("Execute"):
        cursor.execute(query)
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        st.dataframe(df)
        st.success("Query execution successful!")
        conn.commit()
