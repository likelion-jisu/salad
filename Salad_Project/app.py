from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port='5000')

@app.route('/mongo',methods=['GET'])
def mongoTest():
    uri = "mongodb://localhost"
    client = MongoClient(uri)
    
    db = client.saladDB
    collection = db.reservation
    results = collection.find()
    client.close()
    return render_template('reservation_list.html', data=results)
