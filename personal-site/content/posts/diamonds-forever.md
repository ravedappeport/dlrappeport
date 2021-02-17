---
title: "Diamonds Forever"
date: 2021-02-17T05:37:13Z
draft: false
plotly: true
---

Time for a brief personal note. On January 29th 2021, I took the big leap and proposed to my girlfriend, Emma, at L'Auberge Resort in Sedona, Arizona. Thankfully, she said yes and we had an amazing weekend together. This photo below was taken by our photographer minutes after the proposal and captures a moment of pure bliss.
<br><br>
![victory-photo](/img/diamonds-forever/victory-photo.JPG)
<br>
While I could definitely write more about the weekend we had, I am instead going to spend the rest of this post writing about something I wish I had found better information about online. 

## Background

If you are like me when I was going through the process of looking for a diamond engagement ring online, I suspect that at times you will waffle between feelings of extreme uncertainty about what you are purchasing to feelings of extreme blasè or as Drake says, YOLO. The advice I seemed to collect from chatting with most of my engaged or married friends was, learn the 4 Cs (Cut, Color, Clarity, Carat) and to quote my friend Catherine, "*if you love her, spend all your money*". Eventually, I did purchase a ring -- I won't disclose from where or how much I spent -- and my fiancè and I are quite happy with it. Looking back on the experience though, I was left wanting for more in-depth information about what diamonds cost and a better explanation why. Lo and behold, here we are.

## Digging for Diamond Data

Apparently there is already a well known public diamond dataset that is used frequently by the data science community. The popular python visualization package, Seaborn, installs with the [dataset](https://github.com/mwaskom/seaborn-data) by default. I probably could have saved myself a lot of time by making use of the public dataset, but I do not feel that the data accurately represents the diamonds and prices that I came across when I myself was looking at diamonds online.  

My approach then was to pull diamond data from three of the largest online diamond engagement ring sites:
- [Blue Nile](https://www.bluenile.com/)
- [Brilliant Earth](https://www.brilliantearth.com/)
- [James Allen](https://www.jamesallen.com/)

If you were to scroll through each of these sites, you will likely find that they all have a very similar UX flow. In fact, I wouldn't be surprised if the same third party company designed the "diamond search" feature of all three of their websites. My original thought was to try to use [Selenium](https://selenium-python.readthedocs.io/installation.html#introduction), a web acceptance testing framework that is also useful for manipulating DOM objects and web scraping. Spending maybe 1 or 2 days mucking about with Selenium, I came to the conclusion that the dynamic html tables I was trying to manipulate were too complex and the technique I opted for instead was look through the network calls being made in a development window until I found the call to XYZ's website backend that was returning the data. Next, I simply used python's request library to send repeated calls to each websites backend while I manipulated the carat parameter in the request query parameters in order to steadily return different result sets.

**NOTE!!!** **DO NOT**. I repeat, **DO NOT**, mimic this method if you share an IP address with your fiancè to be and/or are not making these requests behind a VPN. For about a month, any and all programmatic advertising I saw was for diamond engagement rings. Not surprising, given my IP address was logged making thousands of requests to each of these sites but it was problematic because I had started collecting the data before I had been able to propose and I then had to live in constant worry that Emma would grow suspicious of all the diamond advertising she was seeing. 

<br>
{{< plotly json="/plotly/diamonds-forever/diamond-carat-price-chart.json" height="400px" >}}
<br>