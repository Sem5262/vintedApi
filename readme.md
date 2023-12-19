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
**Vpn is optional but recommended!**
<br>
How to get a vpn extension in your browsers? => download .crx file from a vpn extension from the chromestore [crx downloader](https://crxextractor.com/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

MIT License

Copyright (c) [2023] [Sem5262]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
