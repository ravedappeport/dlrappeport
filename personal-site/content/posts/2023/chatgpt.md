---
title: "ChatGPT"
date: 2023-03-26T15:59:40-0700
lastmode: 2023-03-26T15:59:40-0700
draft: false
plotly: true
description: "ChatGPT built a chess app"
summary: "I used ChatGPT to build a chess app. Here are some of my take-aways"
tags: ["chatgpt", "chess"]
categories: ["tech"]
---

## Background

AI was the biggest story in tech in 2022. In case you missed it, [here](https://stratechery.com/2022/the-2022-stratechery-year-in-review/) is a great write up from Ben Thompson and the product at the center of this story is Open AI's [ChatGPT](https://openai.com/blog/chatgpt). 

The very first time I had heard of Open AI or GPT was in 2020 when Calvin French-Owen wrote about his experience with GPT 3 on his [blog](https://calv.info/gpt-3-real-magic). My own experience with the GPT3 API didn't blow me away, but looking back at Calvin's first impression of GPT3 after spending a weekend building a web application with ChatGPT4, I think he hit the nail on the head with this observation:

> I think that’s where the real magic from the OpenAI API starts to come from. Yes, the model is really good. But even more than that… it’s really accessible.

<br>

## ChatGPT In its own words

<p align="center">
    <img src="/img/chatgpt/chatgpt-in-own-words.png">
</p>

<br>

## Building an App with ChatGPT

### The App

This is the app ChatGPT and I built: **[Lichess App](https://lichess-app.s3.amazonaws.com/index.html)**

<br>
First lets get some facts out of the way. 

1. I am not a professional web developer but I do work for companies that develop software
2. I have never before written or deployed a javascript application over the internet
3. The app I linked above was built in less than two days over a single weekend 

<br>

The app that I asked ChatGPT to help me build is a client facing front end that pulls chess data from the [lichess.org](https://lichess.org/api) api. First, the app gets information on the current top rated players of standard chess game variants, i.e. standard, bullet, blitz, etc. Then the app randomly selects one of these top players and requests a rated game that they played on lichess.org. The app then allows a user to walk through the game that was played by progressing the game forward or backward move by move or selecting a section from a component called "Move History" that moves the game to a given state. There is additional functionality that is relatively self explanatory, but it is worth noting that ChatGPT also helped me to style the application quite a bit including optimizing for smaller screens on mobile devices. The styling and customization is most evident in the chessboard itself as well as the buttons that move the game forward and backward or pull a new random game from lichess.org.

<br>

### What was it like?

I made rapid progress very early on with ChatGPT. I gave it a brief description of what I was trying to do and we were off to the races. I think that within 2-3 hours, I had most of the basic required functionality in place. When I needed to ask for more detail, ChatGPT was normally able to provide what I needed. I consider myself fairly technical and I do think that ChatGPT assumed a level of familiarity with web development that would be too much for someone with absolutely no technical experience to overcome, but at the same time I never told it that I was a complete novice. 

When I did encounter errors while developing, I was mostly able to copy and paste this information into the ChatGPT interface and most of the time, it was able to set me in the right direction. There were times when ChatGPT simply didn't know what to do and would put me into a loop that I would have to work through myself. I think this is actually one limitation of generative AI like ChatGPT right now. There is an assumption that ChatGPT always knows the answer and this is definitely not always the case. ChatGPT never conveys uncertainty to the user but at times I think that would be very helpful context. An example here might be "I think this is the best thing to try but I'm not sure". Another nit would be that ChatGPT is not a pair programmer. As a user, I had to pay attention to times when the model was repeating something it had told me to do in the past and quite often it would be describing a state of my code that was incorrect. Whenever this would happen, I was able to get ChatGPT back to a good state but this felt like a bit of a burden. 

Overall though, I found the experience of working with ChatGPT to build a web application to be fun, educational, sometimes frustrating, and sometimes jaw-dropping. I will never forget this particular exchange about an error that showed up in my console log.

<p align="center">
    <img src="/img/chatgpt/amazing-exchange.png">
</p>

Not only was ChatGPT able to correctly identify where in my code the error was occurring but the AI demonstrated a remarkable understanding of both Chess PGN notation and different types of Chess variants. I'm still a novice when it comes to chess and I can easily see how a bug in my code like this would take me an incredible amount of time to figure out. 

## Conclusion

> ... But even more than that… it’s really accessible.

ChatGPT can certainly help you create new software from scratch but I don't think it can actually develop an application all on its own especially one that is fairly specialized, well designed, and delightful to human users. That being said, I do think that there will be generative AI that can do this in the not too distant future. 


I work in tech and I'm an early adopter of new technologies especially those that have the ability to disrupt the industry I work in. Over the weekend, I showed ChatGPT4 to my future mother-in-law. She is a teacher and she asked ChatGPT4 to help her write a template of a report card for a child who is struggling to retain information and apply it while using language that is careful not to cause too much concern for parents. I wasn't surprised when ChatGPT created a template that was well written and emotionally nuanced. What I hadn't fully considered until that moment was that AI was now accessible and usable by everyone with access to a computer and the internet. To date we've used AI to help us find content. Google is incredible at recommending links. Youtube and TikTok can recommend videos that entertain us. Every child these days knows how to ask the internet for information, but every child in the future will know how to use the internet to create.

<p align="center">
    <img src="/img/chatgpt/closing-remark-gpt.png">
</p>

*Editorial Note*
<br>
I want to thank [lichess.org](https://lichess.org/about) for being an incredible community of people who are passionate about chess and open-source software. I only thought of this project after coming across their website and don't think it would have been possible without them.