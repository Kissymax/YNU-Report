# -*- coding: utf-8 -*-
#coding: utf-8
################################################
def str_isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
################################################
def cul():
          global x
          global y
          print "演算子を入力(+,-,*,/,c) >>",
          op = raw_input()                 
          if len(op) == 1:
            if op in '+':
                mode=1
                print x,
                print "数を入力 >>",
                num = raw_input ()
                if str_isfloat(num) == 1:
                 y=int (num)
                 x=x+y
                 print x,
                 cul()
                else:
                 print x,
                 print "それは数字ではありません",
                 acul()
            elif op in '-':
                mode=2
                print x,
                print "数を入力 >>",
                num = raw_input ()
                if str_isfloat(num) == 1:
                 y=int (num)
                 x=x-y
                 print x,
                 cul()
                else:
                 print x,
                 print "それは数字ではありません",
                 acul()
            elif op in '/':
                mode=3
                print x,
                print "数を入力 >>",
                num = raw_input ()
                if str_isfloat(num) == 1:
                 y=int (num)
                 x=x/y
                 print x,
                 cul()
                else:
                 print x,
                 print "それは数字ではありません",
                 acul()
            elif op in '*':
                mode=4
                print x,
                print "数を入力 >>",
                num = raw_input ()
                if str_isfloat(num) == 1:
                 y=int (num)
                 x=x*y
                 print x,
                 cul()
                else:
                 print x,
                 print "それは数字ではありません",
                 acul()
            elif op in "c":
                x=0
                y=0
                print x,
                acul()
            else:
                print x,
                print "それは演算子ではありません"
                cul()
          else:
           print x,
           print "それは演算子ではありません"
           cul()
################################################
def acul():
   global x
   global y
   print "数を入力 >>",
   num = raw_input ()
   if str_isfloat(num) == 1:
      if mode == 1:
       y = int (num)
       x = x+y
      elif mode == 2:
       y = int (num)
       x = x-y
      elif mode == 3:
       y = int (num)
       x = x/y
      elif mode == 4:
       y = int (num)
       x = x*y
      print x,
      cul()
   else:
      print x,
      print "それは数字ではありません",
      acul()
   cul()
################################################
print "<注>小数には対応してません。"
x = 0
y = 0
print x,
print "数を入力 >>",
mode = 1
num = raw_input ()
if str_isfloat(num) == 1:
      x=int (num)
      print x,
      cul()
else:
      print x,
      print "それは数字ではありません",
      acul()
cul()
