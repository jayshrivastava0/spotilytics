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
