"""Detects text in the file."""
from google.cloud import vision
import io
client = vision.ImageAnnotatorClient()

# [START vision_python_migration_text_detection]
def imageRecognition(): 
    lines = []
    path = "C:\\Users\\nobu2\\Desktop\\todo-app\\img_1942_720.jpg"
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    sentence = get_sorted_lines(response,threshold = 5)
    return sentence
    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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

import json
from google.cloud.vision import AnnotateImageResponse

def save_as_json(response, filename):
    data = AnnotateImageResponse.to_json(response)
    with open(filename, mode='wt', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        
def load_from_json(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        temp = json.load(file)
    response = AnnotateImageResponse.from_json(temp)
    return response

def get_sorted_lines(response,threshold = 5):
    """Boundingboxの左上の位置を参考に行ごとの文章にParseする

    Args:
        response (_type_): VisionのOCR結果のObject
        threshold (int, optional): 同じ列だと判定するしきい値

    Returns:
        line: list of [x,y,text,symbol.boundingbox]
    """
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




