import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Priya Kitchen – Telugu Ruchulu",
    layout="centered"
)

# ---------------- LOGO & BRAND ----------------
st.markdown(
    """
    <h1 style='text-align: center;'>🍛 PRIYA KITCHEN</h1>
    <h4 style='text-align: center; color: green;'>Telugu Ruchulu</h4>
    <p style='text-align: center;'>Amma style cooking, made smart 💚</p>
    <hr>
    """,
    unsafe_allow_html=True
)

st.write("మన ఇంటి రుచులు – మీ దగ్గర ఉన్న పదార్థాలతో వంట!")

# ---------------- USER OPTIONS ----------------
lang = st.selectbox("Language / భాష", ["English", "Telugu"])

dish_type = st.selectbox(
    "What do you want to cook? / ఏ వంట చేయాలనుకుంటున్నారు?",
    ["Curry", "Veg Biryani", "Rice Item", "Quick Fry"]
)

# ---------------- CORE LOGIC ----------------
def generate_recipe(items, dish_type, lang):
    items_lower = items.lower()

    # -------- VEG ONLY CHECK --------
    non_veg = ["egg", "chicken", "fish", "mutton"]
    for nv in non_veg:
        if nv in items_lower:
            return (
                "Priya Kitchen supports only PURE VEG recipes 🌱\n\n"
                "Please remove non-veg ingredients and try again 😊"
                if lang == "English"
                else
                "Priya Kitchen లో కేవలం వెజ్ వంటలే ఉంటాయి 🌱\n\n"
                "నాన్ వెజ్ పదార్థాలు తీసేసి మళ్లీ ప్రయత్నించండి 😊"
            )

    # -------- CURRY NAME DETECTION --------
    if dish_type == "Curry":

        if "potato" in items_lower:
            if "tomato" in items_lower:
                dish = "Aloo Tomato Curry"
            elif "peas" in items_lower:
                dish = "Aloo Peas Curry"
            else:
                dish = "Aloo Curry"

        elif "capsicum" in items_lower:
            dish = "Capsicum Curry"

        elif "tomato" in items_lower:
            dish = "Tomato Curry"

        elif any(v in items_lower for v in ["carrot", "beans", "peas"]):
            dish = "Mixed Vegetable Curry"

        else:
            dish = "Simple Veg Curry"

        if lang == "English":
            return (
                f"Dish: {dish}\n\n"
                "Why this curry:\n"
                f"Based on the ingredients you entered ({items}), this curry suits best for home-style cooking.\n\n"
                "Ingredients used:\n"
                f"- {items}\n"
                "- Oil, salt, chilli powder, turmeric\n\n"
                "Step-by-step method:\n"
                "1. Heat 2 spoons oil in a pan\n"
                "2. Add chopped onions and sauté till soft\n"
                "3. Add ginger & garlic and fry till raw smell goes\n"
                "4. Add tomatoes and cook till soft\n"
                "5. Add turmeric, chilli powder and salt\n"
                "6. Add main vegetables and mix well\n"
                "7. Add 1/2 cup water and cover with lid\n"
                "8. Cook on medium flame till vegetables are soft\n"
                "9. Open lid and cook 2 more minutes\n\n"
                "Cooking Time:\n"
                "20 minutes\n\n"
                "Amma Tip:\n"
                "Slow cooking brings the best taste 💚"
            )
        else:
            return (
                f"వంటకం: {dish}\n\n"
                "ఈ కర్రీ ఎందుకు:\n"
                f"మీరు ఇచ్చిన పదార్థాల ఆధారంగా ({items}) ఈ కర్రీ ఇంటి స్టైల్‌కి బాగా సరిపోతుంది.\n\n"
                "వాడిన పదార్థాలు:\n"
                f"- {items}\n"
                "- నూనె, ఉప్పు, కారం, పసుపు\n\n"
                "తయారీ విధానం:\n"
                "1. కడాయిలో 2 స్పూన్లు నూనె వేడి చేయండి\n"
                "2. ఉల్లి వేసి మెత్తగా అయ్యే వరకు వేయించండి\n"
                "3. అల్లం, వెల్లుల్లి వేసి వాసన పోయే వరకు వేయండి\n"
                "4. టమాటా వేసి మెత్తగా అయ్యే వరకు వండండి\n"
                "5. పసుపు, కారం, ఉప్పు వేయండి\n"
                "6. కూరగాయలు వేసి బాగా కలపండి\n"
                "7. అర కప్పు నీరు వేసి మూత పెట్టండి\n"
                "8. మధ్య మంటపై మగ్గే వరకు ఉడికించండి\n"
                "9. చివరగా మూత తీసి 2 నిమిషాలు మరిగించండి\n\n"
                "పట్టే సమయం:\n"
                "20 నిమిషాలు\n\n"
                "అమ్మ చిట్కా:\n"
                "నెమ్మదిగా వండితే కర్రీ రుచి బాగా వస్తుంది 💚"
            )

    # -------- OTHER DISH TYPES (SIMPLE BUT CLEAR) --------
    if dish_type == "Veg Biryani":
        return (
            "Veg Biryani will be prepared using rice, vegetables and biryani masala.\n\n"
            "Detailed biryani logic will be added next step 🍛"
        )

    if dish_type == "Rice Item":
        return (
            "Rice items like lemon rice, tomato rice or curd rice suit these ingredients.\n\n"
            "Detailed rice logic coming next 🍚"
        )

    return (
        "Quick fry works best with minimum oil and high flame.\n\n"
        "Detailed fry logic coming next 🍳"
    )


# ---------------- UI ----------------
menu = st.sidebar.selectbox("Menu", ["Cook With Ingredients", "Priya Specials"])

if menu == "Cook With Ingredients":
    items = st.text_area("Ingredients / పదార్థాలు")

    if st.button("Suggest Recipe"):
        if items.strip():
            st.write(generate_recipe(items, dish_type, lang))
        else:
            st.warning("Please enter ingredients 😊")

elif menu == "Priya Specials":
    st.subheader("💖 Priya Specials")
    st.write(
        "• Gulab Jamun Ice Cream\n"
        "• Veg Biryani\n"
        "• Methi Chaman\n"
        "• Mango Dal\n"
        "• Coconut Pickle"
    )
