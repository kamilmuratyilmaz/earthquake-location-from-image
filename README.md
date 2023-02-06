## Hello, the idea for creating this repo has come into my mind after the tragic earthquakes in Turkey.

While I was browsing Twitter, I saw many people sharing only photos and address information of people under the rubble. In response to this, I thought about how I could quickly extract latitude and longtitude data from the URL addresses of the photos and prepared useful data to act quickly for the people whom need help.

Simply, the photo first passes through the Google Vision API and the incoming text data is converted into a regular address by passing through the OpenAI text-davinci-003 model. With this address information, longtitude and latitude data of the individual under the rubble are obtained via Google Maps API.

To run the program, you must first fill in the required fields in the .env. Since I cannot afford it financially, I can only write the script, if you can contribute to this issue, please use this script.

You can install gunicorn as a WSGI server to host the program in linux environment, it is available in requirements.txt.

<img src = "https://github.com/kamilmuratyilmaz/earthquake-location-from-image/blob/production/Postman%20Example.png" alt="Postman Example">
