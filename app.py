import streamlit as st

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])


# --------- RECIPE GENERATOR FUNCTION ---------

def ai_recipe(items, lang):

    veg = items.lower()

    if lang == "English":

        return f"""
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

    else:

        return f"""
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
2
