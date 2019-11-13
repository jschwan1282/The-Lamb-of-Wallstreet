# The-Lamb-of-Wallstreet
Final Project

Team Members: 
•	Charles Lindner
•	Lacy Williams
•	Jay Schwan
•	Bonnie-jo Barnaby

Goal:  Predict (Predictive Analysis) what stock prices will be in 13 days based on whether or not there is a positive, neutral or negative tweet.

Tools: 
•	Python/Pandas
•	Tableau
•	Postgres
•	sklearn

Data obtained from: 
•	Twitter API - Twitterscraper
o	Training Data = historical tweets
o	Test Data = current tweets
o	Twitter metrics for how many retweets
•	US Economic Data for stock prices (hopefully CSV from AmeriTrade) 

E – Extract:
•	From Yahoo Finance
o	Selected two years of Netflix stock data 
•	From Twitter
o	Two years prior twitter to run Test/Train process

T – Transform:
•	Pulled JSON dataframes and converted to CSV

L – Load:
•	Loaded CSV files into two training models - Sklearn and TensorFlow
•	Ran data through deep learning methods (Linear Regression, KNN, Quadratic - 2 & 3 Polynomials)
•	Visualization loaded into Tableau

<b><#>links:</#></b></br>
<b>Presentation:</b> </br>
https://docs.google.com/presentation/d/15IJaAgMvJi5bY7gW_OLuJaHFoaTzk8gDxktbXH579bY/edit#slide=id.p </br>
Twitter predicitons:</br>
https://public.tableau.com/profile/charles.august.lindner#!/vizhome/tweet_predictions/TMC?publish=yes </br>
Stock Prediciton - knn model:</br>
https://public.tableau.com/profile/lacy.williams#!/vizhome/TheStoryofKNN/Story1 </br>
Stock Prediction - Poly2 model:</br>
https://public.tableau.com/profile/lacy.williams#!/vizhome/TheStoryofPoly2/Story1 </br>
Stock Prediction - Poly3 model:</br>
https://public.tableau.com/profile/lacy.williams#!/vizhome/TheStoryofPoly3/Story1 </br>
Stock Prediction - Linear regression model:</br>
https://public.tableau.com/profile/lacy.williams#!/vizhome/StoryofRegression/Story1 </br>
