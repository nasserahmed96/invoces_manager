from src.Logger import Logger


class Cache(object):
    class __Cache:
        def __init__(self):
            self._cache = None
            self.logger = Logger()
            self.initialize_cache()

        def __str__(self):
            return "{0!r} {1}".format(self, self._cache)

        def initialize_cache(self):
            self._cache = dict()
            self.logger.debug("Cache is ready")

        def show_cache(self):
            return self._cache

        def append_to_cache(self, key, value):
            self._cache[key] = value
            self.logger.debug(f'Append {key} with value {value} to cache')

        def retrieve(self, key):
            self.logger.debug(f'Getting {key} from cache')
            return self._cache[key]

    instance = None

    def __new__(cls):
        if not Cache.instance:
            Cache.instance = Cache.__Cache()
        return Cache.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr(self, item):
        return setattr(self.instance, item)



