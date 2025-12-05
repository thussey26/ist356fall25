import pickle

def load_cache(pickle_file):
    try:
        with open(pickle_file, 'rb') as f: # open the pickle file for reading
            return pickle.load(f) # load to deserialize from the file
    except FileNotFoundError: # if the file is not found , return an empty dictionary
        return {}
    
def clear_cache(pickle_file): # reset the cache by creating an empty dictionary
    with open(pickle_file, 'wb') as f:
        pickle.dump({}, f) # serialize the empty dictionary to the file
        return {}

def save_cache(cache, pickle_file): # Saves the current in-memory cache  back into the pickle file.
    with open(pickle_file, 'wb') as f: # open the file in write mode
        pickle.dump(cache, f) # serialize the cache dictionary to the file
        return None
#Keeps the cache persistent between runs — so data you saved previously can be reloaded later
if __name__ == '__main__':
    cache = clear_cache('test.pkl')
    assert cache == {}
    cache['test'] = 'test'
    save_cache(cache, 'test.pkl')
    cache = load_cache('test.pkl')
    assert cache == {'test': 'test'}
    assert cache['test'] == 'test'

# Example usage
test1 = load_cache('sentiment.pkl')
print(test1)

#Another example usage
pickle_file = 'geocode_cache.pkl'
cache = load_cache(pickle_file)   # Load existing cache or empty {}

def fake_geocode(location):
    """Pretend this is an API call """
    print(f"Making API call for '{location}'...")
    return {"lat": 43.0481, "lon": -76.1474} 

location = "Syracuse, NY"
cache_key = location.lower()

# Check if the location is already cached
if cache_key in cache:
    print("Using cached data.")
    geo = cache[cache_key]
else:
    print("Not in cache — fetching new data.")
    geo = fake_geocode(location)
    cache[cache_key] = geo  # store new result in memory
    save_cache(cache, pickle_file)  # persist it to file

print("Result:", geo)