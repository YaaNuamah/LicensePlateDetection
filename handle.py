import requests
import base64
import json

def ocr_core(filename):


    IMAGE_PATH = filename
    SECRET_KEY = 'sk_4d0b91bce79fddb6a948b3ec'

    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data = img_base64)
    jsonRes = json.dumps(r.json(), indent=2)
    jsonRes = json.loads(jsonRes)

    for i in jsonRes:

        plate = jsonRes["results"][0]["plate"]
        confidence = jsonRes["results"][0]["confidence"]
        
        if confidence >= 90:
           
            return plate
            return confidence
            break
    
        
    return plate




