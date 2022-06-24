#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pickle
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
app.model = pickle.load(open("model.pickle", "rb"))

@app.route("/api/american", methods=["POST"])
def classifier():
    model = app.model['model'];
    model_version = app.model['version'];
    model_last_update = app.model['model_date'];
    
    request_data = request.get_json(force=True);
    tweet = request_data['text'];
    if (tweet):
        result = model.predict([tweet]);
        return jsonify(is_american=int(result[0]), version=model_version, model_date=model_last_update)
    return jsonify()
# In[ ]:




