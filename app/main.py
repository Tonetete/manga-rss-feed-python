from factory.factory_rss import Factory_RSS
from driver_browser import DriverBrowser
import traceback
import json
import logging
from functions import setup_logger

def main():
    logger_execution = setup_logger('log_execution', 'logs/logs_execution.log')
    logger_error = setup_logger('log_error', 'logs/logs_error.log', level=logging.ERROR)
    
    driver_browser = None
    
    try:
        data_file = open('data/data.json')
        data = json.load(data_file)
        data_to_dump = []
        
        for i in range(0, len(data)):
            driver_browser = DriverBrowser()
            elements = driver_browser.get_elements_by_selector(data[i]['url'], data[i]['selector'])            
            rss = Factory_RSS(data[i]['provider']).get_factory_rss()            
            data_dump = rss.load_rss(data[i], elements, logger_execution)
            data_to_dump.append(data_dump)
            
        data_file = open("data/data.json", "w")
        json.dump(data_to_dump, data_file)
        data_file.close()
        
    except Exception as e:
        print('ERROR', traceback.print_exc())
        logger_error.error(traceback.print_exc())
        
    finally:
        driver_browser.close()
        data_file.close()
        
main()