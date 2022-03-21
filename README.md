# sws
Steam Workshop Scraper is built around scraping appid's.
SWS is built in python 3.9
SWS is a script designed to scrape steam workshop for mods.
It does so by looking through a range of pages and then scrape all the urls. 
Should be used in conjunction with https://steamworkshopdownloader.io/

Current version of Steam Workshop Scraper 1.4.4

builds/SWS.rar contains a directory with the SWS.exe in it.
Run SWS.exe to use

flag '-i' defaults to 107410 if not specified (Arma 3)  
flag '-r' defaults to 1 if not specified

Examples:   
SWS.exe -c  
SWS.exe -i <appid> -fac -s terrain  
SWS.exe -i <appid> -fc --most-subs -s <search_string_here> -r 1-10  
SWS.exe -i <appid> -fac --most-subs -s <search_string_here> -r 1-100  
SWS.exe -i <appid> -u <userid>  
SWS.exe -i <appid> -u <userid> -s <search_string_here>

Documentation needs alot more work.