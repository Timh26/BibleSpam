Lit Spam
=========



Description
------
This project uses a bigram-based markov chain to generate interesting tweets.



Usage
------
Make sure you have the `twitter` library. If you don't, you can get it by running `pip install twitter`. Put your `twitter.oauth` file in the root directory containing your `OAUTH_TOKEN`,`OAUTH_SECRET`,`CONSUMER_KEY`, and `CONSUMER_SECRET` on separate lines in that order. If you don't know what these are, get them from [the Twitter dev site](http://dev.twitter.com). Next, put your source texts in `.txt` format with appropriate titles in the `\sources` folder. Run `chaingen.py`. At this point you are ready to run the main script. If you are doing more than testing, make sure to change the `TESTING` flag to False. Run the script, and enjoy.
