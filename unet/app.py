from flask import Flask, jsonify,render_template,request,Response,send_file
from tensorflow.keras.models import load_model
from keras.utils.image_utils import load_img
from keras.utils.image_utils import img_to_array
import matplotlib.pyplot as plt
import numpy as np
import socket
app = Flask(__name__)

def preprocess(filepath):
  model=load_model("model.h5")
  test_img=load_img(filepath,target_size=(128,128))
  test_img_AsArray=img_to_array(test_img)/255.0
  input_data_with_batch = np.expand_dims(test_img_AsArray, axis=0)
  prediction=model.predict(input_data_with_batch)
  prediction_reshaped=prediction.reshape((128,128,2))
  return prediction_reshaped[:,:,0]

@app.post('/pred')
def get_pred():
    img=request.files['image']
    print(img.filename[-4:])
    if img.filename[-4:]==".png" or img.filename[-4:]==".jpg":
       img.save('media/'+img.filename)
       img_processed=preprocess('media/'+img.filename)
       plt.imshow(img_processed,cmap='gray')
       plt.savefig('img')
       return send_file('img.png',mimetype='image/gif')
    return Response('invalid file extension')
@app.get('/')
def index():
   context={"host":socket.gethostname()}
   return render_template('index.html',**context)
       
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
       
