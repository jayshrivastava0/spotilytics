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
    with open(os.path.join(base_path, "secrets.txt"), "r") as file:
        lines = file.readlines()

    secrets = {}
    for line in lines:
        key, value = line.strip().split("=")
        secrets[key.strip()] = value.strip()

    engine = create_engine(f"""{secrets["dialect"]}://{secrets["username"]}:{secrets["password"]}@{secrets["host"]}:{secrets["port"]}/{secrets["database"]}""")
    Session = sessionmaker(bind=engine)
    # Allow users to input the ID of the row to delete
    user_id = int(st.number_input("Choose User ID to which the update should be applied"))
    subscribed_or_not = st.selectbox("After updation, should User be subscribed or not", options= ['yes', 'no'])
    if subscribed_or_not == 'yes':
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



