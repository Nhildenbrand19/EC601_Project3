# EC601_Project3

## Unit Tests for Project 2 Twitter API/ Google NLP

| Type | Description of Test | Expected Outcome | 
| ----------- | ----------- | ----------- |
| Error Handling | In my first test case, I will take my first example from project 2, the liking of a tweet through from the terminal. This test will test the functionality of this program by trying to like a tweet that was tweeted by a user who's profile is private and the account I am using does not follow this account. | My expected outcome in this case is that I would get an error back saying "tweet unavailable" or some type of error saying that specified tweet can not be found. |
| Functionality under normal use case | Let's now take my second example of pulling the 10 most recently liked tweets from a company. In this test, I want to test what output I get if I send this request at the same time that the company likes another tweet. Is that tweet going to be included in my request, is it not, or is an error going to be thrown? | My expected outcome in this case would be to pull all the tweets prior to the liking of this new tweet because the request was made at the same time. |
| Performance | For this test, let's take the example of pulling tweets from individuals. I want to test performance here so if an individual has 10s of thousands of tweets can this request pull all of these tweets? Will it break the program or request or will it succeed? I will do this test by not specifying a number of tweets to pull and taking an account that has that many tweets. | I would expect this program to succeed but take much longer than if only pulling 10 tweets. |
| Error Handling | Now lets test another error handling example in the case of Panera Bread. Looking at my example from project 2 lets test the error handling of accidentally inputting a wrong character into the key word we are trying to search. For example typing in "Panrra" instead of "Panera" | In this case, I would expect the program to pull the key word that contains the error. There are way to many tweets to be able to distinguish and this would be a very hard error to deal with. |
| Performance | Looking at a Google NLP case, I want to test if the sentiment analysis on movies would be changed by inputting 5,000 more negative reviews when training my model. The idea of this test is to see if more negative tests would misclassify any positive reviews because the model has seen a sustaintial amount more negative than postive reviews.| My expected outcome of this test is that the accuracy of the analysis actually would improve as it has more data to differentiate postive from negative  |


## Unit Tests for Project 2 Product
| Type | Description of Test | Expected Outcome | 
| ----------- | ----------- | ----------- |
| Functionality under normal use case | This will be my most simple test of the four. Here I want to test a normal use case where I am successfully pulling both the weekly schedule and the power rankings for that specific week. I want to test if my python program will read what I want it to and correctly output the predicted winners of that week into a text file. | My expected outcome here is a txt file that predicts the winners of each game for the specified week. |
| Functionality under misuse casee | This test will look at a misuse case where the previous weeks schedule is pulled but the power rankings for the current week  is used. | My expected outcome here would be no issue with the output or program, only the incorrect prediction for the games as the current week schedule is not being evaluated. |
| Error Handling | I want to test an error of pulling the correct schedule and power rankings but this time inputting 2 teams into the schedule that do not exist in the power rankings.  | I would expect the program to break actually. I did not build in an error handler yet when it comes to teams not in power rankings and in the schedule or vice versa. |
| Performance | This test I want to give the program every weeks schedule of games from Week 1 to Week 17. I want this to then output the predicted outcome of every single game for the year into a text file. | I would expect this to work just as it would work for one week. |


The code attached above shows what a unit test would look like using unitest and unitest.mock. 
