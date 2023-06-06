select t.tweet_id from
tweets t
where length(t.content) > 15