import streamlit as st

st.set_page_config(page_title="Priya Kitchen – Telugu Ruchulu")

st.title("🍛 Priya Kitchen – Telugu Ruchulu")
st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న వాటితో వంట!")

lang = st.selectbox("Language / భాష", ["English", "Telugu"])


# --------- SMART RECIPE GENERATOR ---------

def ai_recipe(items, lang):

    veg = items.lower()

    # ===== BIRYANI STYLE =====
    if "rice" in veg and ("briyani" in veg or "biryani" in veg or "spices" in veg):

        if lang == "English":
            return f"""
Dish Name: Simple Veg Biryani (Home Style)

Ingredients:
- 1 cup rice  
- {veg}  
- 2 onions sliced  
- 1 tomato  
- 2 tsp biryani masala  
- 1 tsp ginger garlic paste  
- 2 tbsp oil  
- salt as needed  
- coriander leaves  

Preparation Steps:
1. Wash rice and soak for 15 minutes  
2. Heat oil and fry onions till golden  
3. Add tomato + ginger garlic  
4. Add vegetables and biryani masala  
5. Add rice with 2 cups water  
6. Cover and cook on low flame 15 minutes  

Time required: 25 minutes

Amma Tip:
Add one spoon ghee on top for nice biryani aroma 💚
"""

        else:
            return f"""
వంటకం పేరు: సింపుల్ వెజ్ బిర్యానీ

కావలసినవి:
- 1 కప్పు బియ్యం  
- {veg}  
- 2 ఉల్లిపాయలు  
- 1 టమాటా  
- 2 స్పూన్లు బిర్యానీ మసాలా  
- 1 స్పూన్ అల్లం వెల్లుల్లి పేస్ట్  
- ఉప్పు  
- కొత్తిమీర  

తయారీ విధానం:
1. బియ్యం 15 నిమిషాలు నానబెట్టండి  
2. నూనెలో ఉల్లి బంగారు రంగు వచ్చే వరకు వేయించండి  
3. టమాటా + అల్లం వెల్లుల్లి వేయండి  
4. కూరగాయలు + బిర్యానీ మసాలా  
5. బియ్యం + 2 కప్పుల నీరు  
6. మూత పెట్టి 15 నిమిషాలు మగ్గించండి  

పట్టే సమయం: 25 నిమిషాలు

అమ్మ చిట్కా:
చివరగా ఒక స్పూన్ నెయ్యి వేస్తే వాసన సూపర్ 💚
"""

    # ===== NORMAL CURRY STYLE =====

    if lang == "English":

        return f"""
Dish Name: {veg.title()} Curry

Ingredients:
- {veg}
- 1 onion  
- 1 to
