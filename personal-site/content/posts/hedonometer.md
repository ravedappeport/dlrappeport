---
title: "Hedonometer"
date: 2020-12-21T14:10:46Z
draft: false
---

## Background

About two months ago, I was introduced to a work of the University of Vermmont Computational Story Lab called the Hedonometer. At its core, the Hedonometer is a large scale NLP application based on Twitter data and is used to measure "happiness" at scale. The creators do a great job summarizing this here:


> **“What is being measured by the instrument?”** <br><br>
 hedonometer.org currently measures Twitter’s Decahose API feed (formerly Gardenhose). The stream reflects a 10% random sampling of the roughly  500 million messages posted to the service daily, comprising roughly 100GB of raw JSON each day. Words in messages we determine to be written  in English are thrown into a large bag containing roughly 200 million words per day. This bag is then assigned a happiness score based on the  average happiness score of the words contained within. While "bag-of-words" approaches can be problematic for small collections of text, we  have found the methodology to work well at the large scale.


The foundational paper describing their methodologies in detail can be found at this [link](https://arxiv.org/abs/1101.5120) and the Hedonometer's current home is [here](https://hedonometer.org/timeseries/en_all/). 

My introduction to the Hedonometer came via Gimlet Media's Replay All podcast and what struck me most as I listened to the show's hosts talk to the creators of the Hedonometer was that this seemed like a cool project for me to try to recreate on my own. So ... that is exactly what I did and below are my attempts at trying to make sense of the Hedonometer as well as my own happiness and what the Hedonometer's methodology says about the news media today. 

## Sluething 


## Notes

- Much of the data being used in this analysis is coming directly from the APIs that the Hedonometer team has gratiously made publicly available and I want to thank the entire team at Vermont's Computational Story Lab for their work

- I've also made heavy use of the public APIs of both Twitter and the New York Times. Links to their respective API documentation can be found [here](https://developer.twitter.com/en/docs) and [here](https://developer.nytimes.com/apis)

- Credit for introducing me to the Hedonometer is owed to Gimlet Media's Reply All podcast and the Hedonometer was featured in this episode: 
<iframe scrolling="no" frameborder="0" width="100%" height="152" allowtransparency="true" allow="encrypted-media" src="https://open.spotify.com/embed/episode/2AwPOVANlKj2GbmKRcBKYF"></iframe

