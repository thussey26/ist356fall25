import requests 
import requests_cache as rq
import pickle

texts = [
    "I love IST356. It is the best course I've ever taken.", 
    "I hate the New York Giants.",
    "I love IST256. It is the best course I've ever taken.", 
    "I don't like the New York Giants."
]

cache = rq.clear_cache('sentiment.pkl') # clear or create a cache file named sentiment.pkl
apikey = "ec25dc1e1297cfba51838bd3"
headers = { 'x-api-key': apikey }
url = "https://cent.ischool-iot.net/api/azure/sentiment"
for text in texts: # loop over each string in the texts list 
    if text in cache: # check if the text was analysed before and is in the cache dictionary
        results = cache[text] 
        from_cache = "CACHED" # add a label to indicate that the result was from the cache
    else: # if the text is not in the cache, call the API
        data = { 'text': text } # create a key/value with the text to send to the API
           
        response = requests.post(url, headers=headers, data=data)
        results = response.json()
        cache[text] = results # save the result for reuse later
        rq.save_cache(cache, 'sentiment.pkl') # write the updated cache to the pickle file
        from_cache = "NOT CACHED" # add a label to indicate that the result was not from the cache

    sentiment = results['results']['documents'][0]['sentiment'] # extract the sentiment from the nested json response
    print(text, sentiment, from_cache) # print text analyzed , sentiment and cache status