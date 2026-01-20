import streamlit as st
import requests
import json

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])

# ----- AI FUNCTION -----

def ai_recipe(items, lang):

    if lang == "English":
        prompt = f"""
        You are a friendly Telugu home mother.
        Create a pure vegetarian recipe using: {items}

        Give in this format:
        Dish Name:
        Ingredients with quantities:
        Cooking Steps:
        Time required:
        Amma Tip:
        """
    else:
        prompt = f"""
        మీరు ప్రేమగా వంట చెప్పే తెలుగు అమ్మలా మాట్లాడండి.
        ఈ పదార్థాలతో వెజ్ వంటకం ఇవ్వండి: {items}

        ఈ ఫార్మాట్‌లో ఇవ్వండి:
        వంటకం పేరు:
        కావలసినవి (మోతాదులతో):
        తయారీ విధానం:
        పట్టే సమయం:
        అమ్మ చిట్కా:
        """

    # free model API
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

    payload = {"inputs": prompt}

    try:
        r = requests.post(API_URL, json=payload, timeout=20)
        result = r.json()
        return result[0]["generated_text"]
    except:
        return "AI busy గా ఉంది, మళ్లీ ప్రయత్నించండి 😊"


menu = st.sidebar.selectbox("Menu",
    ["Cook With Ingredients",
     "Priya Specials",
     "Healthy Tips"])

# ----- COOK SECTION -----

if menu == "Cook With Ingredients":

    items = st.text_area("Ingredients / పదార్థాలు")

    if st.button("Suggest Recipe"):

        with st.spinner("Cooking for you... 👩‍🍳"):
            output = ai_recipe(items, lang)
            st.write(output)

# ----- PRIYA SPECIALS -----

elif menu == "Priya Specials":

    st.subheader("Priya Specials 💖")

    st.write("""
• Gulab Jamun Ice Cream  
• Veg Biryani  
• Methi Chaman  
• Mango Dal  
• Coconut Pickle  
""")

# ----- HEALTH -----

elif menu == "Healthy Tips":

    st.write("""
• ఎక్కువ నూనె వద్దు  
• రోజూ ఒక ఆకు కూర  
• ఇంటి భోజనం బెస్ట్ 💚  
• నీళ్లు ఎక్కువ తాగండి  
""")
