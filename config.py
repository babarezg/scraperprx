# -*- coding: utf-8 -*-

# How many seconds to wait for the proxy to make a connection.
# The higher this number, the longer the check will take
# and the more proxies you will receive.
TIMEOUT = 20

# Maximum concurrent connections.
# Don't set higher than 900, please.
MAX_CONNECTIONS = 900

# Set to False to sort proxies alphabetically.
SORT_BY_SPEED = True

# Path to the folder where the proxy folders will be saved.
# Leave the quotes empty to save the proxies to the current directory.
SAVE_PATH = ""

# Enable which proxy folders to create.
# Set to False to disable.

# Proxies with any anonymity level.
PROXIES = True
# Anonymous proxies.
PROXIES_ANONYMOUS = False
# Same as PROXIES, but including exit-node's geolocation.
# Geolocation format is ip:port::Country::Region::City
PROXIES_GEOLOCATION = False
# Same as PROXIES_GEOLOCATION, but including exit-node's geolocation.
PROXIES_GEOLOCATION_ANONYMOUS = False


# PROTOCOL - whether to enable checking certain protocol proxies (True or False).
# PROTOCOL_SOURCES - proxy lists URLs.
HTTP = False
HTTP_SOURCES = (
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
"https://raw.githubusercontent.com/UserR3X/proxy-list/main/http%2Bs.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
)
SOCKS4 = True
SOCKS4_SOURCES = (
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
"https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks4.txt",
"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
"https://raw.githubusercontent.com/KUTlime/ProxyList/main/ProxyList.txt",
"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
"http://spys.me/proxy.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4%2B5.txt",
)
SOCKS5 = True
SOCKS5_SOURCES = (
   "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
"https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks5.txt",
"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
"https://github.com/monosans/proxy-list/blob/main/proxies/socks5.txt",
"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
"https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5",
"https://www.proxyscan.io/download?type=socks5",
)
