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
def delete_query_for_podcast():
    with open(os.path.join(base_path, "secrets.txt"), "r") as file:
        lines = file.readlines()

    secrets = {}
    for line in lines:
        key, value = line.strip().split("=")
        secrets[key.strip()] = value.strip()

    engine = create_engine(f"""{secrets["dialect"]}://{secrets["username"]}:{secrets["password"]}@{secrets["host"]}:{secrets["port"]}/{secrets["database"]}""")
    Session = sessionmaker(bind=engine)
    # Allow users to input the ID of the row to delete
    
    podcast_id = int(st.number_input("Enter the podcast id to be deleted"))
    if st.button("Run Query"):
        # Perform the query when the button is pressed
        with Session() as session:
            query = text(f"""DELETE FROM "podcasts" where "Podcast_ID" = {podcast_id}""")
            session.execute(query)
            try:
                session.commit()
                # Display a success message
                st.success("Query executed successfully!")
            except:
                st.error("Data can't be inserted")



