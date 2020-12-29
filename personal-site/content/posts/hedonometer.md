---
title: "Hedonometer"
date: 2020-12-21T14:10:46Z
draft: false
plotly: true
---

## Background

About two months ago, I was introduced to a work of the University of Vermont Computational Story Lab called the Hedonometer. At its core, the Hedonometer is a large scale NLP application based on Twitter data and is used to measure "happiness" at scale. The creators do a great job summarizing this here:

> **“What is being measured by the instrument?”** <br><br>
 hedonometer.org currently measures Twitter’s Decahose API feed (formerly Gardenhose). The stream reflects a 10% random sampling of the roughly  500 million messages posted to the service daily, comprising roughly 100GB of raw JSON each day. Words in messages we determine to be written  in English are thrown into a large bag containing roughly 200 million words per day. This bag is then assigned a happiness score based on the  average happiness score of the words contained within. While "bag-of-words" approaches can be problematic for small collections of text, we  have found the methodology to work well at the large scale.

My introduction to the Hedonometer came via Gimlet Media's Replay All podcast. I was always going to find a quantitative measure of global happiness interesting but what struck me most as I listened to the show's hosts talk to the creators of the Hedonometer was that this seemed like ai cool project for me to try to recreate on my own. So ... that is exactly what I did and below is a brief write-up of my attempt. 

## Sleuthing Around

At first, I spent multiple hours messing around with Twitter's API and open source NLP lexicon python packages (a colleague recommend vaderSentiment). What I quickly realized was the following:
1. It is not easy to get large quantities of historical data from Twitter
2. Most of the publicly available NLP sentiment analysis packages seem to follow a similar pattern
3. (and this is embarrassing to admit because it took me multiple days to realize) hedonometer.org makes their lexicon scoring available via an api. 

The general idea employed by both the creators of the Hedonometer and Vader Sentiment is pretty similar. Crowdsource a bunch of people to rank words/emoticon on AWS Mechanical Turk and employ a rules based system to adjust total scores. Vader's rules set and lexicon are both fairly complex and involved, possibly suggestive of why Vader seems to perform better in my opinion (more on this later). Meanwhile, the Hedonometer seems to use a pretty simple adjustment to remove "neutral" words, words with scores between 4-6 on a 1-9 point scale.

## Trump Twitter

Why not start a twitter based sentiment analysis project with @realDonaldTrump? As I've mentioned earlier, it is difficult to come by large volumes of historical tweets and I needed a baseline to compare my "simple" hedonometer to vaderSentiment. Luckily for me, Harvard's dataverse has a publicly available Donald Trump Twitter dataset comprising @realDonaldTrump tweets from May 2009 to November 2019: [source](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KJEBIL). 

<br>
{{< plotly json="/plotly/hedonometer/djt-tweet-hist.json" height="400px" >}}
<br>
{{< plotly json="/plotly/hedonometer/djt-corr.json" height="400px" >}}
<br>
As you can see above, there is some positive correlation here between vaderSentiment and my interpretation of the Hedonometer. I calculated a pearson's r value of ~0.64. Having looked at some histograms of the vaderSentiment and hedonometer scores of these 40 some thousand @realDonaldTrump tweets and also looking at the correlation plot above, what I suspect is going on here is that my adjustment to the hedonometer to remove the more "neutral" words has made the hedonometer score more sensitive on average than vaderSentiment. 

Let's look at a random selection of tweets and scores:
<br>
```
Tweet: RT @@realDonaldTrump: ....No Obstruction. The Dems were devastated - after all this time and money spent ($40,000,000), the Mueller Report w…
 Hedonometer Score: 6.76
 Hedonometer Dict: {'words': {'all': 6.22, 'money': 7.3}, 'freq': 2}
 Vader Score: -0.6124

Tweet: With Jemele Hill at the mike, it is no wonder ESPN ratings have "tanked," in fact, tanked so badly it is the talk of the industry!
 Hedonometer Score: 4.875
 Hedonometer Dict: {'words': {'no': 3.48, 'wonder': 7.08, 'badly': 2.88, 'talk': 6.06}, 'freq': 4}
 Vader Score: -0.7567

Tweet: RT @mike_pence: Latino Americans know that it was freedom, not socialism, that gave us the most prosperous and powerful nation in the histo…
 Hedonometer Score: 6.0424999999999995
 Hedonometer Dict: {'words': {'Americans': 6.5, 'know': 6.1, 'not': 3.86, 'gave': 6.26, 'us': 6.26, 'most': 6.22, 'powerful': 7.08, 'nation': 6.06}, 'freq': 8}
 Vader Score: 0.8923

Tweet: I can get Nancy Pelosi as many votes as she wants in order for her to be Speaker of the House. She deserves this vi… https://t.co/KiXwdFt4XQ
 Hedonometer Score: 6.146666666666666
 Hedonometer Dict: {'words': {'votes': 6.08, 'she': 6.18, 'She': 6.18}, 'freq': 3}
 Vader Score: 0.0

Tweet: “What happened is that Donald Trump won. Down goes Comey.” @foxandfriends
 Hedonometer Score: 3.66
 Hedonometer Dict: {'words': {'Down': 3.66}, 'freq': 1}
 Vader Score: 0.5719
```
<br>
If there is one take away here, it's that measuring sentiment for individual tweets is not very accurate. Because I've constructed the "simple" hedonometer model myself, all that the logic is doing for each individual tweet is averaging the scored words found in the tweet. vaderSentiment has a larger lexicon and is a bit more complex (my hot take here is that it is slightly more accurate than the hedonometer at detecting underlying sentiment in individual tweets), but even vaderSentiment seems to get things wrong quite often with "tweet" sized text. 

This is something that the creator's of the Hedonometer themselves acknowledge in their paper.

>We address several key aspects and limitations of our measurement. First, as with any sentiment analysis technique, our instrument is fallible for smaller texts, especially at the scale of a typical sentence, where ambiguity may render even human readers unable to judge meaning or tone [61]. Nevertheless, problems with small texts are not our concern, as our interest here is in dealing with and benefiting from very large data sets.
Second, we are also effectively extracting a happiness level as perceived by a generic reader who sees only word frequency. Indeed, our method is purposefully more simplistic than traditional natural language pro- cessing (NLP) algorithms which attempt to infer mean- ing (e.g., OpinionFinder [62, 63]) but suffer from a degree of inscrutability. By ignoring the structure of a text, we are of course omitting a great deal of content; nevertheless, we have shown using bootstrap-like approaches that our method is sufficiently robust as to be meaningful for large enough texts [23].

Given the data exploration above, I am both fairly comfortable with my simple hedonometer and also going to stick to comparing results using my simple hedonometer to scores that hedonometer.org makes publicly available via their API. 

Before moving on though, some more fun with DJT tweets and sentiment analysis.
<br>
{{< plotly json="/plotly/hedonometer/djt-tweets-by-hour.json" height="400px" >}}
<br>
I am sure this has been said before and I am stealing this idea from a smarter person's article I've read elsewhere (if you have the link please send my way). The graph above removes retweets and shows @realDonaldTrump tweet sentiment (normalized vaderSentiment and hedonometer scores) by the hour of day EST time the tweets were sent. In the first 3 years of his Presidency, Donald Trump did the majority of his tweeting between 6 and 10 am EST time and these hours also tended to be when he sent his most negative and unhappy tweets. Looking at the 2020 time series for English speaking twitter on hedonomter.org, a single std dev. move in hedonometer scores is roughly ~0.07 points. From Election Day 2020 (11/3/2020) to the news channels announcements of Joe Biden as the next President of the United States (11/7/2020), English speaking twitter's average happiness dipped and recovered a roughly 1.5 std dev move. The day before Thanksgiving day to Thanksgiving day 2020 was roughly equal to a single standard deviation. I feel these two facts give interesting context to the notion that based on his tweets, Donald Trump's happiness appears to fluctuate by a "Thanksgiving Day" from 6 AM to 2 PM. I wonder how much happier I would be if he stayed of twitter until after he finished a morning round of golf. 

## The New York Times

One of the more interesting applications I could think of for my hedonometer was to do an analysis of the news media. As it turns out, the New York Times has fantastic, public APIs, specifically the `archive` endpoint. 

>The Archive API returns an array of NYT articles for a given month, going back to 1851. Its response fields are the same as the Article Search API. The Archive API is very useful if you want to build your own database of NYT article metadata. You simply pass the API the year and month and it returns a JSON object with all articles for that month. The response size can be large (~20mb).

Here is a look at average hedonometer scores for articles in November of each year going back to 1851. In total, this chart comprises 1.2 million headlines and 81 million words.
<br>
{{< plotly json="/plotly/hedonometer/nyt-november-headlines.json" height="400px" >}}
<br>
In a year (2020), that seems so much worse than years in recent memory I take some solace for the general up and to the right nature of this chart. 

Here are some headlines from some of the more interesting points of this graph. 

**1856**

{{< plotly json="/plotly/hedonometer/nyt-twitter-rolling-avg.json" height="400px" >}}

## Notes

- Much of the data being used in this analysis is coming directly from the APIs that the Hedonometer team has graciously made publicly available and I want to thank the entire team at Vermont's Computational Story Lab for their work. The foundational paper describing their methodologies in detail can be found at this [link](https://arxiv.org/abs/1101.5120) and the Hedonometer's current home is [here](https://hedonometer.org/timeseries/en_all/). 

- I've also made heavy use of the public APIs of both Twitter and the New York Times. Links to their respective API documentation can be found [here](https://developer.twitter.com/en/docs) and [here](https://developer.nytimes.com/apis)

- Credit for introducing me to the Hedonometer is owed to Gimlet Media's Reply All podcast and the Hedonometer was featured in this episode: 
<iframe scrolling="no" frameborder="0" width="100%" height="152" allowtransparency="true" allow="encrypted-media" src="https://open.spotify.com/embed/episode/2AwPOVANlKj2GbmKRcBKYF"></iframe>

