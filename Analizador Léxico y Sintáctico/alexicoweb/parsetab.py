
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMA COMILLA END IDENTIFICADOR IGUAL INT LABIERTO LCERRADO PABIERTO PCERRADO PRINTF PROGRAMA PUNTOCOMA READ SUMA VARIABLEprograma : PROGRAMA IDENTIFICADOR PABIERTO PCERRADO LABIERTO cuerpo LCERRADOcuerpo : inicializacion leer igual imprimir final inicializacion : INT variables PUNTOCOMAvariables : VARIABLE variables\n                   | COMA variables\n                   | vacio\n                   leer : READ VARIABLE PUNTOCOMA leer\n              | READ VARIABLE PUNTOCOMAigual : VARIABLE IGUAL VARIABLE SUMA VARIABLE PUNTOCOMAimprimir : PRINTF PABIERTO COMILLA cadena COMILLA PCERRADO PUNTOCOMAcadena : CADENA CADENA CADENA\n                final : END PUNTOCOMAvacio :'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,10,],[0,-1,]),'IDENTIFICADOR':([2,],[3,]),'PABIERTO':([3,24,],[4,29,]),'PCERRADO':([4,38,],[5,41,]),'LABIERTO':([5,],[6,]),'INT':([6,],[9,]),'LCERRADO':([7,27,32,],[10,-2,-12,]),'READ':([8,20,26,],[12,-3,12,]),'VARIABLE':([9,11,12,14,15,25,26,31,34,],[14,18,19,14,14,30,-8,-7,37,]),'COMA':([9,14,15,],[15,15,15,]),'PUNTOCOMA':([9,13,14,15,16,19,21,22,28,37,41,],[-13,20,-13,-13,-6,26,-4,-5,32,40,43,]),'PRINTF':([17,40,],[24,-9,]),'IGUAL':([18,],[25,]),'END':([23,43,],[28,-10,]),'COMILLA':([29,35,42,],[33,38,-11,]),'SUMA':([30,],[34,]),'CADENA':([33,36,39,],[36,39,42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'cuerpo':([6,],[7,]),'inicializacion':([6,],[8,]),'leer':([8,26,],[11,31,]),'variables':([9,14,15,],[13,21,22,]),'vacio':([9,14,15,],[16,16,16,]),'igual':([11,],[17,]),'imprimir':([17,],[23,]),'final':([23,],[27,]),'cadena':([33,],[35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAMA IDENTIFICADOR PABIERTO PCERRADO LABIERTO cuerpo LCERRADO','programa',7,'p_programa','sintactico.py',10),
  ('cuerpo -> inicializacion leer igual imprimir final','cuerpo',5,'p_cuerpo','sintactico.py',13),
  ('inicializacion -> INT variables PUNTOCOMA','inicializacion',3,'p_inicializacion','sintactico.py',16),
  ('variables -> VARIABLE variables','variables',2,'p_variables','sintactico.py',19),
  ('variables -> COMA variables','variables',2,'p_variables','sintactico.py',20),
  ('variables -> vacio','variables',1,'p_variables','sintactico.py',21),
  ('leer -> READ VARIABLE PUNTOCOMA leer','leer',4,'p_leer','sintactico.py',29),
  ('leer -> READ VARIABLE PUNTOCOMA','leer',3,'p_leer','sintactico.py',30),
  ('igual -> VARIABLE IGUAL VARIABLE SUMA VARIABLE PUNTOCOMA','igual',6,'p_igual','sintactico.py',39),
  ('imprimir -> PRINTF PABIERTO COMILLA cadena COMILLA PCERRADO PUNTOCOMA','imprimir',7,'p_imprimir','sintactico.py',55),
  ('cadena -> CADENA CADENA CADENA','cadena',3,'p_cadena','sintactico.py',58),
  ('final -> END PUNTOCOMA','final',2,'p_final','sintactico.py',62),
  ('vacio -> <empty>','vacio',0,'p_vacio','sintactico.py',77),
]
