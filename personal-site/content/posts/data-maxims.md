---
title: "Some Startup Data Maxims"
date: 2021-09-23T04:31:28Z
updated: 2021-09-23T04:31:28Z
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

To be perfectly honest, whenever I have gotten similar questions in the past I usually point people to some of the blogs and authors linked above. Suffice it to say but a lot has been written on this topic already. If there is one opportunity for me to add a unique perspective to this debate I think it is this. I haven't yet found a clear rule set that helps to guide aspiring data-driven companies as they navigate the many winding paths between making their first data hire and growing scalable data functions. So in one huge act of ego and bravado, I am here to lay out my ten ...

<p align="center">
    <img src="/img/data-maxims/10-commandments.gif">
</p>

... 5 data maxims to live by. 

## 5 Data maxims to live by
### 1. Start at the center
Especially in the very beginning, resist the urge to [specialize](https://erikbern.com/2021/07/23/what-is-the-right-level-of-specialization.html). It seems to me that normally it is somewhere between series A and B rounds, or roughly the 20-30 employee mark, when startups first look to hire data people. This is probably the right time to hire data people. But too often, the focus and job descriptions of the first data roles at these companies are way too narrow, i.e. `<Insert Department Here>` Data Scientist. More often than not, business teams have different data and analytical maturity curves, and -- borrowing from my own background -- it is totally normal that the risk or finance teams at a FinTech company will have bigger "data needs" in the beginning. However, I would advise against hiring your first data people directly into these business teams.

Why? Well, the problems those teams are trying to address are never actually that unique. Management reporting, predictive modeling, and data visualization are problem spaces that every team at your company will want to solve for and by specializing too early there is a risk of creating duplicative work across teams and missing out on an early opportunity to establish frameworks and best practices that will help to scale data adoption across the company.

What should you do instead? Hire people directly into a central data team. You might need to adopt different organizational structures as you continue to grow but for now the most important thing is to create best practices and tell your new data hires to focus on getting the basics right, think the bottom of the [data pyramid](https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007). Dotted lined reporting out of the central team is probably fine but its super important in the early days to get everyone using the same tools and speaking the same language. You'll want a strong foundation to build on otherwise you'll find yourself constantly trying to reconcile different disparate data pipelines, metrics, and pieces of analysis. 

### 2. Learn to embrace technical debt

If my last maxim was framed for the prospective CTO or CEO looking to make their first data hires, this next pearl of wisdom is for those first few data hires who walk through your company's doors. 

Don't worry about data meshes, event streaming, or any other pie-in-the-sky ivory tower idea that data academia is getting worked up about. The truth is your stakeholders don't care and probably never will. You also likely have another thing working against you. Popular culture has taught us to worship at the altar of the brilliant software engineer who through sheer force of will and Red Bulls has written thousands of lines of code through the night to deliver the feature that will immediately monetize and drive incredible value ... and we all just accept that whatever he or she did is incredibly complicated and impossible to understand ... at the same time your management team expects to have data on the performance of the new feature first thing tomorrow. 

<p align="center"><iframe width="560" height="315" src="https://www.youtube.com/embed/y8OnoxKotPQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

This stark contrast of expectations is something that most people who have worked in data will recognize. On the one hand, we are not totally blameless. Its our job to make sure that everyone is at least partially aware of the complexities surrounding the data platform and also that management is aware of the cost of doing business. At the same time, especially early on, its incredibly important that we demonstrate value through data. But ... and this is a big but ... this will likely mean that shortcuts will have to be taken. Shortcut here is analogous for creating some level of technical debt to drive immediate value, i.e. a fist full of python scripts dumping data into redshift on a cron job and planning on replacing this later with better infrastructure when time allows. 

Now, back to my CTO and CEO looking to make their first data hire. I strongly feel that the best leaders of nascent data teams can be differentiated by their ability to understand when and where to take short cuts without sacrificing too much optionality or pain in the long run. If you find this type of person, hire them. Cherish them. 

### 3. Everyone is a data owner and everyone is a data analyst

Who are we, [the purple people](https://blog.getdbt.com/we-the-purple-people/)? This dbt blog post is brilliant. But it was only after I read one of the accompanying linked posts by [Benn Stancil](https://benn.substack.com/p/analytics-is-at-a-crossroads) when the gears really started turning for me. 

<p align="center">
    <img src="/img/data-maxims/mind-blown.gif">
</p>

One of the best things that has happened to the data space in the last few years has been the increased tooling and technical skill set of people who work in data roles, see [rule 5](#5-the-data-platform-is-a-production-platform). In some ways, it has also been one of the worst things. In our quest to right the perceived wrong of being seen as less technical than the software engineers we work with, we fail to appreciate the technical and analytical skills of the stakeholders we support. I know I have been guilty of espousing the importance of "data democratization" within organizations but then throwing up blockers when team members didn't want to abandon their excel spreadsheets.

Funnily enough, I've also seen the other side of the coin working closely with many software engineers. Most engineers want to be good data partners and don't want to break data pipelines or dashboards if they can avoid it. At the largest and most "data mature" companies, engineers are able to maintain contracts between their applications and the data platform but at startups you are more often than not dumping data directly out of production databases and associated 3rd party apps with no contract and little schema management. Your engineers don't want to put you in a bad position, but if they need to get a feature out by a deadline and that means refactoring their microservice backend ...well ... dashboards be damned. 

Where am I going with this? Let's talk more about what I think it means for the future to be purple. This [one quote](https://blog.getdbt.com/we-the-purple-people/) really got me.

> Success in modern software engineering isn't measured by technical complexity but by clarity, reliability, agility and impact — it is a collaborative practice, grounded in an ecosystem of open tools that enable automating the rote mechanics and focusing on the higher order problems. The term engineering itself is derived from the Latin ingenium, meaning "cleverness" and ingeniare, meaning "to contrive, devise".  

Something I got wrong when I first started in data was that I thought that there was something inherently unique about the skill set that data scientists et. al. had. Sure there is a lot of math and some software knowledge, but nothing that can't be self taught by anyone with enough determination. "Being purple", which I believe most successful data teams are, means that you've acquired enough software know-how to translate between software engineers and applications on one side and business stakeholders on the other side. But then the end all be all for data teams can not be to live all by ourselves in the middle. We need to help make everyone around us "purple" as well. 

On one end, we need to help to empower business stakeholders to see themselves as analysts and data scientists by helping in whatever way we can to enable them to create their own insights and automation around data. Thankfully there is a lot of incredible things happening in the data automation and data application space these days that I'm sure will help push this trend along. On the other end, we need to help engineers and other technical stakeholders to see themselves as true data owners rather than data being purely a byproduct. And as I said before, most people want to be good partners. Its up to us to help build frameworks, processes, and systems that lower the burden of "data ownership" for technical teams. Again, I see a lot of amazing companies and products being developed to address this problem. 

I know I've probably put too many words into this already but one last thought here to really drive home what I am saying. I promise you that the bright lines we may perceive today that divide engineers from data people from business people are going to continue fade away. The best policy is to embrace this change head on and think critically about how your team or company can create a culture that encourages everyone to see themselves as a data owner and data analyst. 
### 4. Insights is a people business

This maxim, thankfully, will be brief. I would argue that if the goal of a data team is to produce insights that create business value or serve as basis for future data product, i.e. production ML models etc, then the value of the insight actually has nothing to due with its brilliance, clarity, buzz word, buzz word. Instead, all of the value comes from the actions that follow the insight itself. Without any subsequent action by a company, an insight is meaningless. Insights is a people business because if you can't convince anyone to actually do anything then there is no point. When hiring data people, don't lose sight of this fact and equally important, ask yourself if your organizational structure and culture will truly enable insights to influence people. 

### 5. The data platform is a production platform 

Okay so I realize that this last maxim may sound contradictory to [rule 3](#3-everyone-is-a-data-owner-and-everyone-is-a-data-analyst) and probably a little contradictory to [rule 2](#2-learn-to-embrace-technical-debt) but I assure you it is not. I'm not here to make an argument that every data team needs to be more technical and even more like software engineers who are regularly testing and deploying code into production. What I am arguing is that the data platform needs to be treated like an extension of the production platform and this does mean investing and adopting many of the best practices that have helped to enable more reliable software development. For me personally, it was my introduction to [dbt](https://blog.getdbt.com/what-exactly-is-dbt/) that really kicked down the door and helped me to imagine a world with CI/CD and multi-environment pre-release testing of the data platforms I worked with. Since then, the shear number of tools and companies that I have come across that are popping up to help make development and deployment of "data code" (don't know what else to call it) easier is incredible. 

Your data warehouse/platform is in all likelihood the first internal facing software product that the rest of your company interacts with. I am biased, but I also think it is the most important. Don't be afraid to invest time and money into making sure you have the same certainty around the quality of your data that you do around your customer facing applications. The earlier companies decide to do this the better. 

## The End

I have borrowed heavily from the works of others in this post and wherever I could I have tried to cite whatever I could. I want to acknowledge everyone who is putting out content and thinking critically about how to empower companies to be better with data. I wrote this post as my own small contribution to the cause. 

