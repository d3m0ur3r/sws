# Steam Workshop Scraper 1.4.4
Steam Workshop Scraper is built around scraping appid's.  
SWS is built with python 3.9  
SWS is a script designed to scrape steam workshop for mods.
It does so by looking through a range of pages and then scrape all the urls.  
Should be used in conjunction with https://steamworkshopdownloader.io/

Windows installation:
 * Unpack the rar file then Run SWS.exe to use.

Linux installation:
* python3 -m pip install -r requirements.txt
* python3 ./main.py

General info:
* flag '-i' defaults to 107410 if not specified (Arma 3)  
* flag '-r' defaults to 1 if not specified
* By default, all outputs are sorted by '**STARS**'.

Usage examples:
* SWS.exe/main.py -c
* SWS.exe/main.py -i <**APP_ID**> -fac -s <**SEARCH_STRING**>
* SWS.exe/main.py -i <**APP_ID**> -fc --most-subs -s <**SEARCH_STRING**> -r <**RANGE**>  
* SWS.exe/main.py -i <**APP_ID**> -fac --most-subs -s <**SEARCH_STRING**> -r <**RANGE**>  
* SWS.exe/main.py -i <**APP_ID**> -u <**USER_ID**>  
* SWS.exe/main.py -i <**APP_ID**> -u <**USER_ID**> -s <**SEARCH_STRING**>
* SWS.exe/main.py -i <**APP_ID**> -r <**RANGE**> --filter-author <**AUTHOR_NAME**>
