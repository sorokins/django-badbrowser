__version__ = "1.0.12"
import os
from django.conf import settings

def check_user_agent(user_agent, requirements):
    import httpagentparser
    from pkg_resources import parse_version
    
    if not user_agent:
        return True
    
    if not requirements:
        return True
    
    if type(user_agent) == httpagentparser.Result or type(user_agent) == dict:
        parsed = user_agent
    else:
        parsed = httpagentparser.detect(user_agent)
    
    if "browser" not in parsed:
        return True
    
    if "name" not in parsed["browser"]:
        return True
    
    if "version" not in parsed["browser"]:
        return True
    
    user_browser = parsed["browser"]["name"].lower()
    user_browser_version = parsed["browser"]["version"]
    import logging
    logger = logging.getLogger('browser_detection')
    log_path = os.path.join(settings.PROJ_PATH, 'log')
    try:
        os.mkdir(log_path, 0744)
    except OSError:
        pass
    hdlr = logging.FileHandler(os.path.join(log_path, 'browser_detection.log'))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.WARNING)
    logger.info(user_browser_version)
    logger.info(user_agent)
    for browser, browser_version in requirements:
        if user_browser == browser.lower():
            if not browser_version:
                return True
            if cmp(parse_version(browser_version), parse_version(user_browser_version)) <= 0:
                return True
            else:
                return False

    return True
