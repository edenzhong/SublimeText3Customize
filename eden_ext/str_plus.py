
def str_to_num(s):
	try:
		if ( len(s) > 2 ):
			if (( s[0] == "0" ) and (( s[1] == "x" ) or (s[1] == "X"))):
				return int(s,16)
				#return str_to_hex(s[2:])
		return int(s)
	except Exception:
		return 0