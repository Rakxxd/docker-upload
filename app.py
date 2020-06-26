from flask import Flask, request, Response, jsonify, url_for, send_from_directory
import logging, os
from werkzeug import secure_filename
app = Flask(__name__)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = "{}/uploads/".format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPLOAD_FOLDER

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


prdeicted_value = 2239
def getPredictedValue(val):
    return val**2



file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def hello():
    return "Hellow_World!"

@app.route('/GetPrdeiction', methods=['POST'])
def get_Prdeiction():
    request_data= request.get_json()
    if "value" in request_data:
        return jsonify(getPredictedValue(request_data["value"]))
    return "Check Format"

@app.route('/upload')
def upload():
    return """
    <html>
    <head>
        <title>Test Densed Server</title>
    </head>
    <body>
        <h1>Enter your file below</h1>
        <br/><br/>
        <form method="POST" action="/img" enctype=multipart/form-data>
            Upload File <input type="file" name="image"><br />
            <br/><br/>
            <input type="submit" value="Upload"><br />
        </form>
    </body>
</html>
    """

@app.route('/img', methods = ['POST'])
def img():
    app.logger.info(PROJECT_HOME)
    if request.files['image']:
        app.logger.info(UPLOAD_FOLDER)
        img = request.files['image']
        img_name = secure_filename(img.filename)
        #create_new_folder(app.config['UPLOAD_FOLDER'])
        create_new_folder(UPLOAD_FOLDER)
        #saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        saved_path = os.path.join(UPLOAD_FOLDER, img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        app.logger.info("os {}".format(os.path.dirname(os.getcwd())))
        return "done"
        #return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)
    else:
        return "Where is the image?"


if __name__ == "__main__":
	app.run()