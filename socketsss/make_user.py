import socket
import pickle


class Cnonnect_to_server():
	def __init__():
		pass


def header_space(msg):
	header = 64
	msg_length = len(msg)
	used_header_space = len(str(msg_length))

	print(f"{msg_length}{'-'* (header - used_header_space)}")
	header_with_tie_dash = f"{msg_length}{'-'* (header - used_header_space)}"
	
	return header_with_tie_dash

def get_user_info():	
	clinet_info_dict = {"first_name":"fornnavn", "last_name":"etternavn", "user_name":"brukernavn", "tlf":"tlf"}

	for key in clinet_info_dict.keys():
		clinet_info = input(f"{clinet_info_dict[key]}?") 

		clinet_info_dict[key] = clinet_info


	print(clinet_info_dict)


	return clinet_info_dict

def make_conn(user_info):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("", 12347))
	task_code = "1000"

	task_code = pickle.dumps(task_code)
	print(task_code)
	task_code_length = header_space(task_code)

	s.send(task_code_length.encode("utf-8"))
	s.send(task_code)


	user_info = pickle.dumps(user_info)
	print(user_info)
	user_info_lenght = header_space(user_info)
	print(user_info_lenght)

	s.send(user_info_lenght.encode("utf-8"))
	s.send(user_info)



user_info = get_user_info()
make_conn(user_info)

