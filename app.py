import streamlit as st
from PIL import Image
from model import predict, hikaku

st.set_option("deprecation.showfileUploaderEncoding", False)
st.sidebar.title("Take a photo of your dogs")
st.sidebar.write("Let me make a guess about breeds of your dogs")
st.sidebar.write("")
img_source = st.sidebar.radio("How upload?",("select file","take a photo"))
if img_source == "select file":
    img_file = st.sidebar.file_uploader("Choose the photo",type=["png","jpg","jpeg"])
elif img_source == "take a photo":
    img_file = st.camera_input("Let's shoot")

if img_file is not None:
    with st.spinner("guessing..."):
        img = Image.open(img_file)
        st.image(img, caption="Target", width=480)
        st.write("")
        result = predict(img)
        st.write(f"## This dog is {result[0]}")
        link = f"[related pics](https://www.pinterest.jp/search/pins/?q={result[0]}&rs=typed)"
        st.markdown(link, unsafe_allow_html=True)
        st.write("")
        st.write(f"## The dog is similar to {result[2]}")
        st.image(result[1], caption="you might like this dog", width=300)
        link1 = f"[this dog is waiting for you](https://www.pinterest.jp/search/pins/?q={result[2]}&rs=typed)"
        st.markdown(link1, unsafe_allow_html=True)

st.sidebar.caption("""Used traindatasets by Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. \n
First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011. [pdf] [poster] [BibTex]\n
Secondary:J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li and L. Fei-Fei, ImageNet: A Large-Scale Hierarchical Image Database. IEEE Computer Vision and Pattern Recognition (CVPR), 2009. [pdf] [BibTex]\n
Licence is Creative Commons Attribution-ShareAlike 4.0 International License.""")