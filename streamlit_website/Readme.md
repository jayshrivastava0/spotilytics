# Spotilytics

## Overview
Spotilytics is a comprehensive database management and analytics project designed to compute essential business Key Performance Indicators (KPIs). It monitors metrics such as customer churn analysis, monthly active users (MAU), Customer Lifetime Value (CLV), and Gross Revenue, providing valuable insights for strategic decision-making and performance evaluation within the Spotify platform. Performed other analyses like Geotargeting, Follower Count, and Regional Genre Analysis to gain deeper insights into user engagement, demographic trends, and cultural preferences across different markets, ultimately enhancing content curation, personalized recommendations, and platform optimization strategies.

## Project Structure
- **home_page.py**: Defines the content for the home page of the web application, including information about the contributors and their roles.

- **insert_queries.py**: Contains functionality related to inserting new data into the PostgreSQL database.

- **delete_query.py**: Implements the logic for deleting records from the database.

- **update_queries.py**: Manages the update queries for modifying data in the database.

- **select_queries.py**: Handles various SELECT queries to retrieve specific information from the database.

## Dependencies
- `PIL`: Python Imaging Library for working with images.
- `streamlit`: Web framework for creating interactive web applications.
- `sqlalchemy`: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- `psycopg2-binary`: PostgreSQL adapter for Python.

## Database Configuration
1. Store your database credentials in a file named `secrets.txt` and save it. 
   ```
   dialect=postgresql
   username=<your_username>
   password=<your_password>
   host=<your_host>
   port=<your_port>
   database=<your_database>
   ```

## Running the Application
1. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

2. Execute the main script:
   ```
   streamlit run DQML_group.py
   ```

3. Access the application by navigating to the provided URL in your web browser.

## Pages
The web application consists of the following pages:

- **Home**: Overview and introduction to the project and contributors.
- **ER_diagram**: Displays the Entity-Relationship (ER) diagram of the database.
- **Insert Query**: Allows users to insert new data into the database.
- **Delete Query**: Enables the deletion of records from the database.
- **Select Query**: Provides options for running SELECT queries to retrieve specific information.
- **Update Query**: Facilitates the modification of data in the database.




-- The readme for fake data geneartion script is the folder Fake_Data_generator


Feel free to explore and interact with the various functionalities of the web application!

---


