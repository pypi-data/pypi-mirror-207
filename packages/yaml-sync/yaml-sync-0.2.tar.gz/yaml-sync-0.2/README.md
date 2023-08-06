## yamlsync

Yaml Sync is a *very* lightweight YAML-based cache for when you want to preserve the state of something on disk in a human readable way.

## Installation

To install Yaml Sync, simply run:

```bash
pip install yaml-sync
```


## Example usage

Here's a quick example of how to use Yaml Sync:

```
from yaml_sync import YamlCache

# Create a cache that reads and writes to the specified file
cache = YamlCache('cache.yaml', mode='rw')

# Save a key to the cache and write to disk
cache['hello'] = 'world'

# Check if a key is in the cache
assert 'hello' in cache

# Retrieve a key from the cache
variable = cache['hello']

# Save a list to the cache
cache['list_example'] = [1, 2, 3]
```

The resulting yaml will be:

```
hello: world
list_example:
  0: 1
  1: 2
  2: 3
```

You can pass `number_lists=True` at init to save any lists as a numbered dictionary. Since the goal of Yaml Sync is a human-readable file, the numbering may be desired in some cases.

If a value is None, that key is not returned for `key in cache`. e.g.

```python
cache['empty_key'] = None
assert 'empty_key' in cache
# AssertionError
```

Finally, you can specify a preferred order to the keys, to control what is shown first in the yaml.

```python
cache = YamlCache('cache.yaml', order=['b', 'a'])

cache['a'] = 'hello'
cache['b'] = 'world'
with open('cache.yaml') as f:
    print(f.read())
```

```bash
b: world
a: hello
```

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).