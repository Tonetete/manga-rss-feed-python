from . import manga_plus_rss


class Factory_RSS():
    
    def __init__(self, provider):
        self.rss = {
            "mangaplus": manga_plus_rss.MangaPlusRSS
        }                

        self.factory_rss = self.rss[provider]()
    
    def get_factory_rss(self):
        return self.factory_rss