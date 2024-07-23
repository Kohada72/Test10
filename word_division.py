"""----------------------------------------------------------------------
File Name       : word_division.py
Version         : V1.4
Designer        : 和田一真
Date            : 2024.06.09
Purpose         : レシート画像の解析データから食材名の抽出をする。
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 和田一真  2024.06.09  初期バージョン
V1.1 : 和田一真  2024.06.18  制御用関数(wordDivision)追加
V1.2 : 和田一真  2024.07.13  非ASCII環境対応
V1.3 : 和田一真  2024.07.13  高効率モデル(ja_100)にも対応
V1.4 : 和田一真  2024.07.14  wordDivisionの戻り値をdictへ変更
"""

import fasttext
import numpy as np
import re

ingredients_list = [
    "りんご", "バナナ", "にんじん", "トマト", "じゃがいも", "レタス", "たまねぎ", "にんにく",
    "鶏", "牛", "豚", "肉", "魚", "米", "パスタ", "パン", "チーズ", "牛乳",
    "卵", "バター", "塩", "胡椒", "砂糖", "蜂蜜", "鮭", "オレンジ", "豆腐"
]

unknown_list = [
    "にら", "トウフ"
]

modifiers = [
    "釣", " ", "　"
]

"""----------------------------------------------------------------------
Function Name   : loadModel
Designer        : 和田一真
Date            : 2024.07.21
Function        : モデルのロード・キャッシュ化を行う．
Argument        : なし
Return          : なし
----------------------------------------------------------------------"""
def loadModel():
    global model, ingredient_vectors
    model_path = "./models/ja_100.bin"  #cc.ja.300 or ja_100
    model = fasttext.load_model(model_path)  #モデルのロード
    ingredient_vectors = {ingredient: model.get_word_vector(ingredient) for ingredient in ingredients_list}  #ベクトルの事前計算

"""----------------------------------------------------------------------
Function Name   : cosineSimilarity
Designer        : 和田一真
Date            : 2024.06.09
Function        : 比較する単語ベクトルのコサイン類似度を計算する．
Argument        : vec1, vec2 比較する単語のベクトル
Return          : ベクトルのコサイン類似度
----------------------------------------------------------------------"""
def cosineSimilarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0
    return dot_product / (norm_vec1 * norm_vec2)

"""----------------------------------------------------------------------
Function Name   : isIngredient
Designer        : 和田一真
Date            : 2024.06.09
Function        : 単語が食材名であるかを判定する．
Argument        : word 判定する単語, threshold 判定の閾値
Return          : 食材名かどうかの真偽値
----------------------------------------------------------------------"""
def isIngredient(word, threshold=0.67):  #cc.ja.300なら0.45, ja_100なら0.67
    for j in range(1, len(word) + 1):
        res = [word[i : i+j] for i in range(0, len(word) + 1 - j)]
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

"""----------------------------------------------------------------------
Function Name   : extractKeywords
Designer        : 和田一真
Date            : 2024.06.09
Function        : 入力された単語から不要な文字列を除去する．
Argument        : word 単語
Return          : phrase 抽出後の単語
----------------------------------------------------------------------"""
def extractKeywords(word):
    pattern = r'[*＊※〇◎☆¥#!()【】a-zA-Z0-9０-９]'
    phrase = re.sub(pattern, '', word)
    for modifier in modifiers:
        phrase = phrase.replace(modifier, "")
    return phrase

"""----------------------------------------------------------------------
Function Name   : wordDivision
Designer        : 和田一真
Date            : 2024.07.15
Function        : 文字列から食材名のdict配列を取り出す.
Argument        : data_array 判定したい単語を含んだ単語の配列
Return          : divided_list 抽出された単語を入れたdict配列
----------------------------------------------------------------------"""
def wordDivision(data_array):
    divided_list = []
    for word in data_array:
        text = extractKeywords(word)
        if(len(text) == 0):
            continue
        if(isIngredient(text)):
            ingredient = {
                "name": text,
                "quantity": 0,
                "unit": "g"
            }
            divided_list.append(ingredient)

    return divided_list
