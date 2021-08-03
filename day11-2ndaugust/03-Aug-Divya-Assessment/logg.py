import logging


#logging.basicConfig(filename = "demo.log" ,level=logging.DEBUG)         # to change default level
logging.basicConfig(level=logging.DEBUG)
logging.warning("excepted value is in integer") # default level
logging.error("an unknown error happened")
logging.critical("critical error")
logging.info("Normal message")
logging.debug("for developers")

# x = 10
# y = 20
# z =x+y
# logging.info(z)

