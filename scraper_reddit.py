
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import insert

from textblob import TextBlob
from nltk.corpus import stopwords
import re
from datetime import datetime, timedelta


#clean tweet text

def clean_text(text):
  ex_list = ['rt', 'http', 'RT']
  exc = '|'.join(ex_list)
  text = re.sub(exc, ' ' , text)
  text = text.lower()
  words = text.split()
  stopword_list = stopwords.words('english')
  words = [word for word in words if not word in stopword_list]
  clean_text = ' '.join(words)
  return clean_text

def sentiment_score(text):
  analysis = TextBlob(text)
  if analysis.sentiment.polarity > 0:
    return 1
  elif analysis.sentiment.polarity == 0:
    return 0
  else:
    return -1

import praw

reddit = praw.Reddit(client_id='yourclientid',
                     client_secret='yourclientsecret',
                     username='yourusername',
                     password='yourpassword',
                     user_agent='youruseragent')

# Now you can make API requests using the `reddit` object

subreddit_name = "ChatGPT" # Replace with the name of the subreddit you want to search
max_results = 1000# Replace with the maximum number of results you want to retrieve
sort_by = "all" # Replace with the sorting method you want to use (e.g. "hot", "new", "top", etc.)
# time_range = 14  # Number of days


# Get the submissions for the time range
submissions = reddit.subreddit(subreddit_name).search(query='*', sort=sort_by,time_filter='all', limit=max_results)


meta_list = [] 
for submission in submissions:
    title = submission.title
    created_at = submission.created_utc
    num_comments = submission.num_comments
    score = submission.score  #  total number of upvotes minus the total number of downvotes
    upratio = submission.upvote_ratio
    if submission.author is not None:
      author = submission.author.name
    else:
      author = '[deleted]'

    permalink = submission.permalink
    url = submission.url
    text = submission.selftext
    text_sent = clean_text(text)
    result_score = sentiment_score(text_sent)


    data_dict = {
        "title": title,
        "created_at": datetime.fromtimestamp(created_at),
        "num_comments": num_comments,
        "score": score,
        "upratio":upratio,
        "author": author,
        "permalink": permalink,
        "url": url,
        "sentiment_score": result_score 

    }
    meta_list.append(data_dict)

print(len(meta_list))


#connect engine
engine = create_engine('postgresql://username:yourpassword@servername:portnumber/database')

conn = engine.connect()
metadata = MetaData()
print(metadata.tables)
# reflect db schema to MetaData
trans = conn.begin()
metadata.reflect(bind=engine)

table_reddit = metadata.tables['reddit_info']

insert_stmt = insert(table_reddit)
#if you have constraint in your database, and you just want to update unique record
do_nothing_stmt = insert_stmt.on_conflict_do_nothing(constraint='reddit_info_pkey')


result_proxy = conn.execute(do_nothing_stmt, meta_list)
trans.commit()
conn.close()

