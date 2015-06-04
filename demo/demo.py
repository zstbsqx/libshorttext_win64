#!/usr/bin/env python

import sys, os
sys.path += ['..']
from libshorttext.analyzer import *

if __name__ == '__main__':
  print(1)
  predict_result = InstanceSet('predict_result')
  print(2)
  analyzer = Analyzer('train_file.model')
  print(3)
  insts = predict_result.select(wrong, with_labels(['Books', 'Music', 'Art', 'Baby']), sort_by_dec, subset(100))
  print(4)
  analyzer.info(insts)
  print(5)
  analyzer.gen_confusion_table(insts)
  print(6)
  insts.load_text()
  print(7)
  print(insts[61])
  print(8)
  analyzer.analyze_single(insts[61], 3)
  print(9)
  analyzer.analyze_single('beatles help longbox sealed usa 3 cd single', 3)
  print(10)
