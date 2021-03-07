import asyncio
from dataprep.eda import plot
from dataprep.connector import connect

auth_token = "55xi9MzvQHBUHjWf4TIPib6EaVrnpU-1TMR1J11SJ5xvx2vFtZF7rK-dHWUauOHocP-59tTB7Fg8ySlLjWghy4xqZSfVuwxCBQSNs_Pa2rsGTc40fWJaULC7MhhEYHYx"

#searchedCategory = (input("Give me a category")).lower()
#searchedLocation = input("What location are you looking at? ")

searchedCategory = "burgers"
searchedLocation = input("Search for average places in a city: ")
searchedLongitude = 50
searchedLatitude = 123


catergoryList = ["burgers", "sushi", "pizza", "coffee", "salad", "chinese", "indian",
                 "japanese", "bars", "vegan", "fast food", "dim sum", "donuts", "bubble tea", "mexican"]

listQuote = open(searchedLocation + 'data.txt', 'w')
bigString = ""

# You can get ”yelp_access_token“ by following https://www.yelp.com/developers/documentation/v3/authentication
for i in catergoryList:
    conn_yelp = connect(
        "yelp", _auth={"access_token": auth_token}, _concurrency=5)
    df = asyncio.run(conn_yelp.query(
        "businesses", categories=i.lower(), location=searchedLocation, _count=100))

    # Remove irrelevant data
    df = df[(df['city'] == searchedLocation)]


# print(df[['name', 'address1', 'city', 'state', 'categories',
#          'country', 'zip_code', 'price', 'rating']])

    bigString += ("The average location of a "
                  + str(i)
                  + " place in "
                  + str(searchedLocation)
                  + " is at "
                  + "("
                  + str(df["latitude"].mean())
                  + ", "
                  + str(df["longtitude"].mean())
                  + ")"
                  + "\n"
                  + "Rating: "
                  + str(df["rating"].mean())
                  + "\n\n")
    print(bigString)
listQuote.write(bigString)
listQuote.close
