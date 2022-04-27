from __future__ import division
from PIL import Image
import math
import os

def long_slice(image_path, out_name, outdir, slice_size):
    """slice an image into parts slice_size tall"""
    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))

    count = 1
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  
        #set the bounding box! The important bit     
        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        working_slice.save(os.path.join(outdir, "slice_" + out_name + "_" + str(count)+".png"))
        count +=1

if __name__ == '__main__':
    #slice_size is the max height of the slices in pixels
    #long_slice("03-12-22.png", "longcat",os.getcwd(), 2000)
  
   long_slice("/Users/zahinroja/Downloads/data/fox/03-12-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/12", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-13-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/13", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-14-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/14", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-15-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/15", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-16-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/16", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-17-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/17", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-18-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/18", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-19-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/19", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-20-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/20", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-21-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/21", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-22-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/22", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-23-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/23", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-24-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/24", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-25-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/25", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-26-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/26", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-27-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/27", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-28-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/28", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-29-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/29", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-30-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/30", 2000)
   long_slice("/Users/zahinroja/Downloads/data/fox/03-31-22.png","longcat", "/Users/zahinroja/Downloads/data/fox_2000px/31", 2000)
   
   
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-01-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/01", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-02-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/02", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-03-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/03", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-04-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/04", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-05-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/05", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-06-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/06", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-07-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/07", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-08-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/08", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-09-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/09", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-10-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/10", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-11-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/11", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-12-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/12", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-13-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/13", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-14-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/14", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-15-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/15", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-16-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/16", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-17-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/17", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-18-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/18", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-19-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/19", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-20-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/20", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-21-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/21", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-22-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/22", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-23-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/23", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-24-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/24", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-25-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/25", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-26-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/26", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-27-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/27", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-28-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/28", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-29-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/29", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-30-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/30", 2000)
   long_slice("/Users/zahinroja/Downloads/data/cnn/03-31-22.png","longcat", "/Users/zahinroja/Downloads/data/cnn_2000px/31", 2000)
   
   
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-01-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/01", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-02-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/02", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-03-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/03", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-04-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/04", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-05-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/05", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-06-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/06", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-07-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/07", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-08-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/08", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-09-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/09", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-10-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/10", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-11-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/11", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-12-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/12", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-13-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/13", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-14-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/14", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-15-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/15", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-16-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/16", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-17-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/17", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-18-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/18", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-19-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/19", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-20-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/20", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-21-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/21", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-22-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/22", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-23-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/23", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-24-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/24", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-25-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/25", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-26-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/26", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-27-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/27", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-28-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/28", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-29-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/29", 2000)
   long_slice("/Users/zahinroja/Downloads/data/aljazeera/03-30-22.png","longcat", "/Users/zahinroja/Downloads/data/aljazeera_2000px/30", 2000)
   

