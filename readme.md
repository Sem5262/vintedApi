# vintedApi

A web scraper that gets new items from the vinted catalog

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install vintedApi.

```bash
pip install vintedApi
```

## Usage


```python
from vintedApi import VintedApi

vintedApi =  VintedApi()
vintedApi.searchUrl = '' # url from vinted catalog

vintedApi.addSearchBrowser(vpn_path='./vpns/example_vpn.crx') # creates a new browser that that seaches for new items in the catalog (vpn extension optional)
vintedApi.addSearchBrowser(vpn_path='./vpns/example_vpn1.crx')
vintdedApi.addItemBrowser(vpn_path='./vpns/example_vpn2.crx' ) # creates a new browser that scrapes data for specific item (vpn extension optional)
vintdedApi.addItemBrowser(vpn_path='./vpns/example_vpn2.crx' )

# you can add as much browsers as you need

vintedApi.search() 
# returns list with all the new items and their details [{item1},{item2},...]

vintedApi.itemSearch(item_id)
#retuns data for specific item

vintedApi.itemSearchRaw(item_id):
#returns all the raw data from vinted

vintedApi.searchForNewItems()
# returns list with all the new item ids



vintedApi.deleteItemBrowser(index)
# deletes specific browser

vintedApi.deleteSearchBrowser(index)
# deletes specific browser

```
vpn is optional but recommended.
How to get vpn? download .crx file from a vpn extension from the chromestore [crx downloader](https://crxextractor.com/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)
