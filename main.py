import streamlit as st
import genAi_helper
# Title
st.title("Restaurant Name And Menu Generator !!!")
cuisine = st.sidebar.selectbox(
    'Pick a Cuisine', ("Indian", "Italian", "Maxican", "Tamil"))


def generate_restaurant_name_and_items(cuisine):
    return {

        'restaurant_name': 'Curry Delight',
        'menu_items':'samosa, panner'
        }
if cuisine :

    response =  generate_restaurant_name_and_items(cuisine)
    #
    # menu_items = response['menu_items'].split(",")
    
    response = genAi_helper.LLM_MODEL(cuisine)
    st.header("Resturnment Name")  
    st.write(response['Resturnment'].replace(".",""))
  
    st.header("**Menu Items**")
    get_ind = str(response['Menu']).index(":")
    for item in response['Menu'][get_ind+3::].split(","):
        if len(item) > 2:
            st.write(item)
    st.header("Connact With Me")
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <a href="https://www.instagram.com/p_awan__kumar/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="40" style="margin-right: 10px;">
        </a>
        <a href="https://www.linkedin.com/in/pawan941394/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="40" style="margin-right: 10px;">
        </a>
        <a href="https://www.youtube.com/channel/UClgbj0iYh5mqY_81CMCw25Q/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="40" style="margin-right: 10px;">
        </a>
        <a href="https://github.com/pawan941394" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="40" style="margin-right: 10px;">
        </a>
   <a href="https://wa.me/919057714590" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="40" style="margin-right: 10px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
    
