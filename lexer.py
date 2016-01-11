import sys,ply.lex

keywords = {'args' : 'ARGUEMENTS','int' : 'TYPE_INT'}

tokens = ['STRING','REALNUMBER','INT_CONST','HEXANUM','EXPONENTIALNUM', ]+list(keywords.values())

t_ignore_COMMENT        = r"//[^\n]+|"r"/\*[^(\*/)]+(\*/)"
t_REALNUMBER		= r'(\d*\.\d+)|(\d+\.\d*)'
t_INT_CONST		= r'\d+'
t_HEXANUM		= r'0[xX][0-9a-fA-F]+'
t_EXPONENTIALNUM	= r'((\d*\.\d+)|(\d+\.\d*)|\d+)(e|E)(\+|-)?\d+'




def t_error(t):
	print "Unrecognized character skipped : '%s'" % t.value[0]
	t.lexer.skip(1)

def t_STRING(t):
        r"(?P<start>\"|')[^\"']*(?P=start)"
        t.value	= t.value.replace("\"","").replace("'","")
        return t


lexer = ply.lex.lex()

def lex_output(input):
	


