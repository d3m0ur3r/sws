# Steam Workshop Scraper 1.4.4
Steam Workshop Scraper is built around scraping appid's.
SWS is built in python 3.9
SWS is a script designed to scrape steam workshop for mods.
It does so by looking through a range of pages and then scrape all the urls. 
Should be used in conjunction with https://steamworkshopdownloader.io/

Installation:
 * Unpack the rar file then Run SWS.exe to use.  
 * Or use python3 with ./main.py

Extra details:
* flag '-i' defaults to 107410 if not specified (Arma 3)  
* flag '-r' defaults to 1 if not specified
* By default, all outputs are sorted by 'STARS'. 
* Use --sort-by [**ID, STARS, AUTHOR, USERID, TITLE**]. Sorts ASC
* It's possible to use rich tables with --rich-table

Usage examples:   
* SWS.exe -c
* SWS.exe -i <**APP_ID**> -fac -s <**SEARCH_STRING**>
* SWS.exe -i <**APP_ID**> -fc --most-subs -s <**SEARCH_STRING**> -r 1-10  
* SWS.exe -i <**APP_ID**> -fac --most-subs -s <**SEARCH_STRING**> -r 1-100  
* SWS.exe -i <**APP_ID**> -u <**USER_ID**>  
* SWS.exe -i <**APP_ID**> -u <**USER_ID**> -s <**SEARCH_STRING**>
* SWS.exe -i <**APP_ID**> -r 1-20 --filter-author <**AUTHOR_NAME**>
