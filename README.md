I wanted to make a solver for the nyt spelling bee puzzle as found here: https://www.nytimes.com/puzzles/spelling-bee/hub.
I initially wrote v1 which generates every permutation of the characters and checks this against a wordlist to see if it's a valid word. 
My second approach was when I realised i could do the inverse, so I checked all the words against the wordlist to see if they contained the letters in the hive.
I then wanted to automate this using webscraping, but as I was doing this, I realised the answers are embedded in the site's html so v3 just grabs the answers from the site.
