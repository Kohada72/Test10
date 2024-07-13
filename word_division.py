"""----------------------------------------------------------------------
File Name       : word_division.py
Version         : V1.1
Designer        : 和田一真
Date            : 2024.06.09
Purpose         : レシート画像の解析データから食材名の抽出をする。
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 和田一真  2024.06.09  初期バージョン
V1.1 : 和田一真  2024.06.18  制御用関数(wordDivision)追加
V1.2 : 和田一真  2024.07.13  非ASCII環境対応
"""
"""
Package Requirement
-----------------------------------
fasttext-wheel 0.9.2   (Windows)
numpy          1.26.4
pip            23.0.1
pybind11       2.12.0
setuptools     67.6.0
wheel          0.38.4
"""

# -*- coding: utf-8 -*-

import fasttext
import numpy as np
import re

#判定用食材リスト
ingredients_list = [
    "りんご", "バナナ", "にんじん", "トマト", "じゃがいも", "レタス", "たまねぎ", "にんにく",
    "鶏", "牛", "豚", "肉", "魚", "米", "パスタ", "パン", "チーズ", "牛乳",
    "卵", "バター", "塩", "胡椒", "砂糖", "蜂蜜", "ぶり", "鮭"
]

#未知語のリスト
unknown_list = [
    "にら"
]

#除外語リスト
modifiers = [
    "釣", " ", "　"
]

#初期化
model_path = "./models/cc.ja.300.bin"
model = fasttext.load_model(model_path)  #モデルのロード
ingredient_vectors = {ingredient: model.get_word_vector(ingredient) for ingredient in ingredients_list}  #ベクトルの事前計算

#類似度計算関数
def cosineSimilarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
    return dot_product / (norm_vec1 * norm_vec2)

#食材判定関数
def isIngredient(word, threshold=0.45):
    for j in range(1, len(word) + 1):
        res = [word[i:i+j] for i in range(0, len(word) + 1 - j)]
        for text in res:
            word_vector = model.get_word_vector(text)
            if(not np.any(word_vector)):
                for unknown in unknown_list:
                    if unknown in text:
                        return True
            else:
                for ingredient, ingredient_vector in ingredient_vectors.items():
                    similarity = cosineSimilarity(word_vector, ingredient_vector)
                    if similarity > threshold:
                        return True
    return False

#キーワードの抽出
def extractKeywords(word):
    pattern = r'[*＊〇◎☆¥#!()【】a-zA-Z0-9０-９]'
    phrase = re.sub(pattern, '', word)
    for modifier in modifiers:
        phrase = phrase.replace(modifier, "")
    return phrase

#制御用関数
def wordDivision(data_array):
    divided_list = []
    for word in data_array:
        text = extractKeywords(word)
        if(len(text) == 0):
            continue
        if(isIngredient(text)):
            divided_list.append(text)
    return divided_list
