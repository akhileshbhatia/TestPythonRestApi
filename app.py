from flask import Flask,current_app,jsonify

app = Flask(__name__)

@app.route("/api/imageName")
def imageName():
    name ="hashbrown.jpg" 
    return jsonify(image_name=name)


@app.route("/")
def init():
    return current_app.send_static_file("file1.html")

if __name__ == '__main__':
    app.run(debug = True)