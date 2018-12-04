
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CHAR COLON COMMA COMMENT CREATE DECLARATION DOT DOUBLE ELSE ENDLINE EVENTS FOR GET IDENTIFIER IF INITDB INITUI LBrace LET LOCATION LParen METHOD NEW NOTIFY NUMBER RBrace RParen SENDTO SET STRING THEN TITLE TYPE WHILEsettitle : TITLE COLON STRING ENDLINEsetevent : EVENTS COLON STRING ENDLINEsetlocation : LOCATION COLON STRING ENDLINEsetsendto : SENDTO COLON STRING ENDLINEexpression : IDENTIFIER DOT NEW LBrace settitle setevent setlocation setsendto RBrace ENDLINEexpression : IDENTIFIER DOT INITUI LParen RParenexpression : IDENTIFIER DOT INITDB LParen RParen'
    
_lr_action_items = {'TITLE':([0,],[2,]),'$end':([1,5,],[0,-1,]),'COLON':([2,],[3,]),'STRING':([3,],[4,]),'ENDLINE':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'settitle':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> settitle","S'",1,None,None,None),
  ('settitle -> TITLE COLON STRING ENDLINE','settitle',4,'p_set_title','natparse.py',43),
  ('setevent -> EVENTS COLON STRING ENDLINE','setevent',4,'p_set_events','natparse.py',47),
  ('setlocation -> LOCATION COLON STRING ENDLINE','setlocation',4,'p_set_location','natparse.py',51),
  ('setsendto -> SENDTO COLON STRING ENDLINE','setsendto',4,'p_set_sendto','natparse.py',55),
  ('expression -> IDENTIFIER DOT NEW LBrace settitle setevent setlocation setsendto RBrace ENDLINE','expression',10,'p_create_event','natparse.py',59),
  ('expression -> IDENTIFIER DOT INITUI LParen RParen','expression',5,'p_initUI','natparse.py',69),
  ('expression -> IDENTIFIER DOT INITDB LParen RParen','expression',5,'p_initDB','natparse.py',73),
]
