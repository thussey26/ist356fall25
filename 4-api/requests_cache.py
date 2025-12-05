import pickle

# load data from a specified pickle file and return it.
# rb is read binary mode
def load_cache(pickle_file):
    try:
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
# clear the cache by overwriting the pickle file with an empty dictionary
#opens file in write binary mode ('wb'), overwrite the file contents (or create a file)
def clear_cache(pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump({}, f)
        return {}
# store the cache dictionary into a specified pickle file
def save_cache(cache, pickle_file):
    with open(pickle_file, 'wb') as f:
        pickle.dump(cache, f)

if __name__ == '__main__':
    cache = clear_cache('test.pkl')
    assert cache == {}
    cache['test'] = 'test'
    save_cache(cache, 'test.pkl')
    cache = load_cache('test.pkl')
    assert cache == {'test': 'test'}
    assert cache['test'] == 'test'

