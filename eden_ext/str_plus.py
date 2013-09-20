import re

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

def clear_comment(s,syntax_type="cpp"):
    if ( "cpp" == syntax_type ):
        lns = s.splitlines()
        s = ""
        for ln in lns:
            ln = re.sub("//[^\n$]*","",ln)
            if ( len(s)>0):
                s += "\n"
            s += ln
    
    return s

def get_indent_of_string(s):
    mo = re.search("^[ \t]+(?=[^ \t$])", s)
    if (mo):
        return mo.group(0)
    else:
        return ""

def get_file_name_from_full(full):
    match = re.search("[^\\\/]+$",full)
    if ( match ):
        name = match.group(0)
        match = re.search("^[^\.]+",name)
        if (match):
            return match.group(0)
    return full

def get_word_by_idx(s,idx):
    match = re.findall("\w+",s)
    if ( match ):
        if ( idx > 0 ):
            if ( len(match)>idx):
                return match[idx]
        elif (len(match)>=(-idx)):
            return match[idx]
    return None
    