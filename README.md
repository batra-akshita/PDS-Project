# Option - 1: (For PDS)
Link to the Post: https://github.com/taspinar/twitterscraper
(This post will not give location specific data)

1) Install the Scrapper
pip install twitterscraper

2) Run the Python code with edit dates: get_tweets.py


# Option - 2 (For Capstone)
Link to the post to get the tweet details of particular user. https://github.com/justinlittman/twitter-scraper
This only gives the tweetsID. For Tweet details, we need to use the twarc https://github.com/edsu/twarc#twitter-api-keys

1) Install Chrome Driver
2) pip install selenium
3) pip install twarc
4) run Python Code twitter_scraper.py
5) this will give the tweetsIDs, put them in a text file.
6) run command "Configure twarc" in cmd, enter the key values:
   (customer) API-key:  Mf9sWyUePbMUJhJmNb70z6FUB
   (customer) API-secret: 9RO1VrpsAbAgtFzcZBjddPILeG0l6ewCrIuks3hYEoH0moWEXR
   Acess-token: 977418354402234369-JNjXjPK2tP4j1eGSQBFQjPRGklT7rNy
   Acess-token-secret: NkTisSRGpReMSi5Ne6eoKptWQku1XUpao6ilELPy6e9Aa
   
   Note: All the keys are associated with my account, I would recommend to create your own keys
   
7) twarc hydrate ids.txt > tweets.json

	Note: ids.txt is what we got from step - 5


