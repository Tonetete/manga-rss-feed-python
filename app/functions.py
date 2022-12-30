from distutils.dir_util import copy_tree
import re
import sys
import logging

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]    

def get_number(s):
    return re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)


def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def check_chapters_are_different(current_chapter, chapter):
    number_current_chapter = get_number(current_chapter)
    number_chapter = get_number(chapter)
    
    if len(number_chapter) > 0 and len(number_current_chapter) > 0 and number_chapter[0] != current_chapter[0]:
        if float(number_current_chapter[0]) < float(number_chapter[0]):
            return True
        else:
            return False
    elif current_chapter != chapter:
        return True
    else:
        return False
 
def copy_rss_folder():
    try:
        rss_path = '/usr/src/app/rss'
        desination_rss_path = '/usr/src/rss'

        copy_tree(rss_path, desination_rss_path)

    except Exception as e:
        print('ERROR', e)  
