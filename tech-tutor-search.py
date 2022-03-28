#This program automatically searches for a local tutor using Python

#import search module
from googlesearch import search

#stored queries
queries = ["Local Math Tutor", "Local English Tutor"]

#iterate through queries and print search results
for i in queries:
    for j in search(i, tld="com", lang="en", num=1, start=0, stop=1, pause=2.0):
        print(j)
