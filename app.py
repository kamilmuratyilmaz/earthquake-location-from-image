from maps import location_from_address
from openai_script import extract_and_find_address
from vision import detect_text_uri
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
load_dotenv()

ImageToLocation = Flask(__name__)
ImageToLocation.config.from_object('configuration.config.ProductionConfig')
ImageToLocation.config.from_envvar("APPLICATION_SETTINGS")


@ImageToLocation.route('/image-to-location', methods=['POST'])
def image_to_location():
    if request.method == 'POST':
        image_url = request.json['image_url']
        text_from_image = detect_text_uri(image_url)
        address = extract_and_find_address(text_from_image)

        # Find location as latitude and longitude
        location = location_from_address(address)
        return jsonify(location)


if __name__ == '__main__':
    ImageToLocation.run(host=os.environ.get("FLASK_HOST"),
                        port=os.environ.get("FLASK_RUN_PORT"),
                        threaded=os.environ.get("THREADED"))
