import json

import files.file_functions as ff
from bitstring import BitArray

current_log = ""
current_best = ""
last_best = ""


def init_new_session():
	__init_prev_best()
	__increase_session_number()
	__init_new_session_files()


def add_log(data):
	ff.add_to_file(current_log, data)


def save_best(data: BitArray):
	file = open(file=current_best, mode='wb')
	data.tofile(file)
	file.close()


def get_mutations_num():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	return conf['max_num_of_mutations']


def get_bots_num():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	return conf['number_of_bots']


def get_mutation_chance():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	return conf['mutation_chance_percent']


def get_spawn_mode():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	return int(conf['spawn_mode'])


def get_keep_only_best():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	return bool(conf['keep_only_best'])


def get_init_from_last():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	return bool(conf['init_from_last'])


def get_prev_best():
	return last_best


def __init_prev_best():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	global last_best
	last_best = str(ff.LOGS_DIR + 'best-' + str(conf['session_number']) + ".bin")


def __increase_session_number():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	conf['session_number'] = conf['session_number'] + 1

	with open(ff.CONF_FILE, 'w') as json_file:
		json.dump(conf, json_file)


def __init_new_session_files():
	data = ff.read_from_file(ff.CONF_FILE)
	conf = json.loads(data)

	log_name = 'log-' + str(conf['session_number']) + ".txt"
	best_name = 'best-' + str(conf['session_number']) + ".bin"

	global current_log
	global current_best
	current_log = str(ff.LOGS_DIR + log_name)
	current_best = str(ff.LOGS_DIR + best_name)

	with open(current_log, 'w') as json_file:
		json.dump(conf, json_file)

	ff.write_to_file(current_best, "")
