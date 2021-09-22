---
title: "Some Startup Data Maxims"
date: 2021-09-19T23:42:45Z
draft: false
description: "Strong convictions loosely held about how to build data teams and data infrastructure"
summary: "I've sat on the fence for a while about writing this post. Here are some strong convictions loosely held about data teams and data infrastructure at startups"
tags: ["startup","management","infrastructure","organization"]
categories: ["startups"]
---

<p align="center">
    <img src="/img/data-maxims/lumbergh-data.jpeg">
</p>

## Background
Sometimes life finds a way of telling you to sit down and write a blog post. The same week that a friend of a friend asked me for some advice around making the first data hire at his startup [Erik Bernhardsson's](https://erikbern.com/2021/07/07/the-data-team-a-short-story.html) fictional narrative about building data teams at startups was going viral. Many in the Analytics blogo-sphere took notice or have been writing about similar things for a long time. What is the modern data [experience](https://benn.substack.com/p/the-modern-data-experience#footnote-1)? What [color](https://blog.getdbt.com/we-the-purple-people/) best describes data people? What is the future of the [data platform](https://erikbern.com/2021/07/07/the-data-team-a-short-story.html)? Are analysts honeydew or are they [cantaloupe](https://benn.substack.com/p/third-rail)?

To be perfectly honest, whenever I have gotten similar questions in the past I usually point people to some of the blogs and authors linked above. Suffice it to say but a lot has been written on this topic already. If there is one opportunity for me to add a unique perspective to this debate I think it is this. I haven't yet found a clear rule set that helps to guide aspiring data-driven companies as they navigate the many winding paths between making their first data hire and growing scalable data functions. In my own experience, I have encountered many difficult trade-offs and decisions that aren't always obvious. So in one huge act of ego and bravado, I am setting out to create ten ...

<p align="center">
    <img src="/img/data-maxims/10-commandments.gif">
</p>

... 5 data ~~commandments~~ maxims to live by. 

## 5 Data maxims to live by
### 1. Start at the center
Especially in the very beginning, resist the urge to [specialize](https://erikbern.com/2021/07/23/what-is-the-right-level-of-specialization.html). It seems to me that normally it is somewhere between series A and B rounds, or roughly the 20-30 employee mark, when startups first look to hire data people. This is probably the right time to hire data people, i.e. after you've first stood up and built "the thing" you now want to better understand and optimize "the thing". But too often, the focus and job descriptions of the first data roles at a company are way too narrow, i.e. {Insert Department Here} Data Scientist. More often than not, business teams have different data and analytical maturity curves, and -- borrowing from my own background -- it is totally normal that the Risk or Finance teams at a FinTech company will be a bigger data stakeholder in the early days of company's life cycle. However, I would advise against hiring your first data people directly into these business teams to focus solely on the problems those teams are facing today. 

Why? Well to put it as succinctly as I can, the problems those teams are trying to address are not actually that unique. Management reporting, predictive modeling, and data visualization are problem spaces that every team at your company will want to solve for and by specializing too early there is a risk of creating duplicative work across teams and missing out on an early opportunity to establish frameworks and best practices that will help to scale data adoption across the company.

What should you do instead? Hire people directly into a central data team. You might need to adopt different organizational structures as you continue to grow and discover bottlenecks in your incoming work queue from your stakeholders but for now the most important thing is to create best practices and tell your new data hires to focus on getting the basics right, think the bottom of the [data pyramid](https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007). Dotted lined reporting out of the central team is probably fine but its super important in the early days to get everyone using the same tools and speaking the same language. You'll want a strong foundation to build on otherwise you'll find yourself constantly trying to reconcile different disparate data pipelines and pieces of analysis. 

### 2. Learn to embrace technical debt

If my last maxim was framed for the prospective CTO or CEO looking to make their first data hires, this next pearl of wisdom to those first few data hires who walk through your companies doors. 

Don't worry about data meshes, event streaming, or any other pie-in-the-sky ivory tower idea that data academia is getting worked up about. The truth is your end users don't care and probably never will. You also probably have another thing working against you. Hollywood, Silicon Valley, and popular culture have taught us to worship at the altar of the brilliant software engineer who through sheer force of will and Red Bull has written thousands of lines of code through the night to deliver the feature that immediately monetizes and drives incredible value ... and we all just accept that whatever he or she did is incredibly complicated and impossible to understand ... at the same time your management team expects to have data on the performance of the new feature in no time at all. 

<p align="center"><iframe width="560" height="315" src="https://www.youtube.com/embed/y8OnoxKotPQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

This stark contrast of expectations is something I feel most people who have worked in data will emphasize with. On the one hand, we are not totally blameless. Its our job to make sure that everyone is at least partially aware of the complexities surrounding the data platform and also that management is aware of the cost of doing business, see [rule 3](#3-everyone-is-a-data-owner-and-everyone-is-a-data-analyst). At the same time, especially early on, its incredibly important that we demonstrate value through data, but ... and this is a big but ... this will likely mean that shortcuts will have to be taken. Shortcut here is short code for asking some level of technical debt to drive immediate value, i.e. a fist full of python scripts dumping data into redshift on a cron job, and planning on replacing this later with better infrastructure when time allows. 

Now, back to my CTO and CEO looking to make their first data hire. I strongly feel that the best leaders of nascent data teams can be differentiated by their ability to understand when and where to take short cuts without sacrificing too much optionality or pain in the long run. 

### 3. Everyone is a data owner and everyone is a data analyst

Who are we, [the purple people](https://blog.getdbt.com/we-the-purple-people/), who help businesses to build process and applications around data? One of the best things that has happened to the data space in the last few years has been the increased tooling and technical skill set of people who work in data roles, see [rule 5](#5-the-data-platform-is-a-production-platform). In some ways, it has also been [one of the worst things](https://benn.substack.com/p/analytics-is-at-a-crossroads).


### 4. Insights is a people business

### 5. The data platform is a production platform 

