#! /usr/bin/env python
# Copyright (C) 2015 Mirko van der Waal
# Distributed under terms of the MIT license.

from sys import exit as Die

try:
    # Obtain the HTML/Connection.
    import requests

    # Parse it.
    from bs4    import BeautifulSoup as Bs

except ImportError as e:
    print e, Die(0)

class Anime:
    def exists(self, args):
        ''' Validate the existence of all given Anime. '''

        # Define the default path to extend.
        BASE_URL  = "http://kissanime.com/Anime/"

        CONNECTED = []

        def validate(argument):
            ''' Format a anime to fit a path. 
                @return: Generator
            '''

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
    
        def connect(argument): 
            ''' Connect to the kissanime servers with the argument. 
                @return: Boolean
            '''

            # Attempt to create a  connection.
            try:
                # Assume True by default.
                if requests.get(BASE_URL + argument).status_code != 200:
                    return False
                return True

            except Exception as err:
                print err, Die(1)
             
        # Make a lambda to remove the tail dash.
        tail_dash = lambda: dashed[: len(dashed) - 1] if dashed.endswith('-') else dashed

        # If there is only argument. Transform it to a list as we go over all the arguments.
        # If we were not to do this. It would attempt to connect to every character.
        if type(args) in [unicode, str]: args = [args]
        
        # Go over all the arguments passed the exists method.
        for argument in args:
            
            # Make a string of all the characters.
            # To prevent any further confusion the string is converted to lowercase.
            dashed = ''.join(list(validate(argument))).lower()
        
            # Reasign the value without the last character if that is a dash.
            dashed = tail_dash()

            # Eventhough it is False there is a chance we can fix it anyway.
            if connect(dashed) == False:
                
                # Maintain the original for whenever we fail to fix it.
                retr = dashed
                
                # Try for pre-caution.
                try:
                    # We attempt to fix it by removing this value and then retry.
                    if 'sub' in dashed:
                        dashed = dashed.replace('sub', '')
                        dashed = tail_dash()
                    
                    if 'dub' in dashed:
                        dashed = dashed.replace('dub', '')
                        dashed = tail_dash()

                    if not connect(dashed):
                        dashed = retr        
                    
                # Pass off any not working attempt. Worth a shot.
                except:
                    pass
            
            CONNECTED.append({dashed:connect(dashed)})

        # Do not return list format with 1 entry.
        return CONNECTED[0] if len(args) <= 1 else CONNECTED

    def search(self, query, amount = 0):
        ''' Search for a single anime and will only return the first result.'''

        BASE_URL = "http://kissanime.com/Search/Anime/"
        
        RESULTS = []

        try:
            # Attempt create two new objects
            # HTTP Object will serve as an instance of the requests module.
            HTTP = requests
            
            # HTML Object will serve as an instance of the PrettySoup module.
            # It containts the data data from a HTTP request.
            # NOTE: I hate the word beautiful.
            HTML = Bs(str(HTTP.get(BASE_URL + query).content))
        
        except Exception as err:
            print err
            Die(1)


        # Format the title to remove excess whitespacing and new lines.
        try:
            title = HTML.title.string.split('\n')[1]

        except IndexError:
            return 'The resource cannot be found.'

        # This means there is only one result.
        # It is being handeled as the primary result straight away
        if title != 'Find anime':
            return HTML.title.string.split('\n')[1]
        
        else:
            # Get the first listing table, there is only one so no sweat.
            try:
                listing = HTML.find_all(class_='listing')[0]
            
            # Handle the no results were found exception.
            except IndexError:
                return "Your query did not match any results."

            # Depending on the set value determine the amount of results.
            # The default is 0, which means all.
            anchors = listing.find_all("a") if amount == 0 else listing.find_all("a")[:int(amount)]

            # Itterate over all the anchor tags.
            for anchor in anchors:

                # Assign the .string value of that anchor tag.
                # A try is used here to filter anime from upcomming episodes.
                # These are also planted in a anchor tag but irrelevant.
                try:
                    string = anchor.string.split('\n')[1]
                    RESULTS.append(string)

                # When one of those episodes is found you pass ignore it.
                except:
                    pass
              
        return RESULTS[0] if len(anchors) <= 1 else RESULTS

    def index(self, query):
        pass
        ### INDEXING ALGORITHM FOR TOMORROW!

































