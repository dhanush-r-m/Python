import logging
## logging settings

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
    )

logger = logging.getLogger("Arthmetic app")

def add(x,y):
    result = x + y
    logger.debug(f"adding {x} + {y} = {result}")
    return result

def subtract(x,y):
    result = x - y
    logger.debug(f"subtracting {x} - {y} = {result}")
    return result

def multiply(x,y):
    result = x * y
    logger.debug(f"multiplying {x} * {y} = {result}")
    return result

def divide(x,y):
    try:
        result = x / y
        logger.debug(f"dividing {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero")
        return None
    
add(1,2)
subtract(2,1)
multiply(2,3)
divide(3,4)