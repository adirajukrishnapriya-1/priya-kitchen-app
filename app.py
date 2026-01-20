import streamlit as st

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])


# --------- RECIPE GENERATOR FUNCTION ---------

def ai_recipe(items, lang):

    veg = items.lower()

    if lang == "English":

        text = f"""
Dish Name: Home Style {veg.title()} Curry

Ingredients:
- {veg}
- 1 onion  
- 1 tomato  
- 1 tsp salt  
- 1 tsp chilli powder  
- 1/2 tsp turmeric  
- 2 spoons oil  

Cooking Steps:
1. Heat oil in a pan  
2. Add chopped onions & tomatoes  
3. Add salt, chilli, turmeric  
4. Add {veg}  
5. Cook for 10-12 minutes  
6. Add coriander leaves  

Time required: 15 minutes

Amma Tip:
Cook on medium flame and sprinkle little water for softness 💚
"""
        return text

    else:

        text = f"""
వంటకం పేరు: ఇంటి స్టైల్ {veg} కర్రీ

కావలసినవి:
- {veg}  
- 1 ఉల్లిపాయ  
- 1 టమాటా  
- 1 స్పూన్ ఉప్పు  
- 1 స్పూన్ కారం  
- 1/2 స్పూన్ పసుపు  
- 2 స్పూన్లు నూనె  

తయారీ విధానం:
1. కడాయిలో నూనె వేడి చేయండి  
2. ఉల్లి టమాటా వేయండి  
3. ఉప్పు, కారం, పసుపు వేయండి  
4. {veg} కలపండి  
5. 10-12 నిమిషాలు ఉడికించండి  
6. చివరగా కొత్తిమీర వేసండి  

పట్టే సమయం: 15 నిమిషాలు

అమ్మ చిట్కా:
మధ్య మంటపై వండితే రుచి బాగా వస్తుంది 💚
"""
        return text


# --------- APP MENU ---------

menu = st.sidebar.selectbox(
    "Menu",
    ["Cook With Ingredients",
     "Priya Specials",
     "Healthy Tips"]
)

# --------- COOK SECTION ---------

if menu == "Cook With Ingredients":

    items = st.text_area("Ingredients / పదార్థాలు")

    if st.button("Suggest Recipe"):

        if items.strip() == "":
            st.write("Please enter ingredients 😊")
        else:
            output = ai_recipe(items, lang)
            st.write(output)


# --------- PRIYA SPECIALS ---------

elif menu == "Priya Specials":

    st.subheader("Priya Specials 💖")

    st.write("""
• Gulab Jamun Ice Cream  
• Veg Biryani  
• Methi Chaman  
• Mango Dal  
• Coconut Pickle  
""")


# --------- HEALTH TIPS ---------

elif menu == "Healthy Tips":

    st.write("""
• ఎక్కువ నూనె వద్దు  
• రోజూ ఒక ఆకు కూర తినండి  
• ఇంటి భోజనం ఆరోగ్యం 💚  
• నీళ్లు ఎక్కువగా తాగండి  
""")
