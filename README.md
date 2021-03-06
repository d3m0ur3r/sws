# Steam Workshop Scraper 1.5.1
Steam Workshop Scraper works like a CLI tool.  
SWS is a script designed to scrape steam workshop for mods, 
it does so by looking through a range of pages and then
scrape all necessary data to be put into a table.
Once desired ids are scraped, use https://steamworkshopdownloader.io/ to download them all.

SWS is built with python 3.9


### Windows installation:

* Unpack the rar file then Run SWS.exe to use.

### Linux installation:

    $ python3 -m pip install -r requirements.txt  
    $ python3 ./main.py

### General info:
* flag '-i' defaults to 107410 if not specified (Arma 3)
* flag '-r' defaults to 1 if not specified
* By default, all outputs are sorted by '**STARS**'.

### Usage examples:
* SWS.exe -c
* SWS.exe -i <**APP_ID**> -fac -s <**SEARCH_STRING**>
* SWS.exe -i <**APP_ID**> -fc --most-subs -s <**SEARCH_STRING**> -r <**RANGE**>
* SWS.exe -i <**APP_ID**> -fac --most-subs -s <**SEARCH_STRING**> -r <**RANGE**>
* SWS.exe -i <**APP_ID**> -u <**USER_ID**>
* SWS.exe -i <**APP_ID**> -u <**USER_ID**> -s <**SEARCH_STRING**>
* SWS.exe -i <**APP_ID**> -r <**RANGE**> --filter-author <**AUTHOR_NAME**>

### What's new ?
* Cache functionality
    * Faster searches and less 'hammering' at steam servers.