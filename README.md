<h1>Stock-News-Monitoring</h1>

<br>ABSTRACT: </br>
This is a simple project that gives a real time data of stocks of a particular company that the user wish to know. To be more specific 
in this project we compare the price of a Tesla stock at market close yesterday and market close the day before yesterday. The difference
in price is calculated and if the difference is more that 3% then an SMS is sent to the user consisting information about %difference(raise or reduction in price) 
along with the news that explains the recent advancements in the Tesla stock. This gives an idea to the user regarding how to go about the investment.

<h2>Steps followed while writing the python code for this project</h2>
<br>1. Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]</br>
2. Get the day before yesterday's closing stock price
<br>3. Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp</br>
4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
<br>5. If percentage is greater than 3(or any number of your choice) then print("Get News").</br>
6. Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
<br>7. Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation</br>
8. Create a new list of the first 3 article's headline and description using list comprehension.
<br>9. Send each article as a separate message via Twilio.</br>

<h2>APIs used</h2>
1. https://www.alphavantage.co/ is a stock market API used to get the stock price of different firms. Read this documentation https://www.alphavantage.co/documentation/ for better understanding of the API used in this project.</br>
2. https://newsapi.org/ is a news API used to get the recent news related to the companies. Read the following documentation for better understanding https://newsapi.org/docs/endpoints/everything.
3. https://www.twilio.com/docs/sms/quickstart/python this link will walk help you through the entire process step-by-step, starting with setting up your. Twilio account all the way through sending an SMS using a Messaging Service.

<h2>What is Twilio Messaging?</h2>
Twilio Messaging is an API to send and receive SMS, MMS, OTT messages globally. It uses intelligent sending features to ensure messages reliably reach end users wherever they are. 
