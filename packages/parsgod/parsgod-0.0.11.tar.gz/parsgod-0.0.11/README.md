The module allows you to automatically determine what to use - requests or selenium, and write the basis of the parser on both modules. Also supports writing the basics of asynchronous parser.

To start using the module, you need to call the - pgmode function. The rest can be found by looking under the hood of this library.



```python
import parsgod

parsgod.pgmode(url='https://sunlight.net', headers={'User-agent': 'Mozilla 5.0'}, mode='asyncio')
#This code will create the asynchronous parser in your directory

parsgod.pgmode(url='https://sunlight.net', headers={'User-agent': 'Mozilla 5.0'})
#This code will create the parser in your directory

parsgod.pgmode(url='https://ozon.ru', pause_time=5)
#The site above is very poorly protected, so if we insert a link to ozone with cloudflare, then a foundation using selenium will be automatically created
#pause_time is responsible for pausing after loading the page
```


