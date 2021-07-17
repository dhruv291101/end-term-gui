%%writefile app.py
import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
#import tensorflow as tf
#from keras.preprocessing import image
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
#from keras.models import load_model

html_temp = """
   <div class="" style="background-color:salmon;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Dhruv Sevak - PIET18CS048</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing End-Term Examination</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Transformations in X $ Y
         """
         )

img1= st.file_uploader("Please upload image 1", type=("jpg", "png"))

import cv2
from  PIL import Image, ImageOps
def import_and_predict():
  image_data = np.zeros((100,100,3), np.uint8)
	   
  image_data[:] = [img1]
  st.image(image_data, use_column_width=True)
  return 0
    
if st.button("Translation"):
  result=import_and_predict()
  
if st.button("About"):
  st.header("Dhruv Sevak")
  st.subheader("Student, Department of Computer Engineering, PIET")
html_temp = """
   <div class="" style="background-color:white;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:black;margin-top:10px;">Digital Image processing EndTerm Lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)

