from abc import abstractmethod

class RSS():
    
    @abstractmethod
    def load_rss(self, data, elements, logger_execution): 
        raise NotImplementedError