from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# %reload_ext autoreload
# %autoreload 2
# %matplotlib inline

import utils 
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,10)
import rasterio
import numpy as np
from flask import jsonify

def prepare_image():
    #grab sat image
    #theres a list of 12 of them at https://20tree-public.s3-eu-west-1.amazonaws.com/candidates/cloudmask/tif_tiles.txt

    sat_tile = 'Sentinel2L2A_sen2cor_18TUR_20180812_clouds=5.3%_area=99%.tif'

    crop = (5000,5000,512,512)
    #NOTE were only reading first rgb bands here
    #for model predictions we skip the band
    #argument to load all 10 bands
    image, meta = utils.tif_to_image(sat_tile, crop=crop, bands=[3,2,1])
    #meta needed if we want to save the image
    with rasterio.open("test.tif", 'w', **meta) as dst:
        dst.write(image)

    #show it
    fig = plt.figure(figsize=(10,10))
    img = rasterio.open("test.tif").read()
    img = np.clip(img, 0, 2000)/2000.0
    plt.imshow(np.transpose(img, (1,2,0)))

    plt.rcParams["figure.figsize"] = (10,10)

    #meta needed if we want to save the image
    image,meta = utils.tif_to_image(sat_tile, crop=crop) #NOTE no band arg = we load all bands

    with rasterio.open("test.tif", 'w', **meta) as dst:
        dst.write(image)

    # NOTE: if you have the model stored somewhere else, 
    # change the location in utils.infer_image()
    return True


@app.route('/infer/', methods=['POST'])
def infer():
    image_path = request.files['image_path']
    try:
        res = utils.infer_image(file_path=request.files['image_path'].filename, plot=True) #x and y starting point at 5000, were always taking a 512x512 crop
        return jsonify(res.shape, res.tolist())
    except Exception as e:
        return jsonify(e)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
