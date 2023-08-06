import os
import yaml

class YamlCache:
    """
    A simple YAML-based cache class for Python.

    The cache can be used as an in-memory cache, or it can persist data to disk
    using a YAML file as the storage format.

    :param cache_location: Path to the YAML file used for storing the cache.
                           If None, this is a basic in-memory cache.
    :param mode: File access mode. 'rw' for read-write (default), 'w' to erase
                 existing cache, 'r' for read-only.
    """

    def __init__(self, cache_location=None, mode='rw', number_lists=False):
        self.cache_location = cache_location
        self.mode = mode
        self.number_lists = number_lists # True to save lists as numbered lists
        self.cache = {}

        if self.cache_location is not None:
            if os.path.exists(self.cache_location) and mode != 'w':
                self.load()
            elif mode == 'w':
                self.write()

    def __getitem__(self, key):
        """
        Retrieve the value associated with the specified key from the cache.

        :param key: The key to retrieve the value for.
        :return: The value associated with the specified key.
        """
        return self.cache[key]

    def __setitem__(self, key, value):
        """
        Set the value associated with the specified key in the cache.

        If the value is a list, it is saved as a numbered dictionary.

        :param key: The key to set the value for.
        :param value: The value to associate with the key.
        """
        if isinstance(value, list) and self.number_lists:
            value = {i: v for i, v in enumerate(value)}

        self.cache[key] = value
        if self.cache_location is not None:
            self.write()

    def __contains__(self, key):
        """
        Check if the specified key is in the cache.

        :param key: The key to check for.
        :return: True if the key is in the cache, False otherwise.
        """
        return key in self.cache

    def load(self, cache_location="default"):
        """
        Load the cache from the YAML file specified by cache_location.

        Raises:
            ValueError: If cache_location is None and no cache_location is specified.
        """
        if cache_location=="default":
            if self.cache_location is None:
                raise ValueError("Cache location not specified")
            cache_location = self.cache_location

        with open(cache_location, 'r') as f:
            self.cache = yaml.safe_load(f)

    def write(self, cache_location="default"):
        """
        Write the cache to the YAML file specified by cache_location.

        Raises:
            ValueError: If cache_location is None or if the cache is read-only.
        """
        if self.mode == 'r':
            raise ValueError("Cache is read-only")

        if cache_location=="default":
            if self.cache_location is None:
                raise ValueError("Cache location not specified")
            cache_location = self.cache_location

        with open(cache_location, 'w') as f:
            yaml.safe_dump(self.cache, f)