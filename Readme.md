# [Spotilytics Website](https://spotilyticss.streamlit.app/)

# [Spotilytics Website on Hugging Face](https://huggingface.co/spaces/jayshrivastava/Spotilytics)

### Overview

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



-------------------------------------------------------------------------------------

#### The readme for fake data geneartion script is the folder Fake_Data_generator
# Entity Sets Table README

## Overview

This dataset contains synthetically generated data using Faker for various entities such as users, artists, albums, tracks, podcasts, user playlists, transactions, and premium subscriptions. The purpose of this dataset is to provide a simulated environment for testing and analysis.

## Entity Descriptions

1. **Users**
   - `User_ID`: Incremental identifier for users.
   - `User_Email`: Email address of the user.
   - `User_Encrypted_Pass`: Encrypted password (MD5) of the user.
   - `User_Region`: Region associated with the user.
   - `Created_At`: Timestamp indicating the user's creation date.
   - `Is_Subscribed`: Subscription status ("yes" or "not").
   - `Subscription_ID`: Identifier for the subscription if subscribed, otherwise null.

2. **Artists**
   - `Artist_ID`: Identifier for artists.
   - `Artist_Name`: Name of the artist.

3. **Albums**
   - `Album_ID`: Identifier for albums.
   - `Album_Title`: Title of the album.
   - `Album_Release_Date`: Release date of the album.

4. **Tracks**
   - `Track_ID`: Identifier for tracks.
   - `Track_Title`: Title of the track.
   - `Track_Genre`: Genre of the track.
   - `Track_Duration_Minutes`: Duration of the track in minutes.
   - `Track_Duration_Seconds`: Duration of the track in seconds.

5. **Podcasts**
   - `Podcast_ID`: Identifier for podcasts.
   - `Podcast_Title`: Title of the podcast.
   - `Episode_Number`: Incremental episode number.
   - `Episode_Date`: Date of the podcast episode.
   - `Host_Name`: Name of the podcast host.

6. **User Playlists**
   - `User_Playlist_ID`: Identifier for user playlists.
   - `Title`: Title of the playlist.
   - `Public/Private`: Visibility status of the playlist ("public" or "private").
   - `Track/Podcast`: Type of content in the playlist ("track" or "podcast").

7. **Transactions**
   - `Subscriber_ID`: Subscriber identifier.
   - `Payment_Method`: Payment method used for the transaction.
   - `Transaction_Date`: Date of the transaction.

8. **Premium Subscriptions**
   - `Subscriber_ID`: Subscriber identifier.
   - `Start Date`: Start date of the subscription.
   - `End Date`: End date of the subscription.
   - `Canceled or Not`: Subscription status ("renew" or "cancel").

## Constraints
- First you'll have to create a database then insert that into the cell of postgres connection
- User passwords are encrypted using MD5.
- Subscription status is represented as "yes" for subscribed users and "not" for non-subscribed users.
- Episode numbers for podcasts are incremental.
- Episode dates for podcasts are weekly incremental until the episode number changes to 1.
- User playlist visibility is either "public" or "private," and the content type is either "track" or "podcast."
- Transaction dates are monthly incremental.
- Premium subscriptions are marked as "renew" if the end date is "01-01-2099"; otherwise, they are marked as "cancel" with the date of cancellation.

## Notes

- This dataset is synthetically generated using the Faker library to create a realistic yet fictional representation of the entities.
- It is intended for testing, analysis, and educational purposes.


Feel free to explore and interact with the various functionalities of the web application!

---

