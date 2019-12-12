
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocEQUALSEQCOMPARENOTEQGREATERTHANLESSTHANleftPLUSMINUSleftMULTIPLYDIVIDEMODCOMMENT CONNECT DEFINE DIVIDE EQCOMPARE EQUALS GREATERTHAN HELP ID IP LBRACKET LESSTHAN LPARENT MINUS MOD MULTIPLY NOTEQ NUMBER PLUS QUIT RBRACKET RESERV RPARENT SEND STARTstatement : quit\n                     | words \n                     | sum\n                     | start_server\n                     | connectconnect : CONNECT IP NUMBERstart_server : START IP NUMBERsum : NUMBER PLUS NUMBERquit : QUIT RESERVwords : ID \n                 | words \n                 | words IDsend : SEND words'
    
_lr_action_items = {'QUIT':([0,],[7,]),'ID':([0,3,8,12,],[8,12,-10,-12,]),'NUMBER':([0,14,15,16,],[9,17,18,19,]),'START':([0,],[10,]),'CONNECT':([0,],[11,]),'$end':([1,2,3,4,5,6,8,12,13,17,18,19,],[0,-1,-2,-3,-4,-5,-10,-12,-9,-8,-7,-6,]),'RESERV':([7,],[13,]),'PLUS':([9,],[14,]),'IP':([10,11,],[15,16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'quit':([0,],[2,]),'words':([0,],[3,]),'sum':([0,],[4,]),'start_server':([0,],[5,]),'connect':([0,],[6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> quit','statement',1,'p_statement','utilities.py',156),
  ('statement -> words','statement',1,'p_statement','utilities.py',157),
  ('statement -> sum','statement',1,'p_statement','utilities.py',158),
  ('statement -> start_server','statement',1,'p_statement','utilities.py',159),
  ('statement -> connect','statement',1,'p_statement','utilities.py',160),
  ('connect -> CONNECT IP NUMBER','connect',3,'p_connect','utilities.py',164),
  ('start_server -> START IP NUMBER','start_server',3,'p_start_server','utilities.py',168),
  ('sum -> NUMBER PLUS NUMBER','sum',3,'p_sum','utilities.py',173),
  ('quit -> QUIT RESERV','quit',2,'p_quit','utilities.py',177),
  ('words -> ID','words',1,'p_words','utilities.py',183),
  ('words -> words','words',1,'p_words','utilities.py',184),
  ('words -> words ID','words',2,'p_words','utilities.py',185),
  ('send -> SEND words','send',2,'p_send','utilities.py',192),
]