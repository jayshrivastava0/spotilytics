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

def page2():
    st.markdown(
        f"<h1 style='text-align: center; font-size: 70px; color: #FF0000'>Add the required fields to add record in Podcast Table</h1>",
        unsafe_allow_html=True
    )
    # st.title("What is Spotilytics, you ask?")
    with open(os.path.join(base_path, "secrets.txt"), "r") as file:
        lines = file.readlines()

    secrets = {}
    for line in lines:
        key, value = line.strip().split("=")
        secrets[key.strip()] = value.strip()


    engine = create_engine("postgresql://kecagi7371:WBxwqNPX9r0V@ep-solitary-poetry-a50h7kvl-pooler.us-east-2.aws.neon.tech/spotify_db?sslmode=require")
    Session = sessionmaker(bind=engine)
    # Allow users to input the ID of the row to delete
    
    podcast_id = int(st.number_input("Enter the Podcast ID to enter in the DB"))
    podcast_title = st.text_input("Enter the Podcast_title to be inserted:")
    episode_number = int(st.number_input("Enter the Episode Number of the Podcast:"))
    episode_date = st.date_input("Enter Episode Date of Podcast")
    host_name = st.text_input("Enter Host name for podcast")
    if st.button("Run Query"):
        # Perform the query when the button is pressed
        with Session() as session:
            query = text(f"""INSERT INTO "podcasts" ("Podcast_ID", "Podcast_Title", "Episode_Number", "Episode_Date", "Host_Name") \
                         VALUES ({podcast_id}, '{podcast_title}' , {episode_number}, '{episode_date}', '{host_name}');""")
            values = {
            "podcast_id": podcast_id,
            "podcast_title": podcast_title,
            "episode_number": episode_number,
            "episode_date": episode_date,  # Convert date to string
            "host_name": host_name}

            session.execute(query, values)
            try:
                session.commit()
            
                # Display a success message
                st.success("Query executed successfully!")
            except:
                st.error("Data can't be inserted")



