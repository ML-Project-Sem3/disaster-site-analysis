import streamlit as st

success = st.empty()
st.title('Disaster')
st.header('NSUT')
st.set_option('deprecation.showfileUploaderEncoding', False)
select_box = st.sidebar.slider("How much would you rate the accuracy", max_value=10, min_value=0)
feedback = st.sidebar.text_area('Feedback')
file_up = st.file_uploader("Upload the image", type='jpg')
if file_up is not None:
    success.success('Uploaded successfully')
    st.image(file_up, caption="Image You Uploaded", use_column_width=True)
    st.image(file_up, caption="Predicted Image", use_column_width=True)
