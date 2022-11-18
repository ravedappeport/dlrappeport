---
title: "Learning about TLS and proxies to see if I am sleeping better at night"
date: 2022-11-18T08:22:35-0500
lastmode: 2022-11-18T08:22:35-0500
draft: true
plotly: true
description: "Learning to proxy my phone network traffic to get more data from my apps"
summary: "A little bit about sleep and a lot about internet security"
tags: ["internet", "running", "security", "data", "sleep"]
categories: ["misc"]
---

## Background

When I decided to get more serious about running, I made an investment in a running watch. Wirecutter and Amazon reviews led me to purchase the [COROS Apex Pro](https://www.amazon.com/Coros-Premium-Multisport-Watch-Black/dp/B07XZHKM7R). Compared to similarly priced running watches, the Apex Pro had two killer features for me: 
1. It has an incredible battery life 
2. It tracks different sleep statistics that I was interested in. 

COROS, like Garmin and other similar companies, offers a smart phone app that is free to use with purchase of a compatible watch. COROS's app is beautifully designed and I love it but its big flaw (for me) is that I can't easily bulk export my sleep or other health data that the app has access to. 

Not to be stopped from getting what I want. I learned that I can "trick" COROS's servers to sending me the data I want by proxying and modifying the network traffic being sent from my iPhone to COROS. This post is an exploration into why I wanted my sleep data so badly and some of the things that I learned about proxy servers and internet security. 

## Why do I care about sleep?

## What does a proxy server look like?

## What is TLS anyways?

This video helps does a good job going into the nitty gritty. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/cuR05y_2Gxc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Here is my admittedly amateur understanding of TLS. [TLS](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) stands for Transport Layer Security and that little "s" in "https" means that the website server you are communicating with is using some version of TLS to ensure that the network traffic between your computer and that server is secure. Secure here means that the packets of information being sent back and forth are encrypted and only your browser and the server have the means to decrypt them -- *assuming you're not being spied on by a nation state actor with a super computer powerful enough to brute force the encryption*. 


The "TLS Handshake" is both incredibly common and incredibly important to how the internet works. Literally every website you visit (well almost every) will engage with your browser in a TLS handshake prior to doing anything else. How does it work? Public private key magic! Here is my brief story to help explain how TLS works


<span style="color:violet">
First your browser reaches out to the server and says "Hello, I am Dave and I can speak one of seven different encryption languages." Next the server responds by saying "Hello Dave! I am xAYSxAyz9 server. Here is my ID card (certificate) to prove I am who I say I am. You said you speak gobble gook. Let's communicate that way! Here is a password (public key) you can use to securely communicate with me". Because metaphorical me or my friends have been burned one too many times by servers pretending to be someone they aren't, I decide to take a close look at the certificate. I want to make sure a trusted third party, a certificate authority, has put their signature on the certificate so that I know I can trust it. I want to beware of self-signed, i.e. probably fake certificates like the fake IDs kids try to pass by bouncers at bars before they turn 21. This server's ID looks good!. Next I tell the server "OK xAYSxAyz9. I trust you are who you say you are. But I want to be extra careful, so let me create a new password (shared secret) that we can use to communicate." I create the shared secret, then I use the server's public key and the gobble gook alrgorithm to encrypt it. "Here you go server. Let's use this new password (encrypted) to communicate!" The server takes this new encrypted password and decrypts it using the private key associated with its public key. Now both myself and the server have the same shared key we can use to communicate privately and bingo bango we are off to the races.
</span>

**What is the difference between HTTP and HTTPS you might ask?** HTTPS is "secure" meaning it requires encryption via TLS whereas HTTP does not. Most modern browsers heavily discourage users from interacting with websites that do not have HTTPS. 

**What does TLS and SSL certificates have to do with proxies anyways?** If you want to see the network traffic being sent between your smart phone apps and those app's servers, you need to get in between the TLS communication happening between your phone and the server. In order to do this, you'll need to set up an HTTPS proxy server to sit in between your phone and the app server. Your phone needs to trust this HTTPS proxy server and trust here means that your proxy server needs to have access to a valid certificate from a certificate authority. When you put all these things together you'll have your smart phone communicating securely with your proxy server via TLS and your proxy server communicating securely with the app servers via TLS.

## Data and stuff