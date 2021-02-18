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
While I could definitely write more about the weekend we had, I am instead going to spend the rest of this post writing about something I wish I had found better information about online before I proposed, diamond engagement rings.

## Background

If you are like me when I was going through the process of looking for a diamond engagement ring online, I suspect that at times you will waffle between feelings of extreme uncertainty about what you are purchasing to feelings of extreme blasè or as Drake says, YOLO. The advice I seemed to collect from chatting with most of my engaged or married friends was, learn the 4 Cs (Cut, Color, Clarity, Carat) and to quote my friend Catherine, "*if you love her, spend all your money*". While this is sage advice and I did eventually purchase a ring -- I won't disclose from where or how much I spent -- I was left wanting for more in-depth information about what diamonds cost and a better explanation why. Lo and behold, here we are. 

My strategy for figuring out why diamonds cost what they do in two parts:
1. Scrape a ton of diamond data from popular online engagement ring sites
2. Build predictive models to ascertain what features are most important to diamond price

## Digging for Diamond Data

Apparently there is already a well known public diamond dataset that is used frequently by the data science community. The popular python visualization package, Seaborn, installs with the [diamonds dataset](https://github.com/mwaskom/seaborn-data) by default. I probably could have saved myself a lot of time by making use of the public dataset, but I do not feel that the data accurately represents the diamonds and prices that I came across when I myself was looking at diamonds online.  

My approach then was to pull diamond data from three of the largest online diamond engagement ring sites:
- [Blue Nile](https://www.bluenile.com/)
- [Brilliant Earth](https://www.brilliantearth.com/)
- [James Allen](https://www.jamesallen.com/)

If you were to scroll through each of these sites, you will likely find that they all have a very similar UX flow. In fact, I wouldn't be surprised if the same third party company designed the "diamond search" feature of all of their websites. My original thought was to try to use [Selenium](https://selenium-python.readthedocs.io/installation.html#introduction), a web acceptance testing framework that is also useful for manipulating DOM objects and web scraping. Spending maybe 1 or 2 days mucking about with Selenium, I came to the conclusion that the dynamic html tables I was trying to manipulate were too complex and the technique I opted for instead was look through the network calls being made in a development window until I found the call to XYZ's website backend that was returning the data. Next, I simply used python's request library to send repeated calls to each websites backend while I manipulated the carat parameter in the request query parameters in order to steadily return different result sets.

**NOTE!!!** **DO NOT**. I repeat, **DO NOT**, mimic this method if you share an IP address with your fiancè to be and/or are not making these requests behind a VPN. For about a month, any and all programmatic advertising I saw was for diamond engagement rings. Because I had started collecting the data before I had been able to propose, I then had to live in constant fear that Emma would grow suspicious of all the diamond advertising she was seeing. 

After a big some data cleaning and minimal munging -- James Allen uses different labels for cut compared to Brilliant Earth for example -- I was left with a (576820, 9) dataset that looked something like this:

```
print(diamond_df.sample(n=5, random_state=0).to_markdown())

|        | shape    |   price |   carat | cut         | color   | clarity   | vendor          | is_lab   |   log_price |
|-------:|:---------|--------:|--------:|:------------|:--------|:----------|:----------------|:---------|------------:|
|   6412 | Round    |     740 |    0.3  | Ideal       | F       | SI1       | Brilliant Earth | False    |     2.86923 |
|  34866 | Round    |    1110 |    0.4  | Ideal       | F       | SI1       | Brilliant Earth | False    |     3.04532 |
| 164602 | Round    |    2020 |    1.2  | Super Ideal | J       | VS1       | Brilliant Earth | True     |     3.30535 |
|  45097 | Marquise |    1220 |    0.5  | Good        | H       | SI1       | Brilliant Earth | False    |     3.08636 |
| 481003 | Round    |    3720 |    1.04 | Very Good   | F       | I1        | James Allen     | False    |     3.57054 |
```

Here is an interactive plot showing carat and log price grouped by vendor and whether or not the diamond is a "loose" diamond or a lab diamond. 
<br>
{{< plotly json="/plotly/diamonds-forever/diamond-carat-price-chart.json" height="400px" >}}
<br>
We shouldn't be shocked to find that there is a strong correlation between carat and price. Calculating an R^2 value for the graph above, I found that ~67% of the variation in log price is explained by carat. Its also apparent from the graph classifying a diamond as a "lab" or "loose" diamond has a large impact on price.

## Sidebar...What the hell are lab diamonds any way? 

[Lab diamonds](https://en.wikipedia.org/wiki/Synthetic_diamond#Gemstones) are real diamonds, full stop. In fact...

>In July 2018, the U.S. Federal Trade Commission approved a substantial revision to its Jewelry Guides, with changes that impose new rules on how the trade can describe diamonds and diamond simulants.[120] The revised guides were substantially contrary to what had been advocated in 2016 by De Beers.[119][121][122] The new guidelines remove the word "natural" from the definition of "diamond", thus including lab-grown diamonds within the scope of the definition of "diamond". The revised guide further states that "If a marketer uses 'synthetic' to imply that a competitor's lab-grown diamond is not an actual diamond, ... this would be deceptive."[1][121]

Lab diamonds that are used as gemstones are produced using CVD (Chemical Vapor Disposition) or HPHT (high-pressure high-temperature) methods and only recently, as of mid 2010s, have begun to penetrate the gemstone market as upstarts such as Brilliant Earth have entered the market. *Gem-quality diamonds grown in a lab can be chemically, physically and optically identical to naturally occurring ones.* Also because of awareness that traditional diamond mining has led to human rights abuses, lab grown diamonds are also an ethically sound alternative to "loose" diamonds. 

...anyways...
<br>
...back to the data...

## Linear Model to Get Us Going
One obvious way to try to get a sense of what features have the greatest impact on diamond price is to run a simple linear regression using the base 10 logarithm of price as a dependent variable. Why log transform your dependent variable you might say? The short answer here is that you always want to avoid skewed distribution in residuals. By using a log transformation, we are reducing skewness in our dependent variable and approximating a normal distribution thus helping to alleviate risk of skewed residuals. Ohh....one more thing...there are a lot of categorical variables involved in this dataset: color, clarity, cut, etc. In order to better handle for these, I've done a one-hot encoding transformation to turn these into dummy variables. Also, because we know that some of these categorical dummmies are perfectly correlated with each other, if a diamond is color E it cant also be color F, I've removed the following columns `['Fair', 'K', 'I1' , 'Blue Nile','Emerald', 'price']` from the datatset and added a constant term. Because we've removed the above dummmies, the constant in the regression results below captures the variance for a Fair cut, K colored, I1 clarity, Blue Nile emerald shaped diamond.

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              log_price   R-squared:                       0.831
Model:                            OLS   Adj. R-squared:                  0.831
Method:                 Least Squares   F-statistic:                 7.073e+04
Date:                Wed, 17 Feb 2021   Prob (F-statistic):               0.00
Time:                        20:49:53   Log-Likelihood:             1.2306e+05
No. Observations:              461453   AIC:                        -2.461e+05
Df Residuals:                  461420   BIC:                        -2.457e+05
Df Model:                          32                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               2.2473      0.009    254.261      0.000       2.230       2.265
carat               0.7369      0.001   1440.295      0.000       0.736       0.738
is_lab             -0.3724      0.001   -426.629      0.000      -0.374      -0.371
Asscher             0.0329      0.006      5.434      0.000       0.021       0.045
Cushion             0.0414      0.003     13.902      0.000       0.036       0.047
Heart               0.0808      0.005     15.468      0.000       0.071       0.091
Marquise            0.0833      0.004     19.611      0.000       0.075       0.092
Oval                0.0621      0.002     27.629      0.000       0.058       0.067
Pear                0.0796      0.003     31.382      0.000       0.075       0.085
Princess            0.0055      0.003      1.963      0.050     8.5e-06       0.011
Radiant             0.0443      0.004     10.026      0.000       0.036       0.053
Round               0.1438      0.002     72.221      0.000       0.140       0.148
Good               -0.0505      0.008     -6.085      0.000      -0.067      -0.034
Ideal              -0.0166      0.008     -2.034      0.042      -0.033      -0.001
Super Ideal         0.0060      0.008      0.736      0.462      -0.010       0.022
Very Good          -0.0350      0.008     -4.294      0.000      -0.051      -0.019
D                   0.2779      0.002    169.315      0.000       0.275       0.281
E                   0.2532      0.002    155.457      0.000       0.250       0.256
F                   0.2505      0.002    152.106      0.000       0.247       0.254
G                   0.2535      0.002    153.388      0.000       0.250       0.257
H                   0.2268      0.002    133.833      0.000       0.224       0.230
I                   0.1613      0.002     93.614      0.000       0.158       0.165
J                   0.0995      0.002     56.110      0.000       0.096       0.103
FL                  0.5412      0.005     98.989      0.000       0.530       0.552
IF                  0.3044      0.003    117.193      0.000       0.299       0.310
SI1                 0.1520      0.002     68.721      0.000       0.148       0.156
SI2                 0.0922      0.002     41.181      0.000       0.088       0.097
VS1                 0.2397      0.002    107.610      0.000       0.235       0.244
VS2                 0.2165      0.002     97.522      0.000       0.212       0.221
VVS1                0.2683      0.002    113.775      0.000       0.264       0.273
VVS2                0.2565      0.002    113.016      0.000       0.252       0.261
Brilliant Earth     0.0102      0.001      8.412      0.000       0.008       0.013
James Allen        -0.0049      0.001     -4.605      0.000      -0.007      -0.003
==============================================================================
Omnibus:                    95161.361   Durbin-Watson:                   2.003
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           312020.298
Skew:                          -1.044   Prob(JB):                         0.00
Kurtosis:                       6.445   Cond. No.                         130.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```


<br>
{{< plotly json="/plotly/diamonds-forever/lm-prediction-chart.json" height="400px" >}}
<br>

## XGB Knows How the Diamonds are Priced

<br>
{{< plotly json="/plotly/diamonds-forever/xgb-prediction-chart.json" height="400px" >}}
<br>