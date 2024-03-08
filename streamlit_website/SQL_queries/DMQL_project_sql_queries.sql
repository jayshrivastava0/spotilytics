
--query 1
-- Most popular genres in different regions – top 3 genres in each region
explain (ANALYZE, COSTS, TIMING)
WITH UserTrackGenre AS (
    SELECT
        "user"."User_Region",
        "tracks"."Track_Genre",
        COUNT(*) AS play_count,
        ROW_NUMBER() OVER (PARTITION BY "user"."User_Region" ORDER BY COUNT(*) DESC) AS genre_rank 
    FROM
        "user"
    JOIN
        "user_tracks" ON "user_tracks"."User_ID" = "user"."User_ID"
    JOIN
        "tracks" ON "user_tracks"."Track_ID" = "tracks"."Track_ID"
    GROUP BY
        "user"."User_Region", "tracks"."Track_Genre"
)
SELECT
    "User_Region",
    "Track_Genre",
    play_count
FROM
    UserTrackGenre
WHERE
    genre_rank <= 3;
	

--query 2
--album with most subscribed users - ALBUM WISE REVENUE - MOST TIME
explain (ANALYZE, COSTS, TIMING)
SELECT
    "album"."Album_Title",
    SUM(CASE WHEN "user"."Subscription_ID" IS NOT NULL THEN 1 ELSE 0 END) AS count
FROM
    "user"
JOIN
    "user_artists" ON "user_artists"."Artist_ID" = "user"."User_ID"
JOIN
    "album_artists" ON "album_artists"."Album_ID" = "user_artists"."Artist_ID"
JOIN
    "album" ON "album"."Album_ID" = "album_artists"."Album_ID"
GROUP BY
    "album"."Album_Title"
ORDER BY count DESC;


--artists have how many subscribed user follower count - ARTIST WISE REVENUE
--query 3
explain (ANALYZE, COSTS, TIMING)
select "artist"."Artist_Name", count("user"."Subscription_ID")
from "user"
inner join "user_artists" on "user"."User_ID" = "user_artists"."User_ID" 
inner join "artist" on "artist"."Artist_ID" = "user_artists"."Artist_ID"
where "user"."Subscription_ID" IS NOT NULL 
group by "artist"."Artist_Name"

--query 4
--display podcasts by region
select "user"."User_Region", "podcasts"."Podcast_Title" from "playlist_and_podcast"
join "podcasts" on "podcasts"."Podcast_ID" = "playlist_and_podcast"."Podcast_ID"
join "user_playlist" on "user_playlist"."User_Playlist_ID" = "playlist_and_podcast"."User_Playlist_ID"
join "user_and_playlist" on "user_and_playlist"."User_Playlist_ID" = "user_playlist"."User_Playlist_ID"
join "user" on "user"."User_ID" = "user_and_playlist"."User_ID"
order by "user"."User_Region"
--or
--display number of podcasts by region
select "user"."User_Region", count( distinct "podcasts"."Podcast_Title") as CNT from "playlist_and_podcast" --changed
join "podcasts" on "podcasts"."Podcast_ID" = "playlist_and_podcast"."Podcast_ID"
join "user_playlist" on "user_playlist"."User_Playlist_ID" = "playlist_and_podcast"."User_Playlist_ID"
join "user_and_playlist" on "user_and_playlist"."User_Playlist_ID" = "user_playlist"."User_Playlist_ID"
join "user" on "user"."User_ID" = "user_and_playlist"."User_ID"
group by "user"."User_Region"
order by CNT desc


--query 5
--display most played host of podcasts by region
WITH RankedPodcastHosts AS (
  SELECT
    "user"."User_Region",
    "podcasts"."Host_Name",
    ROW_NUMBER() OVER (PARTITION BY "user"."User_Region" ORDER BY COUNT(*) DESC) AS rank
  FROM
    "playlist_and_podcast"
    JOIN "podcasts" ON "podcasts"."Podcast_ID" = "playlist_and_podcast"."Podcast_ID"
    JOIN "user_playlist" ON "user_playlist"."User_Playlist_ID" = "playlist_and_podcast"."User_Playlist_ID"
    JOIN "user_and_playlist" ON "user_and_playlist"."User_Playlist_ID" = "user_playlist"."User_Playlist_ID"
    JOIN "user" ON "user"."User_ID" = "user_and_playlist"."User_ID"
  GROUP BY
    "user"."User_Region", "podcasts"."Host_Name"
)
SELECT
  "User_Region",
  "Host_Name"
FROM
  RankedPodcastHosts
WHERE
  rank = 1;


--query 6
--credit card vs gift + debit card count
SELECT
    COUNT(CASE WHEN "Payment Method" = 'Credit Card' THEN "Subscriber ID" END) AS CREDIT_CARD_COUNT,
    COUNT(CASE WHEN "Payment Method" IN ('Gift Card', 'Debit Card') THEN "Subscriber ID" END) AS GIFT_DEBIT_COUNT
FROM
    "transactions";


--query 7
--total revenue from all users on spotify
select COUNT("User_ID") from "user"
where "user"."Subscription_ID" IS NOT NULL

--region wise revenue from users on spotify
select COUNT("User_ID") as CNT, "user"."User_Region" from "user"
where "user"."Subscription_ID" IS NOT NULL
group by "user"."User_Region"
order by CNT desc


--query 8
--number of users with descending duration of track
SELECT
  "tracks"."Track_Title",
  "tracks"."Track_Duration_Minutes" * 60 + "tracks"."Track_Duration_Seconds" AS "Total_Duration_in_seconds",
  COUNT("user"."User_ID") AS "Number_of_Users"
FROM
  "tracks"
JOIN
  "user_tracks" ON "user_tracks"."Track_ID" = "tracks"."Track_ID"
JOIN
  "user" ON "user"."User_ID" = "user_tracks"."User_ID"
GROUP BY
  "tracks"."Track_Title", "Total_Duration_in_seconds"
ORDER BY
  "Total_Duration_in_seconds" DESC;


--query 9
--Churn subscription time of subscribed users
--display churn rate
WITH ChurnData AS (
  SELECT
    "Subscriber ID",
    EXTRACT(day FROM AGE("End Date", "Start Date")) AS No_of_days,
    EXTRACT(month FROM "End Date") AS Churn_Month,
    EXTRACT(year FROM "End Date") AS Churn_Year
  FROM
    "premium_subscription"
  WHERE
    "End Date" != '2099-01-01 00:00:00' -- Only consider completed subscriptions
)
SELECT
  Churn_Year,
  Churn_Month,
  COUNT(*) AS lost_customers,
  ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM "user"), 3) AS churn_rate
FROM
  ChurnData
GROUP BY
  Churn_Year, Churn_Month
ORDER BY
  Churn_Year DESC, Churn_Month DESC;


--query 10
--display incoming, outgoing and current customers month-wise
WITH MonthlyUserSubscriptions AS (
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
  year, month;


--QUERY 13
--cumulative sum of all users monthwise
SELECT month, year, users, sum(users) over (order by year, month, users) as cumulative_sum from 
	(SELECT *, lag(users,1) over(order by (year, month)) as second_month from(
		SELECT																	
			EXTRACT(MONTH FROM created_at) AS month,
			EXTRACT(YEAR FROM created_at) AS year,
			COUNT(user_id) AS users

		FROM
			(
				SELECT
					"Created_At" AS created_at,
					"User_ID" AS user_id
				FROM
					"user" AS users
			) AS created_at_and_user
		GROUP BY month, year 
	) as temp
) as new_output