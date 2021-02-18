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
|   6412 | Round    |     740 |    0.3  | Ideal       | F       | SI1       | Brilliant Earth | False    |     6.60665 |
|  34866 | Round    |    1110 |    0.4  | Ideal       | F       | SI1       | Brilliant Earth | False    |     7.01212 |
| 164602 | Round    |    2020 |    1.2  | Super Ideal | J       | VS1       | Brilliant Earth | True     |     7.61085 |
|  45097 | Marquise |    1220 |    0.5  | Good        | H       | SI1       | Brilliant Earth | False    |     7.10661 |
| 481003 | Round    |    3720 |    1.04 | Very Good   | F       | I1        | James Allen     | False    |     8.22148 |
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
One obvious way to try to get a sense of what features have the greatest impact on diamond price is to run a simple linear regression using the natural logarithm of price as a dependent variable. Why log transform your dependent variable you might say? The short answer here is that you always want to avoid skewed distribution in the residuals. By using a log transformation, we are reducing skewness in our dependent variable and approximating a normal distribution thus helping to alleviate this risk. An additional benefit of using the natural log to transform our dependent variable is that it makes interpretation of the coefficients relatively straightforward as a coefficient of `.15` equates to a percentage increase of `(exp(.15) - 1) * 100` in our dependent variable: 

```
In [10]: (math.exp(.15)-1)*1e2
Out[10]: 16.183424272828304
```
So in the example above, our `.15` coefficient equates to a ~16.2 % increase in our dependent variable. Ohh....one more thing...there are a lot of categorical variables involved in this dataset: color, clarity, cut, etc. In order to better handle for these, I've done one-hot encoding to turn these into dummy variables. Also, because we know that some of these categorical dummmies are perfectly correlated with each other, if a diamond is color E it cant also be color F, I've removed the following columns `['Fair', 'K', 'I1' , 'Blue Nile','Emerald', 'price']` from the datatset and added a constant term. Because we've removed the above dummmies, the constant in the regression results below captures the variance for a Fair cut, K colored, I1 clarity, Blue Nile emerald shaped diamond.

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              log_price   R-squared:                       0.831
Model:                            OLS   Adj. R-squared:                  0.831
Method:                 Least Squares   F-statistic:                 7.073e+04
Date:                Thu, 18 Feb 2021   Prob (F-statistic):               0.00
Time:                        07:08:13   Log-Likelihood:            -2.6180e+05
No. Observations:              461453   AIC:                         5.237e+05
Df Residuals:                  461420   BIC:                         5.240e+05
Df Model:                          32                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               5.1746      0.020    254.261      0.000       5.135       5.214
carat               1.6968      0.001   1440.295      0.000       1.695       1.699
is_lab             -0.8574      0.002   -426.629      0.000      -0.861      -0.853
Asscher             0.0757      0.014      5.434      0.000       0.048       0.103
Cushion             0.0953      0.007     13.902      0.000       0.082       0.109
Heart               0.1861      0.012     15.468      0.000       0.163       0.210
Marquise            0.1919      0.010     19.611      0.000       0.173       0.211
Oval                0.1430      0.005     27.629      0.000       0.133       0.153
Pear                0.1833      0.006     31.382      0.000       0.172       0.195
Princess            0.0126      0.006      1.963      0.050    1.96e-05       0.025
Radiant             0.1020      0.010     10.026      0.000       0.082       0.122
Round               0.3312      0.005     72.221      0.000       0.322       0.340
Good               -0.1162      0.019     -6.085      0.000      -0.154      -0.079
Ideal              -0.0382      0.019     -2.034      0.042      -0.075      -0.001
Super Ideal         0.0138      0.019      0.736      0.462      -0.023       0.051
Very Good          -0.0806      0.019     -4.294      0.000      -0.117      -0.044
D                   0.6399      0.004    169.315      0.000       0.633       0.647
E                   0.5830      0.004    155.457      0.000       0.576       0.590
F                   0.5768      0.004    152.106      0.000       0.569       0.584
G                   0.5837      0.004    153.388      0.000       0.576       0.591
H                   0.5223      0.004    133.833      0.000       0.515       0.530
I                   0.3714      0.004     93.614      0.000       0.364       0.379
J                   0.2290      0.004     56.110      0.000       0.221       0.237
FL                  1.2461      0.013     98.989      0.000       1.221       1.271
IF                  0.7010      0.006    117.193      0.000       0.689       0.713
SI1                 0.3500      0.005     68.721      0.000       0.340       0.360
SI2                 0.2123      0.005     41.181      0.000       0.202       0.222
VS1                 0.5520      0.005    107.610      0.000       0.542       0.562
VS2                 0.4984      0.005     97.522      0.000       0.488       0.508
VVS1                0.6177      0.005    113.775      0.000       0.607       0.628
VVS2                0.5905      0.005    113.016      0.000       0.580       0.601
Brilliant Earth     0.0235      0.003      8.412      0.000       0.018       0.029
James Allen        -0.0112      0.002     -4.605      0.000      -0.016      -0.006
==============================================================================
Omnibus:                    95161.361   Durbin-Watson:                   2.003
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           312020.298
Skew:                          -1.044   Prob(JB):                         0.00
Kurtosis:                       6.445   Cond. No.                         130.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

lorem ipsum lorem ipsum blah blah....

```
|                 |   coefficients |     p_delta |   p_delta_low |   p_delta_high |
|:----------------|---------------:|------------:|--------------:|---------------:|
| const           |      5.17457   | 175.721     |  168.81       |   182.912      |
| carat           |      1.69683   |   4.45664   |    4.44405    |     4.46925    |
| is_lab          |     -0.857427  |  -0.575748  |   -0.577416   |    -0.574073   |
| Asscher         |      0.0756715 |   0.0786082 |    0.0495655  |     0.108455   |
| Cushion         |      0.095304  |   0.0999932 |    0.0853125  |     0.114872   |
| Heart           |      0.186117  |   0.204563  |    0.176488   |     0.233308   |
| Marquise        |      0.191853  |   0.211492  |    0.188484   |     0.234946   |
| Oval            |      0.143012  |   0.153743  |    0.142098   |     0.165508   |
| Pear            |      0.183312  |   0.201189  |    0.187516   |     0.21502    |
| Princess        |      0.0126225 |   0.0127025 |    1.9579e-05 |     0.0255463  |
| Radiant         |      0.101967  |   0.107347  |    0.0854912  |     0.129643   |
| Round           |      0.331151  |   0.392569  |    0.380111   |     0.405141   |
| Good            |     -0.116172  |  -0.109677  |   -0.142379   |    -0.0757294  |
| Ideal           |     -0.0382252 |  -0.0375039 |   -0.0723039  |    -0.00139838 |
| Super Ideal     |      0.0138274 |   0.0139235 |   -0.0227301  |     0.0519517  |
| Very Good       |     -0.0806462 |  -0.07748   |   -0.110818   |    -0.0428921  |
| D               |      0.639936  |   0.89636   |    0.882364   |     0.91046    |
| E               |      0.582988  |   0.791384  |    0.778265   |     0.804599   |
| F               |      0.57684   |   0.780404  |    0.767219   |     0.793686   |
| G               |      0.58371   |   0.792677  |    0.779356   |     0.806098   |
| H               |      0.522322  |   0.685938  |    0.673091   |     0.698884   |
| I               |      0.371373  |   0.449724  |    0.438495   |     0.46104    |
| J               |      0.229027  |   0.257376  |    0.247357   |     0.267475   |
| FL              |      1.24614   |   2.47691   |    2.39217    |     2.56376    |
| IF              |      0.700981  |   1.01573   |    0.992236   |     1.0395     |
| SI1             |      0.350047  |   0.419135  |    0.405037   |     0.433374   |
| SI2             |      0.212314  |   0.236536  |    0.224104   |     0.249095   |
| VS1             |      0.552021  |   0.736759  |    0.719385   |     0.754309   |
| VS2             |      0.498421  |   0.646119  |    0.629712   |     0.662692   |
| VVS1            |      0.617705  |   0.854667  |    0.835036   |     0.874508   |
| VVS2            |      0.590518  |   0.804923  |    0.786533   |     0.823502   |
| Brilliant Earth |      0.0235072 |   0.0237857 |    0.0181934  |     0.0294087  |
| James Allen     |     -0.0112318 |  -0.0111689 |   -0.0158852  |    -0.00643009 |
```


<br>
{{< plotly json="/plotly/diamonds-forever/lm-prediction-chart.json" height="400px" >}}
<br>

## XGB Knows How the Diamonds are Priced

<br>
{{< plotly json="/plotly/diamonds-forever/xgb-prediction-chart.json" height="400px" >}}
<br>