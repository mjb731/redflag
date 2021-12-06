# This should be server running solution, i.e. bootable to start on server or personal computer (consider using like: Flask, Django, Falcon)
# All the parts described below should be connected together in order to boot it all at once on a machine.
# The crawler part:
#     Select one social network of your choice (like Instagram, Twitter)
#     The crawler should return up to 5 images found searched by keyword
# ML part:
#     Choose a very simple ML model of your choice to classify images (also, your choice)
#     Accuracy doesn't matter much for this assignment
# The API would have two endpoints:
#     Search via crawler (described below) by keyword on a social network and return ML analysis
#         The flow would be: API request with keyword >> crawler searches and downloads up to 5 images on a social network >> ML model performs analyses over the images >> API responds with results in JSON the request
#     Uploading images directly and getting ML analysis for that image
#         The flow would be: API request with image file >> ML model perform analysis over the image >> API responds with results in JSON the request

from flask import Flask, jsonify, request
from PIL import Image

from crawler import Crawler
from model import Model

app = Flask(__name__)

# app level objects
app_model = Model()
app_crawler = Crawler()


@app.route('/search/<search>', methods=['GET'])
def do_search(search):
    # get top 5 images
    images = app_crawler.crawl(search)

    # get the classifications for those images
    classifications = []
    for image in images:
        classifications.append(app_model.predict(image))

    resp = jsonify(classifications=classifications)
    resp.status_code = 200
    return resp


@app.route('/upload', methods=['POST'])
def do_upload():
    # predict the image file
    image = request.files['file']
    image_obj = Image.open(image)
    classification = app_model.predict(image_obj)

    resp = jsonify(classification=classification)
    resp.status_code = 200
    return resp
