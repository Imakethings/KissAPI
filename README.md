
# KissAPI
Unofficial http://www.kissanime.com & http://www.kissmanga.com API.

* March 20th
For the time being, there is not a official ```pip``` package yet due to this
still being in development, expect this too change on a short base. Most parts
of the API are already functional and can be used by installing the module by hand.

--------

This file contains the methods regarding the anime site ```anime.py```.
This file contains the methods regarding the manga site ```manga.py```.

*By manually placing these in your project folder they can be used.

Assuming you place the file in your root (```/anime.py```), ```from anime import Anime```.
Assuming you place the file in a (```/lib/anime.py```), ```from lib.anime import Anime```.

*If you receive no error you should be good to go.

--------

(```.validate(string)```)

```
# This one is easily detected and validated.
print Kiss.validate('Ergo proxy')
# >>> Ergo-proxy

# Excess '-' and '_' are removed and limited to one.
# 'sub' is removed due to the default being sub. That one is listed without sub.
print Kiss.validate('Ergo___---___Proxy___---___sub')
# >>> Ergo-proxy

# When nothing is found, False will be returned.
print Kiss.validate('Not an anime')
# >>> False
```



