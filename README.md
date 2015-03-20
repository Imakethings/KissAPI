
# KissAPI - Unofficial http://www.kissanime.com & http://www.kissmanga.com API.

--------

> **March 20th**,
> For the time being, there is not a official ```pip``` package yet due to this
> still being in development, expect this too change on a short base. Most parts
> of the API are already functional and can be used by installing the module by hand.

--------

> **March 21th**,
> Updated README.md to contain all the available methods.

--------

This file contains the methods regarding the anime site ```anime.py```.
This file contains the methods regarding the manga site ```manga.py```.

*By manually placing these in your project folder they can be used.

Assuming you place the file in your root (```/anime.py```), ```from anime import Anime```.
Assuming you place the file in a (```/lib/anime.py```), ```from lib.anime import Anime```.

*If you receive no error you should be good to go.

--------

* ```.validate(string)```

--------

```
print Kiss.validate('Ergo proxy')
>>> Ergo-proxy

print Kiss.validate('Ergo___---___Proxy___---___sub')
>>> Ergo-proxy

print Kiss.validate('Not an anime')
>>> False
```

--------

* ```.search(string, integer, boolean)```

--------

```
# Kiss.search(string_to_validate, output_amount, ?generator_object)

print Kiss.search('Ergo')
>>> [u'Ergo Proxy (Dub)', u'Ergo Proxy (Sub)']

print Kiss.search('Ergo proxy', 1)
>>> Ergo Proxy (Dub)

print Kiss.search('Ergo proxy', 2)
>>> [u'Ergo Proxy (Dub)', u'Ergo Proxy (Sub)']

print Kiss.search('Ergo proxy', 2, True)
>>> <generator object search at 0x7f175c39e1e0>

print Kiss.search('Ergo proxy (Sub)')
>>> Ergo Proxy (Sub)

print Kiss.search('Ergo-proxy-sub')
>>> []
```

--------

* ```.index(string, boolean)```

--------

```
# Kiss.index(string_to_index, ?generator_object)

print Kiss.index('Ergo-proxy')
# A list containing all paths to the episodes.
>>> ['/Anime/Ergo-Proxy/Episode-23?id=31544', '/Anime/Ergo-Proxy/Episode-22?id=31543', '/Anime/Ergo...']

print Kiss.index('Ergo proxy')
>>> []

print Kiss.index('Ergo')
>>> []
```

--------

* ```.extract(string, boolean)```

--------

```
# Kiss.extract(path_to_extract_video, ?shortened_output)

for path in Kiss.index('Ergo-proxy'):
    print Kiss.extract(path, True)

>>> http://is.gd/tQzE8O
>>> http://is.gd/j50k4T
>>> http://is.gd/2H4RyB
>>> http://is.gd/WNKAM9
>>> ...
```






