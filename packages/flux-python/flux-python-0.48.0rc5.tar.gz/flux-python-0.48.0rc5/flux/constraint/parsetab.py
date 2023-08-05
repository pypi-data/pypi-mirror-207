
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTrightNEGATEAND LPAREN NEGATE NOT OR QUOTE RPAREN TOKEN\n        expression : expression expression %prec AND\n        \n        expression : expression AND expression\n        \n        expression : expression OR expression\n        \n        expression : NOT expression\n                   | NEGATE token\n        \n        expression : LPAREN expression RPAREN\n        \n        expression : token\n        \n        token : TOKEN\n        \n        token : QUOTE TOKEN QUOTE\n        '
    
_lr_action_items = {'NOT':([0,1,2,4,5,6,8,9,10,11,12,13,15,16,17,18,],[2,2,2,-7,2,-8,2,2,2,2,-5,2,2,2,-6,-9,]),'NEGATE':([0,1,2,4,5,6,8,9,10,11,12,13,15,16,17,18,],[3,3,3,-7,3,-8,3,3,3,3,-5,3,3,3,-6,-9,]),'LPAREN':([0,1,2,4,5,6,8,9,10,11,12,13,15,16,17,18,],[5,5,5,-7,5,-8,-1,5,5,-4,-5,5,-2,-3,-6,-9,]),'TOKEN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,],[6,6,6,6,-7,6,-8,14,-1,6,6,-4,-5,6,-2,-3,-6,-9,]),'QUOTE':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,],[7,7,7,7,-7,7,-8,-1,7,7,-4,-5,7,18,-2,-3,-6,-9,]),'$end':([1,4,6,8,11,12,15,16,17,18,],[0,-7,-8,-1,-4,-5,-2,-3,-6,-9,]),'AND':([1,4,6,8,11,12,13,15,16,17,18,],[9,-7,-8,-1,-4,-5,9,-2,9,-6,-9,]),'OR':([1,4,6,8,11,12,13,15,16,17,18,],[10,-7,-8,-1,-4,-5,10,-2,-3,-6,-9,]),'RPAREN':([4,6,8,11,12,13,15,16,17,18,],[-7,-8,-1,-4,-5,17,-2,-3,-6,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,2,5,8,9,10,11,13,15,16,],[1,8,11,13,8,15,16,8,8,8,8,]),'token':([0,1,2,3,5,8,9,10,11,13,15,16,],[4,4,4,12,4,4,4,4,4,4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression expression','expression',2,'p_expression_space','parser.py',352),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parser.py',358),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parser.py',364),
  ('expression -> NOT expression','expression',2,'p_expression_unot','parser.py',375),
  ('expression -> NEGATE token','expression',2,'p_expression_unot','parser.py',376),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parens','parser.py',382),
  ('expression -> token','expression',1,'p_token','parser.py',388),
  ('token -> TOKEN','token',1,'p_expression_token','parser.py',394),
  ('token -> QUOTE TOKEN QUOTE','token',3,'p_quoted_token','parser.py',418),
]
