
def reverse_chars(str):
    reverse = list(str)
    reverse.reverse()
    return ''.join(reverse)

def reverse_words(str):
    reverse = str.split()
    reverse.reverse()
    return ' '.join(reverse)

def reverse_words2(str):
    import re
    reverse = re.split(r'\s+', str)
    reverse.reverse()
    return ' '.join(reverse)

def reverse(alist):
    """
    a helper function to reverse a list
    """
    tmp = alist[:]
    tmp.reverse()
    return tmp

def str_to_num(s):
	try:
		if ( len(s) > 2 ):
			if (( s[0] == "0" ) and (( s[1] == "x" ) or (s[1] == "X"))):
				return int(s,16)
				#return str_to_hex(s[2:])
		return int(s)
	except Exception:
		return 0