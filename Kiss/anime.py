#! /usr/bin/env python
# Copyright (C) 2015 Mirko van der Waal
# Distributed under terms of the MIT license.

from sys import exit as Die

try:
    import re
    import requests
    from bs4    import BeautifulSoup as Bs
    from base64 import b64decode
    from gdshortener import ISGDShortener

except ImportError as e:
    print e, Die(0)

class Anime:
    ''''''

    def __init__(self):
        ''' Holds a few global variables for the class and contains
            Lambdas to shorten various repetative actions.
            @return: None.
        '''

        self.BASE_URL   = "http://kissanime.com/"
        self.ANIME_URL  = "http://kissanime.com/Anime/"
        self.SEARCH_URL = "http://kissanime.com/Search/Anime/"

        # Shortens the argument with GDShortener.
        self.shorten    = lambda x: ISGDShortener().shorten(x)[0]
        
        # Removes a tailing dash when one is found.
        self.tail_dash  = lambda x: x[: len(x) - 1] if x.endswith('-') else x
        
        # Attempt to make a connection.
        self.connect    = lambda x,y: False if requests.get(x + y).status_code != 200 else True
        # Basically extends self.connect to a more useable function method.
        self.exists     = lambda x: self.connect(self.ANIME_URL, self.validate(x))

    def __html__(self, href, path):
        ''' Performs a popular task to extract the HTML from a given url. '''
        
        try:
            # Attempt create two new objects
            # HTTP Object will serve as an instance of the requests module.
            HTTP = requests
            
            # HTML Object will serve as an instance of the PrettySoup module.
            # It containts the data data from a HTTP request.
            # NOTE: I hate the word beautiful.
            HTML = Bs(str(HTTP.get(href + path).content))
      
            # Return the HTML content forged by PrettySoup.
            return HTML

        # Return False on every failed attempt.
        except Exception:
            return False

    def validate(self, argument):
        ''' A coat to handle the generator. '''

        def validate(argument):
            ''' Validates the argument to be a valid href.path. '''

            PREVIOUS = ''

            # Encode every argument to unicode as not valid unicode characters
            # Are never used in the url.
            for character in unicode(argument):
                
                # Validate every valid character and filter out all whitespace.
                if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
                    yield character
                    
                    # Set the previous character.
                    # When itterating this can be used to prevent double '--' dashes.
                    PREVIOUS = character

                # If the character cannot be validated yield a '-' dash.
                # This is the default splitter for paths.
                else: 
                
                    # Here we validate if the previous character was a '-' dash.
                    # Yield nothing when that is the case.
                    yield '-' if PREVIOUS != '-' else ''
                     
                    # Set the previous character.
                    # When itterating this can be used to prevent double '--' dashes.
                    PREVIOUS = '-'

        validated = self.tail_dash(''.join(list(validate(argument))))

        # Eventhough it is False there is a chance we can fix it anyway.
        if not self.connect(self.ANIME_URL, validated):
                    
            # Maintain the original for whenever we fail to fix it.
            original = validated
                    
            try:
                # We attempt to fix it by removing this value and then retry.
                if 'sub' in validated:
                    validated = self.tail_dash(validated.replace('sub', ''))
                
                if 'dub' in validated:
                    validated = self.tail_dash(validated.replace('dub', ''))
                
                # We tried our bests.
                if not self.connect(self.ANIME_URL, validated):
                    validated = original       
                
            # Pass off any not working attempt. Worth a shot.
            except:
                pass

        return validated

    def search(self, argument, amount = 0, generator = False):
        ''' A coat to handle the generator. '''

        HTML = self.__html__(self.SEARCH_URL, argument)

        try:
            # Get some basic values from the page.
            title   = HTML.title.string.replace('\n', '')
            listing = HTML.find(class_='listing')
        
            # Whenever we are not performing a search.
            if title != 'Find anime':
                raise ValueError 
 
        # Only one anime is found.
        except ValueError:
            return HTML.title.string.split('\n')[1]

        # When the listing class cannot be found, return no results.
        except Exception:
            return []
        
        def search(argument, amount):
            ''''''
    
            # Depending on the set value determine the amount of results.
            # The default is 0, which means all.
            anchors = listing.find_all("a") if amount == 0 else listing.find_all("a")[:int(amount)]

            # Itterate over all the anchor tags.
            for anchor in anchors:

                # Assign the .string value of that anchor tag.
                # A try is used here to filter anime from upcomming episodes.
                # These are also planted in a anchor tag but irrelevant.
                if '?id=' not in anchor.get('href'):
                    yield anchor.string.replace('\n', '')

        return (list(search(argument,amount)) 
                if not generator 
                else search(argument,amount))

    def index(self, argument, generator = False):
        ''''''
    
        HTML = self.__html__(self.ANIME_URL, argument)

        # Format the title to remove excess whitespacing and new lines.
        try:
            anchors = HTML.find_all(href=re.compile("\/Anime\/"))

        except Exception:
            return False
        
        def index():
            for anchor in anchors:
                if "?id=" in anchor.get("href"):
                    yield anchor.get("href")
            
        return (list(index()) 
                if not generator
                else index())

    def extract(self, argument, shorten = False):
        ''''''

        HTML = self.__html__(self.BASE_URL, argument)

        # Extract the base64 source code in the highest possible quality
        try:
            source = HTML.find(id = "selectQuality").find("option")['value']

        except Exception:
            return False
        
        return b64decode(source) if not shorten else self.shorten(b64decode(source))


















