
# KissAPI
Unofficial http://www.kissanime.com & http://www.kissmanga.com API.

### March 20th
For the time being, there is not a official ```pip``` package yet due to this
still being in development, expect this too change on a short base. Most parts
of the API are already functional and can be used by installing modules by hand.

This files contains the methods regarding the anime site.
```anime.py```

This files contains the methods regarding the manga site.
```manga.py```

######*By manually placing these in your project folder they can be used.*

Assuming you place the file in your root (```/anime.py```).
```from anime import Anime```

Assuming you place the file in a (```/lib/anime.py```).
```from lib.anime import Anime```

######*If you receive no error you should be good to go.*

Lets cover all the methods available.

## Anime
```.__html__(x, y)``` 
```.shorten(x)```   
```.tail_dash(x)``` 
```.connect(x)```  
```.exists(x)```   
```.validate(x)```  
```.search(x)```  
```.index(x)``` 
```.extract(x)``` 
