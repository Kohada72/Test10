"""----------------------------------------------------------------------
File Name       : ImageRecognition.py
Version         : V1.2
Designer        : 平井伸之
Date            : 2024.07.03
Purpose         : レシート画像から文字データを抽出する
----------------------------------------------------------------------"""
"""
Revision :
V1.0 : 平井伸之, 2024.06.11  初期バージョン
V1.01 : 平井伸之, 2024.06.18 jsonファイルのセーブ・ロード機能の追加
V1.1 : 平井伸之, 2024.06.25  OCR結果のソート機能の追加
V1.2 : 平井伸之, 2024.06.03  画像の前処理機能の追加

"""

"""
Package                  Version
------------------------ -----------
blinker                  1.8.2
cachetools               5.3.3
certifi                  2024.6.2
charset-normalizer       3.3.2
click                    8.1.7
colorama                 0.4.6
fasttext-wheel           0.9.2
Flask                    3.0.3
gensim                   4.3.2
google-api-core          2.19.0
google-auth              2.30.0
google-cloud-vision      3.7.2
googleapis-common-protos 1.63.1
grpcio                   1.64.1
grpcio-status            1.62.2
idna                     3.7
itsdangerous             2.2.0
Jinja2                   3.1.4
joblib                   1.4.2
MarkupSafe               2.1.5
numpy                    1.26.4
opencv-contrib-python    4.10.0.84
pandas                   2.2.2
pip                      24.1.2
proto-plus               1.23.0
protobuf                 4.25.3
pyasn1                   0.6.0
pyasn1_modules           0.4.0
pybind11                 2.13.1
python-dateutil          2.9.0.post0
pytz                     2024.1
requests                 2.32.3
rsa                      4.9
scikit-learn             1.5.0
scipy                    1.12.0
setuptools               70.0.0
six                      1.16.0
smart-open               7.0.4
threadpoolctl            3.5.0
tzdata                   2024.1
urllib3                  2.2.1
Werkzeug                 3.0.3
wheel                    0.43.0
wrapt                    1.16.0
"""
from google.cloud import vision
import io
client = vision.ImageAnnotatorClient()
import cv2
import numpy as np
import json
from google.cloud.vision import AnnotateImageResponse

# [START vision_python_migration_text_detection]
def imageRecognition(path): 
    #画像の前処理
    imageDataProcessing(path)
    #OCR結果をソートした文字配列が格納される
    sentence = []
    #ファイル読み込み
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    #google vison
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    #結果をソート
    sentence = get_sorted_lines(response,threshold = 5)

    return sentence
    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
単体テスト用
"texts = response.text_annotations"
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#OCR結果をjsonファイルとして保存
def save_as_json(response, filename):
    data = AnnotateImageResponse.to_json(response)
    with open(filename, mode='wt', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

#OCR結果をjsonファイルをロード        
def load_from_json(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        temp = json.load(file)
    response = AnnotateImageResponse.from_json(temp)
    return response

"""----------------------------------------------------------------------
関数名       : ImageRecognition.py
Designer        : 平井伸之
Date            : 2024.07.03
Purpose         :Boundingboxの左上の位置を参考に行ごとの文章にParseする
    Args:
        response (_type_): VisionのOCR結果のObject
        threshold (int, optional): 同じ列だと判定するしきい値

    Returns:
        line: list of [x,y,text,symbol.boundingbox]
    Args:
        path:画像のpath
----------------------------------------------------------------------"""
def get_sorted_lines(response,threshold = 5):
    # 1. テキスト抽出とソート
    document = response.full_text_annotation
    bounds = []
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols: #左上のBBOXの情報をx,yに集約
                        x = symbol.bounding_box.vertices[0].x
                        y = symbol.bounding_box.vertices[0].y
                        text = symbol.text
                        bounds.append([x, y, text, symbol.bounding_box])
    bounds.sort(key=lambda x: x[1])
    # 2. 同じ高さのものをまとめる
    old_y = -1
    line = []
    lines = []
    sentence = []
    for bound in bounds:
        x = bound[0]
        y = bound[1]
        if old_y == -1:
            old_y = y
        elif old_y-threshold <= y <= old_y+threshold:
            old_y = y
        else:
            old_y = -1
            line.sort(key=lambda x: x[0])
            lines.append(line)
            line = []
        line.append(bound)
    line.sort(key=lambda x: x[0])
    lines.append(line)
    for i in range(len(lines)):
        line = lines[i]
        texts = [i[2] for i in line]
        texts = ''.join(texts)
        sentence.append(texts)
    return sentence

"""----------------------------------------------------------------------
関数名       : ImageRecognition.py
Designer        : 平井伸之
Date            : 2024.07.03
Purpose         : 画像の不要な部分を削除する
    Args:
        path:画像のpath
----------------------------------------------------------------------"""
def imageDataProcessing(path):
    
    #画像読み込み
    img = cv2.imread(path)

    # グレイスケール化
    gray, _ = cv2.decolor(img)
    # 二値化
    ret, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)   
    # 輪郭抽出
    contours, hierarchy = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
    # 面積の大きいもののみ選別
    areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50000:
            ## 輪郭の近似
            epsilon = 0.08*cv2.arcLength(cnt,True) #　＜＜＝＝※3
            approx = cv2.approxPolyDP(cnt,epsilon,True)
            areas.append(approx)
    cv2.drawContours(img,areas,-1,(0,255,0),3)

    # 重心を求める
    cx=cy=0
    for i in areas[0]:
        cx += i[0][0]
        cy += i[0][1]
    cx /=len(areas[0])
    cy /=len(areas[0])

    # 切り取り画像サイズを求める
    h=w=0
    for i in areas[0]:
        if i[0][0]>cx :
            w +=i[0][0]
        else:
            w -=i[0][0]
        #右側
        if i[0][1]>cy:
            #右下
            h += i[0][1]
        else:
            #右上
            h -= i[0][1]

    # 点の順番を求める　tmp
    tmp = []
    for i in areas[0]:
        if i[0][0]>cx :
            #右側
            if i[0][1]>cy:
                #右下
                tmp.append([w,h])
            else:
                #右上
                tmp.append([w,0])
        else:
            #左側
            if i[0][1]>cy:
                #左下
                tmp.append([0,h])
            else:
                #左上
                tmp.append([0,0])
     
    # 射影変換
    dst = []
    pts1 = np.float32(areas[0])
    pts2 = np.float32([tmp])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(img,M,(w,h))
    cv2.imwrite(path,dst)

  
