# # fetch captcha from requests
# import requests
# url="https://web.ctf.devclub.in/dev/4/"
# r = requests.get(url)
# print(r.text)
# extract base64 encoded captcha
import base64
# base64_str = r.text.split('base64,')[1]
# print(base64_str)
# # decode base64 encoded captcha
# decoded_str = base64.b64decode(base64_str)
# img=open('captcha.png','wb')
# img.write(decoded_str)
# img.close()

# ocr on image
# import cv2 
# import pytesseract

# img = cv2.imread('captcha.png')
# # cv2.imshow("Image", img)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# # pytesseract.pytesseract.tesseract_cmd=r'C:Program FilesTesseract-OCRtesseract.exe'
# # cv2.waitKey(0)
# text = pytesseract.image_to_string(img)
# print(text)

# send captcha to server
import requests
# url="https://web.ctf.devclub.in/dev/4/"
# r = requests.post(url, data={'captcha':text})
# print(r.text)

import mechanicalsoup
import bs4
import cv2 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
while True:
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(
        url="https://web.ctf.devclub.in/dev/4/")
    res=browser.get_current_page().decode('utf-8')
    browser.select_form()
    string=res.split('base64,')[1]
    decoded_str = base64.b64decode(string)
    img=open('captcha.png','wb')
    img.write(decoded_str)
    img.close()
    img = cv2.imread('captcha.png')
    text = pytesseract.image_to_string(img)
    print(text)
    soup = bs4.BeautifulSoup(res, 'html.parser')
    browser["captcha"] = text
    response = browser.submit_selected()
    print(response.text[response.text.find("Verification"):200])


