---
title: "Sleep, TLS, and HTTP Proxies"
date: 2022-11-18T08:22:35-0500
lastmode: 2022-11-18T08:22:35-0500
draft: true
plotly: true
description: "Learning to proxy my phone network traffic to get more data from my apps"
summary: "A little bit about sleep and a lot about internet security"
tags: ["internet", "running", "security", "data", "sleep", "health"]
categories: ["health"]
---

## Background

When I decided to get more serious about running, I made an investment in a running watch. Wirecutter and Amazon reviews led me to purchase the [COROS Apex Pro](https://www.amazon.com/Coros-Premium-Multisport-Watch-Black/dp/B07XZHKM7R). Compared to similarly priced running watches, the Apex Pro had two killer features for me: 
1. It has an incredible battery life 
2. It tracks different sleep statistics that I was interested in. 

COROS, like Garmin and other similar companies, offers a smart phone app that is free to use with purchase of a compatible watch. COROS's app is beautifully designed and I love it but its big flaw (for me) is that I can't easily bulk export my sleep or other health data that the app has access to. 

Not to be stopped from getting what I want. I learned that I can "trick" COROS's servers to sending me the data I want by proxying and modifying the network traffic being sent from my iPhone to COROS. This post is an exploration into why I wanted my sleep data so badly and some of the things that I learned about proxy servers and internet security. 

## Why do I care about sleep?

A few months ago, a friend recommended that I read Matthew Walker's "Why We Sleep". 

<p align="center">
<iframe type="text/html" sandbox="allow-scripts allow-same-origin allow-popups" width="336" height="550" frameborder="0" allowfullscreen style="max-width:100%" src="https://read.amazon.com/kp/card?asin=B06ZZ1YGJ5&preview=inline&linkCode=kpe&ref_=cm_sw_r_kb_dp_DFX815KW310V447DERDE" ></iframe>
</p>

Prior to reading this book, I had always been someone who prided himself on my ability to function on little to no sleep. In high school, I would volunteer as an EMT once a week every Thursday and that meant I came to school most Fridays without really sleeping. In college, I would frequently pull all nighters before important exams or due dates. I never thought this was a problem. In fact, I was proud of my ability "not sleep". As an adult, there was less need to be up all night for School or extra curricular activities, but, I never truly prioritized it. This book completely shifted my way of thinking!!!

It turns out that prolonged, habitual lack of sleep is highly correlated with both academic performance and chronic illness. An [MIT study](https://www.nature.com/articles/s41539-019-0055-z) published in Nature, found that Sleep measures accounted for nearly 25% of the variance in academic performance. Studies linking persistent lack of sleep to chronic illness such as cancer have not always been conclusive, however, one [large scale study](https://pubmed.ncbi.nlm.nih.gov/22295122/) in Europe found the following: 

> Results: During a mean follow-up period of 7.8 years 841 incident cases of type 2 diabetes, 197 cases of myocardial infarction, 169 incident strokes, and 846 tumor cases were observed. Compared to persons sleeping 7-<8 h/day, participants with sleep duration of <6 h had a significantly increased risk of stroke (Hazard Ratio (HR) = 2.06, 95% confidence interval (CI): 1.18-3.59), cancer (HR = 1.43, 95% CI: 1.09-1.87), and overall chronic diseases (HR = 1.31, 95% CI: 1.10-1.55) in multivariable adjusted models. Self-reported daytime sleep at baseline was not associated with incident chronic diseases in the overall study sample. However, there had been an effect modification of daytime sleep by hypertension showing that daytime sleep was inversely related to chronic disease risk among non-hypertensive participants but directly related to chronic diseases among hypertensives.

I had to quickly google [Hazard Ratio](https://en.wikipedia.org/wiki/Hazard_ratio)(s) but it turns out they are simple to interpret. The post from the study above found that people who self reported an average of less than 6 hours of sleep per day were twice as likely to suffer a stroke, ~40% more likely to develop cancer, and ~30% more likely to have any chronic disease compared to participants. This study has been cited by over 200 other academic papers and, on a personal note, stats like this have floored me. I want to also point out that only recently are we in a day and age where many people have fitness trackers that they are wearing to bed and tracking sleep. The findings from the potsdam study relied on self-reported data. In the next couple years, I expect Sleep Research to become more mainstream and influential within Healthcare as the size and accuracy of data improves. 

**Why do I care about sleep?** It might be the single, greatest contributing factor related to improved mental performance and long term health outcomes and it is mostly within my control. 

## What does a proxy server look like?

Ok, time for some technical stuff. 

Put simply and according to [Wikipedia](https://en.wikipedia.org/wiki/Proxy_server), a proxy is a server application that sits in between a client requesting resources and a server providing that resource. For my purposes, I want to a proxy server that can sit between my iPhone and COROS's application servers. 

<div style="text-align: center;">

![mitmproxy image](https://docs.mitmproxy.org/stable/schematics/how-mitmproxy-works-explicit.png)

</div>

Two very good, mostly free proxy applications I found on the web are [mitmproxy](https://mitmproxy.org/) and [Charles Proxy](https://www.charlesproxy.com/).

## What is TLS anyways?

This video helps does a good job going into the nitty gritty. 

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/cuR05y_2Gxc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

Here is my admittedly amateur understanding of TLS. [TLS](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) stands for Transport Layer Security and that little "s" in "https" means that the website server you are communicating with is using some version of TLS to ensure that the network traffic between your computer and that server is secure. Secure here means that the packets of information being sent back and forth are encrypted and only your browser and the server have the means to decrypt them -- *assuming you're not being spied on by a nation state actor with a super computer powerful enough to brute force the encryption*. 


The "TLS Handshake" is both incredibly common and incredibly important to how the internet works. Literally every website you visit (well almost every) will engage with your browser in a TLS handshake prior to doing anything else. How does it work? Public private key magic! Here is my brief story to help explain how TLS works


<span style="color:violet">
First your browser reaches out to the server and says "Hello, I am Dave and I can speak one of seven different encryption languages." Next the server responds by saying "Hello Dave! I am xAYSxAyz9 server. Here is my ID card (certificate) to prove I am who I say I am. You said you speak gobble gook. Let's communicate that way! Here is a password (public key) you can use to securely communicate with me". Because metaphorical me or my friends have been burned one too many times by servers pretending to be someone they aren't, I decide to take a close look at the certificate. I want to make sure a trusted third party, a certificate authority, has put their signature on the certificate so that I know I can trust it. I want to beware of self-signed, i.e. probably fake certificates like the fake IDs kids try to pass by bouncers at bars before they turn 21. This server's ID looks good!. Next I tell the server "OK xAYSxAyz9. I trust you are who you say you are. But I want to be extra careful, so let me create a new password (shared secret) that we can use to communicate." I create the shared secret, then I use the server's public key and the gobble gook alrgorithm to encrypt it. "Here you go server. Let's use this new password (encrypted) to communicate!" The server takes this new encrypted password and decrypts it using the private key associated with its public key. Now both myself and the server have the same shared key we can use to communicate privately and bingo bango we are off to the races.
</span>

**What is the difference between HTTP and HTTPS you might ask?** HTTPS is "secure" meaning it requires encryption via TLS whereas HTTP does not. Most modern browsers heavily discourage users from interacting with websites that do not have HTTPS. 

**What does TLS and SSL certificates have to do with proxies anyways?** If you want to see the network traffic being sent between your smart phone apps and those app's servers, you need to get in between the TLS communication happening between your phone and the server. In order to do this, you'll need to set up an HTTPS proxy server to sit in between your phone and the app server. Your phone needs to trust this HTTPS proxy server and trust here means that your proxy server needs to have access to a valid certificate from a certificate authority. When you put all these things together you'll have your smart phone communicating securely with your proxy server via TLS and your proxy server communicating securely with the app servers via TLS.

## Data and stuff

{{< plotly json="/plotly/sleep-proxy/total-sleep.json" height="400px" >}}

{{< plotly json="/plotly/sleep-proxy/deep-sleep.json" height="400px" >}}

{{< plotly json="/plotly/sleep-proxy/weekday-total-sleep.json" height="400px" >}}