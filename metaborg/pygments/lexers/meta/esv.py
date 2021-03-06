import re
from pygments.lexer import RegexLexer, words
from pygments.token import *

class ESVLexer(RegexLexer):
    name      = 'ESV'
    aliases   = ['esv']
    filenames = ['*.esv']

    tokens = {
        'root': [
            (words(('module','imports',
                    'language','name','description','extensions','table','start','symbols','provider','observer','context',
                    'menus','menu','action','openeditor','source','meta','realtime',
                    'shell','evaluation method','shell start symbol',
                    'line comment','block comment','fences'), suffix=r'\b'), Keyword),
            (r'"[^"^\n]*"', Literal.String),
            (r'[\.\,\|\[\]\(\)\{\}\<\>\;\:\*]', Text.Punctuation),
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*?$', Comment.Singleline),
            (r'\s+', Text.Whitespace),
            (r'.', Text),
        ],
        'comment': [
            (r'[^*/]', Comment.Multiline),
            (r'/\*', Comment.Multiline, '#push'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[*/]', Comment.Multiline)
        ],
    }
