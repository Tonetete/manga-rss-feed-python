import os
import pickle
import shutil
import json
from datetime import datetime, timezone
from feedgen.feed import FeedGenerator
from pathlib import Path

class Feed:
    def __init__(self, title, description, url_img):
        file_contributor = open('data/contributor.json')
        file_host = open('data/host.json')
        
        contributor = json.load(file_contributor)
        self.host_link_rss = json.load(file_host)['host_link_rss']
        
        self.fg = FeedGenerator()
        path_dump_file = 'dumps/' + title + '.obj'

        if not Path(path_dump_file).exists():
            with open(path_dump_file, 'a+') as f:
                self.createFeed(f, title, description, url_img, contributor)
        else:
            with open(path_dump_file, 'rb+') as f:
                self.createFeed(f, title, description, url_img, contributor)
        
        self.fg.lastBuildDate(self.get_current_date())
    
    
    def get_current_date(self):
        today = datetime.now()
        return datetime(
            today.year,
            today.month,
            today.day,
            today.hour,
            today.minute,
            today.second,
            today.microsecond,
            tzinfo=timezone.utc)
    
    
    def createFeed(self, file, title, description, url_img, contributor):
        try:
            self.fg = pickle.load(file)
            file.close();
        except Exception as e:
            self.fg.id(title)
            self.fg.title(title)
            self.fg.image(url=url_img)
            self.fg.description(description)
            self.fg.contributor(name=contributor['contributor_name'], email=contributor['contributor_email'])
            link = self.host_link_rss + title + '.atom'
            self.fg.link( href=link, rel='self' )
            self.fg.language('en')
            file.close();
        
    
    def writeFeed(self, name, title, url):
        fe = self.fg.add_entry()
        fe.id(title)
        fe.title(title)
        
        date_updated = self.get_current_date()
        
        fe.updated(date_updated)
        fe.published(date_updated)        
        fe.link(href=url)
        
        with open('dumps/' + name + '.obj', 'wb+') as f:
            pickle.dump(self.fg, f)
            f.close()
        
        file_path = os.path.abspath(__file__)
        project_path = os.path.dirname(file_path)
        rss_path = os.path.dirname(file_path) + '/rss'
        
        self.fg.atom_file(name + '-atom.xml') # Write the ATOM feed to a file
        self.fg.rss_file(name + '-rss.xml') # Write the RSS feed to a file
        
        shutil.move(project_path + '/' + name + '-atom.xml', rss_path + '/' + name + '-atom.xml')
        shutil.move(project_path + '/' +  name + '-rss.xml', rss_path + '/' + name + '-rss.xml')