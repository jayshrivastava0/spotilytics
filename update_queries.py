# ! pip install sqlalchemy
# ! 
from sqlalchemy import create_engine

# Load database credentials from Streamlit secrets.toml
import streamlit as st
import psycopg2

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# requirements.txt
# import psycopg2-binary
import sqlalchemy
import os


base_path = os.getcwd()
def update_query():
    st.markdown(f"<h1 style='text-align: center; font-size: 50px; color: #FF0000'>Fill the required fields to update a record in User Table</h1>",
        unsafe_allow_html=True)
    with open(os.path.join(base_path, "secrets.txt"), "r") as file:
        lines = file.readlines()

    secrets = {}
    for line in lines:
        key, value = line.strip().split("=")
        secrets[key.strip()] = value.strip()

    engine = create_engine("postgresql://kecagi7371:WBxwqNPX9r0V@ep-solitary-poetry-a50h7kvl-pooler.us-east-2.aws.neon.tech/spotify_db?sslmode=require")
    Session = sessionmaker(bind=engine)
    # Allow users to input the ID of the row to delete
    user_id = int(st.number_input("Choose User ID to Which The Update Should Be Applied"))
    subscribed_or_not = st.selectbox("After Updation, Should User Be Subscribed Or Not", options= ['Yes', 'No'])
    if subscribed_or_not == 'Yes':
        subscription_id = int(st.number_input("What should be the Subscription ID"))
    else:
        subscription_id = 'NULL'
    if st.button("Run Query"):
        # Perform the query when the button is pressed
        with Session() as session:
            query = text(f"""UPDATE "user"
                            SET "Is_Subscribed" = '{subscribed_or_not}', "Subscription_ID" = {subscription_id}
                            WHERE "User_ID"={user_id};""")

            session.execute(query)
            try:
                session.commit()
            
                # Display a success message
                st.success("Query executed successfully!")
            except:
                st.error("Data can't be inserted")



