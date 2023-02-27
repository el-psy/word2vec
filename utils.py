# _*_ coding: utf-8 _*_

import logging
import logging.config
import json


def getlogger(path='./config/log.config.json'):
	# logger=logging.getLogger('simple_example')
	with open(path,'r',encoding='utf-8') as f:
		config=json.load(f)
	logging.config.dictConfig(config)
	return logging

if __name__=='__main__':
	### logger test
	# logger=getlogger('./config/log.config.json')
	# logger.warning('warning')
	# logger.error('error'
	# logger.debug('debug')
	pass