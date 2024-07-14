"""----------------------------------------------------------------------
File Name       : ImageRecognition.py
Version         : V1.0
Designer        : 平井伸之
Date            : 2024.07.13
Purpose         : 画像解析
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 平井伸之, 2024.07.13  初期バージョン

""
------------------------ -----------"""

from word_division import wordDivision
from imageRecognition import imageRecognition

#pathを受け取り画像解析を行う
def imageAnalysis(path):
    ingredient_list = []
    data_array = imageRecognition(path)
    print(data_array)
    ingredient_list=wordDivision(data_array)
    print(ingredient_list)
    return ingredient_list