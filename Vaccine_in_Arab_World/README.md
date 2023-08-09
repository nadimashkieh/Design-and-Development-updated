##Comparative sentiment analysis of Arabic Tweets pre- and post-Omicron.
This project utilizes Python3, and Python 3 packages (URL, JSON, NLPK, Camel Tool, etc...) to extract, process and interpret time-bound tweets related to pre and post Omicron sentiment analysis and dialect identification of Arabic tweets. The aim is to compare the results and the sentiments of tweets within the two timeframes.

##Prerequsites:

- A developer Twitter account.
- Python 3 and related packages


##Order of execution
###Part one:
https://github.com/nadimashkieh/vaccine_Arabic_tweets/blob/main/url_get_Github.ipynb

use url_get to accomplish the following:
- Setup Twitter credentials and connectivity requirements.
- Define queries and bounded timeframes (pre and post Omicron) for collecting tweets. 
- Convert the requested HTML GET JSON data into two separate csv files to be stored on the       local drive.



###Part two:
https://github.com/nadimashkieh/vaccine_Arabic_tweets/blob/main/Vaccine%20in%20the%20Arab%20World%20(Twitter)-Github%20version.ipynb

Vaccine in the Arab World
- Import CAMeL Tools libraries for Arabic NLP (CAMeL Tools is suite of Arabic natural language   processing tools developed by the CAMeL Lab at New York University Abu Dhabi).
- Create two data frames from the csv files.
- Logic was added to omit certain tweets that contained unidentifiable characters.
- Apply CAMeL Tools to process the data.
- Analyze and visualize the data.


This code is open-access, open-use, licensed under Creative Commons Zero v1.0 Universal:
https://github.com/nadimashkieh/vaccine_Arabic_tweets/blob/main/LICENSE 



