# coding=utf8

import pprint
import os

def theme(context):
	"""	Outputs patterns which recognize ZShell file type symbols and translate them to the values
		indicated by the LS_COLORS environment variable.  The symbols are also stripped from the
		output.  This took some slight modification of colout to make happen.

		Added 'omit' as a style which omits the match from the resulting output
		Added ability to specify raw ANSI codes if the code contains a semi-colon
	"""

	ls_colors = dict(x.split('=') for x in os.getenv('LS_COLORS').rstrip(':').split(':'))
	# ls_colors = os.getenv('LS_COLORS').split(':');
	#	pprint.pprint(ls_colors);
	SymbolMap = {
	 '\ ': ['no', "normal,omit"],
	 '\#': ['bd', "asis,omit"],
	 '\%': ['cd', "asis,omit"],
	 '\*': ['ex', "asis,omit"],
	 '\/': ['di', "asis"],
	 '\=': ['so', "asis,omit"],
	 '\?': ['mi', "asis,omit"],
	 '\@': ['ln', "asis,omit"],
	 '\|': ['pi', "asis,omit"],
	}

	result = [ ]

	for (sym, (ls_code, style)) in SymbolMap.items():
		result.append(["^(.+)(" + sym + ")$", ls_colors.get(ls_code, 'none'), style if ls_code in ls_colors else 'normal,omit'])

	return context, result

'''

Further reference material
--------------------------

ZShell Filename Expansion Types (T) flag, or with LIST_TYPES option
	' '	normal file
	'#'	block special device
	'%'	character special device
	'*'	executable
	'/'	directory
	'='	socket
	'?'	broken symbolic link?
	'@'	symbolic link
	'|'	fifo (named pipe)

LS_COLORS Map, thanks to http://www.bigsoft.co.uk/blog/index.php/2008/04/11/configuring-ls_colors
	bd	BLOCK, BLK	Block device
	ca	???
	cd	CHAR, CHR	Character device
	di	DIR	Directory
	do	DOOR	Door
	ex	EXEC	Executable file (i.e. has ‘x’ set in permissions)
	ln	SYMLINK, LINK, LNK	Symbolix link.
			If you set this to ‘target’ instead of a numerical value,
			the color is as for the file pointed to.
	mh	???
	mi	MISSING	Non-existent file pointed to by a symbolic link (visible when you type ls -l)
	or	ORPHAN	Symbolic link pointing to a non-existent file
	ow	OTHER_WRITABLE	Directory that is other-writable (o+w) and not sticky
	pi	FIFO, PIPE	Named pipe
	rs 	???
	sg	SETGID	File that is setgid (g+s)
	so	SOCK	Socket
	st	STICKY	Directory with the sticky bit set (+t) and not other-writable
	su	SETUID	File that is setuid (u+s)
	tw	STICKY_OTHER_WRITABLE	Directory that is sticky and other-writable (+t,o+w)
	no	NORMAL, NORM	Global default, although everything should be something
	fi	FILE	Normal filevim /t
	lc	LEFTCODE, LEFT	Opening terminal code
	rc	RIGHTCODE, RIGHT	Closing terminal code
	ec	ENDCODE, END	Non-filename text
	*.extension	 	Every file using this extension e.g. *.jpg
'''
