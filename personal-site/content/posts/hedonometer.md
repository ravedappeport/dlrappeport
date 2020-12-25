---
title: "Hedonometer"
date: 2020-12-21T14:10:46Z
draft: false
plotly: true
---

## Background

About two months ago, I was introduced to a work of the University of Vermmont Computational Story Lab called the Hedonometer. At its core, the Hedonometer is a large scale NLP application based on Twitter data and is used to measure "happiness" at scale. The creators do a great job summarizing this here:


> **“What is being measured by the instrument?”** <br><br>
 hedonometer.org currently measures Twitter’s Decahose API feed (formerly Gardenhose). The stream reflects a 10% random sampling of the roughly  500 million messages posted to the service daily, comprising roughly 100GB of raw JSON each day. Words in messages we determine to be written  in English are thrown into a large bag containing roughly 200 million words per day. This bag is then assigned a happiness score based on the  average happiness score of the words contained within. While "bag-of-words" approaches can be problematic for small collections of text, we  have found the methodology to work well at the large scale.

My introduction to the Hedonometer came via Gimlet Media's Replay All podcast. I was always going to find a quantitative measure of global happiness interesting but what struck me most as I listened to the show's hosts talk to the creators of the Hedonometer was that this seemed like a cool project for me to try to recreate on my own. So ... that is exactly what I did and below are my attempts at trying to make sense of the Hedonometer as well as my own happiness and what the Hedonometer's methodology may about the news media today. 

## Sluething Around

At first, I spent multiple hours messing around with Twitter's API and open source NLP lexicon python packages (a colleague recommened vaderSentiment). What I quickly realized was the following:
1. It is not easy to get large quantities of historical data from Twitter
2. Most of the publicly available NLP sentiment analysis packages seem to follow a similar pattern
3. (and this is embarassing to admit because it took me multiple days to realize) hedonometer.org makes their lexicon scoring available via an api. 

The general idea employed by both the creators of the Hedonometer and Vader Sentiment is pretty similar. Crowdsource a bunch of people to rank words/emoticon on AWS Mechanical Turk and employ a rules based systemm to adjust total scores. Vaders rules set and lexicon are both fairly complex and involved, possibly suggestive of why Vader seems to perform better in my opinion (more on this later). Meanwhile, the Hedonometer seems to use a pretty simple adjustment to remove "neutral" words, words with scores between 4-6 on a 1-9 point scale.




## New York Times

{{< plotly json="/plotly/hedonometer/nyt-twitter-rolling-avg.json" height="400px" >}}

## Notes

- Much of the data being used in this analysis is coming directly from the APIs that the Hedonometer team has gratiously made publicly available and I want to thank the entire team at Vermont's Computational Story Lab for their work. The foundational paper describing their methodologies in detail can be found at this [link](https://arxiv.org/abs/1101.5120) and the Hedonometer's current home is [here](https://hedonometer.org/timeseries/en_all/). 

- I've also made heavy use of the public APIs of both Twitter and the New York Times. Links to their respective API documentation can be found [here](https://developer.twitter.com/en/docs) and [here](https://developer.nytimes.com/apis)

- Credit for introducing me to the Hedonometer is owed to Gimlet Media's Reply All podcast and the Hedonometer was featured in this episode: 
<iframe scrolling="no" frameborder="0" width="100%" height="152" allowtransparency="true" allow="encrypted-media" src="https://open.spotify.com/embed/episode/2AwPOVANlKj2GbmKRcBKYF"></iframe

