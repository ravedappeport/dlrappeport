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

This is the app ChatGPT and I built: **[ChatGPT Lichess App](https://lichess-app.s3.amazonaws.com/index.html)**

<br>
First lets get some facts out of the way. 

1. I am not a professional web developer but I do work for companies that develop software deployed over the internet
2. I have never before written or deployed a javascript application over the internet
3. The app I linked above was built in less than two consecutive days
<br>

The app that I asked ChatGPT to help me build is a client facing front end that pulls chess data from the [lichess.org](https://lichess.org/api) api. First, the app gets information on the current top rated players of standard chess game variants, i.e. standard, bullet, blitz, etc. Then the app randomly selects one of these top players and requests a rated game that they played on lichess.org. The app then allows a user to walk through the game that was played by progressing the game forward or backward move by move or selecting a section from a component called "Move History" that moves the game to a given state. There is additional functionality that is relatively self explanatory, but it is worth noting that ChatGPT also helped me to style the application quite a bit including optimizing for smaller screens on mobile devices. The styling and customization is most evident in the chessboard itself as well as the buttons that move the game forward and backward or pull a new random game from lichess.org.


