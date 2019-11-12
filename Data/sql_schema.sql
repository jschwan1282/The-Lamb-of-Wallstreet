create table tweets (
	date date,
	likes numeric,
	retweets numeric,
	total_tweets numeric,
	t_value numeric
);

create table stocks (
	date date,
	open numeric,
	hight numeric,
	low numeric,
	close numeric,
	volume numeric
);

select * from stocks;

create table final as (select tweets.date, stocks.close, sum(tweets.likes) as total_lies, sum(tweets.retweets) as total_retweets, 
sum(tweets.total_tweets) as total_tweets, sum(tweets.t_value) as t_value 
from tweets
left join stocks on (tweets.date = stocks.date)
group by tweets.date, stocks.close
order by tweets.date desc
);


