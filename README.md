# Project Overview

The goal of this project is to build an automatic ETL pipeline to update the dashboard. This project use Python to extract data from Reddit API using subreddit: ChatGPT and stream them into the PostgreSQL database, perform sentiment analysis and further build a dashboard using Tableau to display people's attitude toward the new technology.


# Reddit Data Scraper

This is a Python script that scrapes data from a specified subreddit using the PRAW library and inserts the scraped data into a PostgreSQL database. The script also performs text cleaning and sentiment analysis on the scraped data using the TextBlob and NLTK libraries.

## Prerequisites

Make sure you have the following dependencies installed:

- `psycopg2`
- `sqlalchemy`
- `textblob`
- `nltk`
- `praw`

You can install these dependencies using `pip`:

```bash
pip install psycopg2 sqlalchemy textblob nltk praw
```

## Configuration

Before running the script, you need to provide your Reddit API credentials and configure the database connection. Open the script file and replace the following variables with your own values:

- `client_id`: Your Reddit client ID.
- `client_secret`: Your Reddit client secret.
- `username`: Your Reddit username.
- `password`: Your Reddit password.
- `user_agent`: Your Reddit user agent.
- `subreddit_name`: The name of the subreddit you want to scrape.
- `max_results`: The maximum number of results you want to retrieve.
- `sort_by`: The sorting method you want to use (e.g., "hot", "new", "top", etc.).
- `engine`: The connection string for your PostgreSQL database (e.g., `'postgresql://username:password@servername:portnumber/database'`).

## Usage

To run the script, execute the following command:

```bash
python script_reddit.py
```

The script will scrape the specified subreddit, clean the text data, calculate sentiment scores, and insert the scraped data into the PostgreSQL database.

## Visualization

[Reddit Tableau Dashboard](https://public.tableau.com/views/Reddit_16848001724160/RedditDashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

![RedditDashboard](/tableaudashboard.jpg)


## Insights

* 90% of the reddit are positive or natural. Most of the People show positive attitude toward the new technology ChatGPT.

* The distribution of upvote rate is skewed. Most people like to upvote the post regarding to ChatGPT. 

## Conclusion
This data pipeline facilitates the acquisition of real-time data, which is subsequently loaded into a PostgreSQL database and updated on a data dashboard. Due to the inherent limitations of Tableau Public, the file is manually loaded into the Tableau Public platform as part of this project.
