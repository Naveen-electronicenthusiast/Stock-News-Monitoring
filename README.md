# Stock-News-Monitoring

ABSTRACT

This is a simple project that gives real time data of stocks of particular company that the user wish to know. To be more specific 
in this project we compare the price of a Tesla stock at market close yesterday and market close the day before yesterday. The difference
in price is calculated and if the difference is more that 3% then an SMS is sent to the user consisting information about %difference(raise or reduction in price) 
along with the news that explains the recent advancements in the Tesla stock. This gives an idea to the user regarding how to go about the investment.

 Steps followed while writing the python code for this project:
1. Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
2. Get the day before yesterday's closing stock price
3. Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
4. Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
5. If percentage is greater than 3(or any number of your choice) then print("Get News").
6. Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
7. Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
8. Create a new list of the first 3 article's headline and description using list comprehension.
9. Send each article as a separate message via Twilio.

API used
