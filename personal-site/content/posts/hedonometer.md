---
title: "Hedonometer"
date: 2020-12-21T14:10:46Z
lastmod: 2021-09-19T20:08:33Z
draft: false
plotly: true
description: "An attempt to create a simplified version of the University of Vermont's Hedonometer and see what we can do with it"
tags: ["trump", "twitter","hedonometer","sentiment analysis"]
categories: ["data science"]
---

## Background

About two months ago, I was introduced to a work of the University of Vermont Computational Story Lab called the Hedonometer. At its core, the Hedonometer is a large scale NLP application based on Twitter data and is used to measure "happiness" at scale. The creators do a great job summarizing this here:

> **“What is being measured by the instrument?”** <br><br>
 hedonometer.org currently measures Twitter’s Decahose API feed (formerly Gardenhose). The stream reflects a 10% random sampling of the roughly  500 million messages posted to the service daily, comprising roughly 100GB of raw JSON each day. Words in messages we determine to be written  in English are thrown into a large bag containing roughly 200 million words per day. This bag is then assigned a happiness score based on the  average happiness score of the words contained within. While "bag-of-words" approaches can be problematic for small collections of text, we  have found the methodology to work well at the large scale.

My introduction to the Hedonometer came via Gimlet Media's Replay All podcast. I was always going to find a quantitative measure of global happiness interesting but what struck me most as I listened to the show's hosts talk to the creators of the Hedonometer was that this seemed like a cool project for me to try to recreate on my own. So ... that is exactly what I did and below is a brief write-up of my attempt. 

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

One of the more interesting applications I could think of for my hedonometer was to do an analysis of the news media. As it turns out, the New York Times has fantastic, public APIs specifically the `archive` endpoint. 

>The Archive API returns an array of NYT articles for a given month, going back to 1851. Its response fields are the same as the Article Search API. The Archive API is very useful if you want to build your own database of NYT article metadata. You simply pass the API the year and month and it returns a JSON object with all articles for that month. The response size can be large (~20mb).

Here is a look at average hedonometer scores for articles each month of each year going back 100 years to 1920.
<br>
{{< plotly json="/plotly/hedonometer/nyt-hist-headlines.json" height="400px" >}}
<br>
In the chart above, `NYT Headlines` refers to the rolling 12 month average hedonometer score for all front page New York Times headlines and `NYT Abstract` refers to the rolling 12 month average hedonometer score of all front page New York Times article abstracts, i.e. normally 2 to 3 sentence summaries of each story. With 2020 being a year that seems so much worse than others in recent memory, I take some solace for the general up and to the right nature of this chart. That said, it is hard to ignore that rather precipitous drop in happiness that took place in 2020 and there has not been evidence of anything quite like it in the last 20 years. 

The chart also highlights that on average headlines are "unhappier" than their respective abstracts. I don't find this surprising and anecdotally I suspect that language in headlines is meant to grab attention and thus will use words that have more extreme hedonometer scores without fully providing the same context that is available in the article abstract. This doesn't explain the pervasive trend of headlines being more unhappy than happy compared to the articles they are attached to.

The University of Vermont's Hedonometer has a clever mathematical operation for determining which words had the greatest contribution for the delta in average happiness from one period to another called *Word Shifts*. It could be an interesting follow up to this analysis to calculate the period over period word shifts but for the time being I've decided against digging in too much further just given the size of the data involved that I've sucked down onto my laptop locally. The chart above represents analysis of over 44 million words and 26.4 gb of json responses. 

All of that being said, I think its still interesting to just look at a random sampling of the front page headlines and articles for some of the bigger inflection points in this time series. The dates below represent a random selection of some of the larger inflections in the `NYT Abstract` time series.

**October 1940**
>TOKYO AMERICANS HEED U.S. WARNINC TO FLEE FAR EAST; 100 Wives and Children of Business Men Sail--Many Passages Are Booked SHANGHAI AWAITS LINERS Hull Says Plenty of Ships Will Be Available to Bring Back Citizens From Orient
 reservists in Shanghai get physical exams; to rept for duty
 

>Willkie Says 'Common Law' Of Nation Bars Third Term; He Asserts in Louisville New Dealers Seek End of Two-Party System--Insists Roosevelt Caused Arms Lag
 Willkie s, Louisville; text; tours Ill and Ind; s, Indianapolis
 
 **December 1964**
 >Weary Pope Returns From India to Joyful Welcome
 Pope returns to Rome; illus; Turkish Air Force jet buzzes his plane; flight described
 

>Front Page 3 -- No Title
 CANCER AND VIRUSES. Free lecture for the public tonight. 8:30. N. Y. Academy of .Medicine, 2 E. 105.&#8212; Adit.
 

 **February 2001**
 >It's Not Just AT&T: How Telecom Became a Black Hole
 Floyd Norris comment on continuing descent of telecommunications industry; blames situation on too much capital investment and economic slowdown; says financial markets have still not fully discounted pain to come, and neither have rosy economic forceasts that assume economic slowdown will be brief one; cites financial problems at AT&T, Lucent Technologies, France Telecom, British Telecommunications, Deutsche Telekom, VoiceStream Wireless and Nortel Networks; graph (M)
 

>Seton Hall Wonders After Loss To Syracuse
 Syracuse defeats Seton Hall, 63 to 62, in college basketball; photos (M)
 
 **September 2020**
 >Inside eBay’s Cockroach Cult: The Ghastly Story of a Stalking Scandal
 “People are basically good” was eBay’s founding principle. But in the deranged summer of 2019, prosecutors say, a campaign to terrorize a blogger crawled out of a dark place in the corporate soul.
 

>How Colleges Became the New Covid Hot Spots
 Like meatpacking plants and nursing homes early in the pandemic, campuses across the country are experiencing outbreaks.
 

## The New York Times and Twitter
{{< plotly json="/plotly/hedonometer/nyt-twitter-rolling-avg.json" height="400px" >}}
<br>
Lastly, I wanted to compare hedonometer scores for Twitter from hedonometer.org directly to the scores I was calculating for New York Times front page headlines and abstracts. The chart above shows rolling 30 day averages for all three. Up until 2020, there isn't really any evidence of strong correlation between Twitter and the front page of the New York Times, but we can see how in 2020 both time series experience 2 large negative dips, first around the emergence of the Coronavirus and second around the protests against police brutality that occurred over the summer. I'm not surprised to find that in general Twitter appears to be a happier place than the front page of the New York Times, but I was surprised to see how consistently the New York Times front page is much, much unhappier. As someone who is addicted to constantly refreshing the NYT app on my iPhone this summer perhaps I should consider spending a bit more time on Twitter instead.  

## Notes

I hope you found this post enjoyable. All of the code behind this analysis is publicly available on github for those who are curious. 

- Much of the data being used in this analysis is coming directly from the APIs that the Hedonometer team has graciously made publicly available and I want to thank the entire team at Vermont's Computational Story Lab for their work. The foundational paper describing their methodologies in detail can be found at this [link](https://arxiv.org/abs/1101.5120) and the Hedonometer's current home is [here](https://hedonometer.org/timeseries/en_all/). 

- I've also made heavy use of the public APIs of both Twitter and the New York Times. Links to their respective API documentation can be found [here](https://developer.twitter.com/en/docs) and [here](https://developer.nytimes.com/apis)

- Credit for introducing me to the Hedonometer is owed to Gimlet Media's Reply All podcast and the Hedonometer was featured in this episode: 
<iframe scrolling="no" frameborder="0" width="100%" height="152" allowtransparency="true" allow="encrypted-media" src="https://open.spotify.com/embed/episode/2AwPOVANlKj2GbmKRcBKYF"></iframe>

