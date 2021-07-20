
import sys
  
# setting path
sys.path.append('../parentdirectory')

import json
from functions import check_chapters_are_different, get_number
from . import rss
from feed import Feed

class MangaPlusRSS(rss.RSS):
    
    def load_rss(self, data, elements, logger_execution):        
        current_chapter = data['currentChapter']
        elements_reversed = reversed(elements)
        current_element = next(elements_reversed)

        if current_chapter != current_element.text:
            FeedGen = Feed(data['title'], data['description'], data['image'])
            chapters = []
            
            while check_chapters_are_different(current_chapter, current_element.text):
                get_number(current_element.text)                 
                print ('Found new chapter', current_element.text, 'for', data['title'], '!!')
                logger_execution.info('Found new chapter ' + current_element.text + ' for ' + data['title'] + ' !!')
                chapters.append('Chapter ' + current_element.text)
                
                current_element = next(elements_reversed)
            
            data['currentChapter'] = chapters[0].split()[1]
            
            chapters_reversed = list(reversed(chapters))
            for x in range(0, len(chapters_reversed)):
                FeedGen.writeFeed(data['title'], chapters_reversed[x], data['url'])
        
        return data        