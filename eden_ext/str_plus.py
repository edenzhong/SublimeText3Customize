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

def get_sub_str(s,idx,len):
    try:
        return s[idx,idx+len]
    except Exception:
        return EOF

def clear_cpp_comment(s):
    l = len(s)
    payload = 0
    c_cmt = 1
    cpp_cmt = 2
    state = payload
    return_string = ""
    i = 0

    try:
        while i<l:
            if ( state == c_cmt):
                if(s[i:i+2]=="*/"):
                    state = payload
                    i = i + 1
            elif ( state == cpp_cmt):
                if ( s[i] == "\n"):
                    state = payload
            else: # ( state == payload ):
                if(s[i:i+2] == "/*"):
                    state = c_cmt
                    i = i + 1
                elif(s[i:i+2] == "//"):
                    state = cpp_cmt
                    i = i + 1
                else:
                    return_string += s[i]
            
            i = i + 1
    except Exception:
        sublime.message_dialog("exception")
    return return_string

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
    