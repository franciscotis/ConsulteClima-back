from cachetools import TTLCache
import time

cache = TTLCache(maxsize=1024, ttl=3)

def test_cache_saving():
    cache['teste'] = 123
    assert 'teste' in cache

def test_time_out_cache():
    cache['teste'] = 123
    time.sleep(4)
    assert 'teste' not in cache
    

