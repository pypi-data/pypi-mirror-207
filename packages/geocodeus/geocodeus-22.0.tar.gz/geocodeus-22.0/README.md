# geocodeus

The ```ZipCache``` module from the ```geocodeus``` package is a Python library that enables users to retrieve data for US zip codes, such as the latitude and longitude coordinates, city, state, county, and timezone information. This module leverages a caching mechanism to speed up data retrieval and optimize memory usage.

To use the ```ZipCache``` module, users must first import it using the ```from geocodeus import ZipCache statement```. Once the module is imported, they can create an instance of the ```ZipCache``` class with no arguments, which initializes the cache and makes it ready for use. To obtain data for a particular US zip code, users can then call the ```getData()``` method with a zip code string as the argument. The method returns a dictionary that contains information about the specified zip code.

The ZipCache module employs a caching mechanism that enhances performance and memory usage efficiency. When a user calls the ```getData()``` method with a zip code, the module first checks whether the data for that code is already in the cache.


Overall, the ```ZipCache``` module from the ```geocodeus``` package is a powerful and easy-to-use tool for obtaining data for US zip codes. With its efficient caching mechanism and reliable data sources, this module is a must-have for any Python developer working with US zip codes.

## Installation

You can install geocodeus using pip:


```bash
pip install geocodeus


```


## Usage

Here's an example of how to use Zip Cache:

```python
from geocodeus import ZipCache




cache = ZipCache()

# Get data for a zip code
data = cache.getData("96105")
print(data)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)