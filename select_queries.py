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


def select_queries_select():
    st.markdown(
    f"<h1 style='text-align: center; font-size: 50px; color: #FF0000'>Run some predetermined select Queries</h1>",
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
    
    select_queries = ["Region Wise Revenue From Users On Spotify",\
                      "Total Revenue From All Users On Spotify", \
                    "Display Incoming, Outgoing And Current Customers Month-Wise", \
                    "Fetch The Podcast Table"]
    selected_query = st.selectbox("Choose some SELECT queries from the given options", options=select_queries)
    if st.button("Run Query"):

        if selected_query == "Fetch The Podcast Table":
            # Perform the query when the button is pressed
            with Session() as session:
                query = text(f"""select * from "podcasts";""")
                result = session.execute(query).fetchall()
                try:
                    st.success("Query executed successfully!")

                    # Display the result in a table
                    st.table(result)
                except:
                    st.error("Data can't be inserted")


        if selected_query == "Region Wise Revenue From Users On Spotify":
            # Perform the query when the button is pressed
            with Session() as session:
                query = text(f"""select COUNT("User_ID") as CNT, "user"."User_Region" from "user"
                                where "user"."Subscription_ID" IS NOT NULL
                                group by "user"."User_Region"
                                order by CNT desc;""")
                result = session.execute(query).fetchall()
                try:
                    st.success("Query executed successfully!")

                    # Display the result in a table
                    st.table(result)
                except:
                    st.error("Data can't be inserted")
        
        elif selected_query == "Total Revenue From All Users On Spotify":
            # Perform the query when the button is pressed
            with Session() as session:
                query = text(f"""select COUNT("User_ID") as total_revenue_generating_cutomers from "user"
                                    where "user"."Subscription_ID" IS NOT NULL;""")
                result = session.execute(query).fetchall()
                try:
                    st.success("Query executed successfully!")
                    st.table(result)
                except:
                    st.error("Data can't be inserted")

        else:
            with Session() as session:
                query = text(f"""WITH MonthlyUserSubscriptions AS (
                                    SELECT
                                        DISTINCT
                                        EXTRACT(MONTH FROM "Start Date") AS month,
                                        EXTRACT(YEAR FROM "Start Date") AS year,
                                        "Subscriber ID",
                                        CASE WHEN "End Date" < '2099-01-01 00:00:00' THEN "Subscriber ID" END AS lost_customers
                                    FROM
                                        "premium_subscription"
                                    WHERE
                                        EXTRACT(YEAR FROM "Start Date") BETWEEN 2018 AND 2023
                                    )

                                    SELECT
                                    month,
                                    year,
                                    COUNT("Subscriber ID") AS subscription_count,
                                    COUNT(DISTINCT lost_customers) AS lost_customers_count,
                                    COUNT("Subscriber ID") - COUNT(DISTINCT lost_customers) AS difference
                                    FROM
                                    MonthlyUserSubscriptions
                                    GROUP BY
                                    month, year
                                    ORDER BY
                                    year, month;""")
                result = session.execute(query).fetchall()
                try:
                    st.success("Query executed successfully!")
                    st.table(result)
                except:
                    st.error("Data can't be inserted")


