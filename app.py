import os
import cv2
from flask import Flask, render_template, request, redirect
from artify import ClusterImage


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True



# GET Index Route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')




# GET, POST Image Upload Route
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            ext = image.filename.split(".")[-1]
            if ext in ['.png', 'jpg', 'jpeg', 'bmp']:
                user_imgname = "user_img."+ ext
                image.save( os.path.join("static/images/", user_imgname) )
                print("Image" + user_imgname + "Saved")

                # Image Processing
                iterations=10
                k=15
                artified = ClusterImage("static/images/"+user_imgname)
                artified = cv2.cvtColor(artified, cv2.COLOR_RGB2BGR)
                cv2.imwrite("static/images/clustered_output.jpg", artified)
                print("Processed Image saved")

                return redirect('/output')

            else:
                print("Image Type not supported")

            return redirect(request.url) 


    return render_template("upload_image.html")



# GET Output Route
@app.route('/output', methods=["GET"])
def output_image():
    return render_template("output.html")





if __name__ == "__main__":
    app.run(debug=True)