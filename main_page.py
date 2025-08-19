# # # import streamlit as st
# # # import pandas as pd
# # # st.title("Menu")
# # # # st.write(
# # # #     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# # # # )
# # # st.subheader("Menu/Recipe Mapping")
# # # df= pd.DataFrame({
# # #     'Days':["Monday","Tuesday","Wednesday","Thursday","Friday"],
# # #     'Time':["Breakfast","Lunch","Dinner"],
# # #     'Dishes':[],
# # #     'Ingredients':[]
# # # })
# # # st.dataframe(df)


# # import streamlit as st
# # import pandas as pd
# # from itertools import product

# # st.subheader("Menu/Recipe Mapping")

# # days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
# # times = ["Breakfast","Lunch","Dinner"]

# # rows = [
# #     {"Day": d, "Time": t, "Dish": None, "Ingredients": []}
# #     for d, t in product(days, times)   # 5*3 = 15 rows
# # ]

# # df = pd.DataFrame(rows)
# # st.dataframe(df, use_container_width=True)


# import streamlit as st
# import pandas as pd
# from itertools import product

# st.subheader("Menu/Recipe Mapping")
# st.button("Add/Edit Menu")

# days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
# times = ["Breakfast","Lunch","Dinner"]

# # ---- Sample recipe catalog ----
# recipes = {
#     "Poha": ["Poha (rice flakes)","Peanuts","Onion","Mustard","Oil","Salt"],
#     "Idli": ["Rice","Urad dal","Salt"],
#     "Upma": ["Rava (semolina)","Onion","Mustard","Curry leaves","Oil","Salt"],
#     "Veg Pulao": ["Rice","Mixed veg","Whole spices","Oil","Salt"],
#     "Rajma Chawal": ["Rajma","Rice","Onion","Tomato","Spices","Oil","Salt"],
#     "Dal Tadka": ["Toor dal","Ghee","Cumin","Garlic","Chili","Salt"],
#     "Paneer Butter Masala": ["Paneer","Butter","Cream","Tomato","Spices","Salt"],
#     "Chole": ["Chickpeas","Onion","Tomato","Spices","Oil","Salt"],
#     "Veg Biryani": ["Basmati rice","Mixed veg","Spices","Oil","Salt"],
#     "Khichdi": ["Rice","Moong dal","Ghee","Turmeric","Salt"],
#     "Aloo Paratha": ["Wheat flour","Potato","Oil","Spices","Salt"],
#     "Sambar Rice": ["Rice","Toor dal","Sambar powder","Tamarind","Veggies","Oil","Salt"],
# }

# # ---- Sample weekly plan (Day, Time) -> Dish ----
# menu_plan = {
#     ("Monday","Breakfast"): "Poha",
#     ("Monday","Lunch"): "Veg Pulao",
#     ("Monday","Dinner"): "Paneer Butter Masala",

#     ("Tuesday","Breakfast"): "Idli",
#     ("Tuesday","Lunch"): "Rajma Chawal",
#     ("Tuesday","Dinner"): "Chole",

#     ("Wednesday","Breakfast"): "Upma",
#     ("Wednesday","Lunch"): "Dal Tadka",
#     ("Wednesday","Dinner"): "Veg Biryani",

#     ("Thursday","Breakfast"): "Aloo Paratha",
#     ("Thursday","Lunch"): "Sambar Rice",
#     ("Thursday","Dinner"): "Paneer Butter Masala",

#     ("Friday","Breakfast"): "Poha",
#     ("Friday","Lunch"): "Veg Pulao",
#     ("Friday","Dinner"): "Khichdi",
# }

# # ---- Build rows with sample data ----
# rows = []
# for d, t in product(days, times):
#     dish = menu_plan.get((d, t))
#     ingredients = recipes.get(dish, []) if dish else []
#     rows.append({"Day": d, "Time": t, "Dish": dish, "Ingredients": ingredients})

# df = pd.DataFrame(rows)
# st.dataframe(df, use_container_width=True)


import streamlit as st
import pandas as pd
from itertools import product

st.set_page_config(page_title="Menu / Recipe Mapping", layout="wide")
st.subheader("Menu/Recipe Mapping")

# ---------------------------
# Data (catalog)
# ---------------------------
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
times = ["Breakfast","Lunch","Dinner"]

recipes = {
    "Poha": ["Poha (rice flakes)","Peanuts","Onion","Mustard","Oil","Salt"],
    "Idli": ["Rice","Urad dal","Salt"],
    "Upma": ["Rava (semolina)","Onion","Mustard","Curry leaves","Oil","Salt"],
    "Veg Pulao": ["Rice","Mixed veg","Whole spices","Oil","Salt"],
    "Rajma Chawal": ["Rajma","Rice","Onion","Tomato","Spices","Oil","Salt"],
    "Dal Tadka": ["Toor dal","Ghee","Cumin","Garlic","Chili","Salt"],
    "Paneer Butter Masala": ["Paneer","Butter","Cream","Tomato","Spices","Salt"],
    "Chole": ["Chickpeas","Onion","Tomato","Spices","Oil","Salt"],
    "Veg Biryani": ["Basmati rice","Mixed veg","Spices","Oil","Salt"],
    "Khichdi": ["Rice","Moong dal","Ghee","Turmeric","Salt"],
    "Aloo Paratha": ["Wheat flour","Potato","Oil","Spices","Salt"],
    "Sambar Rice": ["Rice","Toor dal","Sambar powder","Tamarind","Veggies","Oil","Salt"],
}

# ---------------------------
# Session state setup
# ---------------------------
if "menu_plan" not in st.session_state:
    st.session_state.menu_plan = {
        ("Monday","Breakfast"): "Poha",
        ("Monday","Lunch"): "Veg Pulao",
        ("Monday","Dinner"): "Paneer Butter Masala",

        ("Tuesday","Breakfast"): "Idli",
        ("Tuesday","Lunch"): "Rajma Chawal",
        ("Tuesday","Dinner"): "Chole",

        ("Wednesday","Breakfast"): "Upma",
        ("Wednesday","Lunch"): "Dal Tadka",
        ("Wednesday","Dinner"): "Veg Biryani",

        ("Thursday","Breakfast"): "Aloo Paratha",
        ("Thursday","Lunch"): "Sambar Rice",
        ("Thursday","Dinner"): "Paneer Butter Masala",

        ("Friday","Breakfast"): "Poha",
        ("Friday","Lunch"): "Veg Pulao",
        ("Friday","Dinner"): "Khichdi",
    }

if "show_form" not in st.session_state:
    st.session_state.show_form = False

def open_form():
    st.session_state.show_form = True

def close_form():
    st.session_state.show_form = False
    st.rerun()

# ---------------------------
# Actions row
# ---------------------------
c1, c2, c3 = st.columns([1,1,6])
c1.button("➕ Add / Edit Menu", on_click=open_form)
if c2.button("🧹 Clear Week"):
    st.session_state.menu_plan = {}
    st.success("Cleared all menu slots.")
    st.rerun()

# ---------------------------
# Conditional form drawer
# ---------------------------
if st.session_state.show_form:
    with st.form("add_edit_menu_form", clear_on_submit=False):
        st.markdown("### Add or Edit a Menu Slot")

        col1, col2 = st.columns(2)
        day  = col1.selectbox("Day", days, index=0, key="form_day")
        time = col2.selectbox("Time", times, index=0, key="form_time")

        # You can preselect the current dish if exists for this slot
        current_dish = st.session_state.menu_plan.get((day, time))
        dish_options = ["— none —"] + sorted(recipes.keys())
        default_idx = dish_options.index(current_dish) if current_dish in dish_options else 0

        dish = st.selectbox("Dish", dish_options, index=default_idx, key="form_dish")

        # Show ingredients preview
        chosen = None if dish == "— none —" else dish
        ings = recipes.get(chosen, [])
        st.caption("Ingredients preview")
        st.write(", ".join(ings) if ings else "—")

        colA, colB = st.columns(2)
        save = colA.form_submit_button("💾 Save")
        cancel = colB.form_submit_button("Cancel")

        if save:
            if chosen:
                st.session_state.menu_plan[(day, time)] = chosen
                st.success(f"Saved: {day} {time} → {chosen}")
            else:
                # Clear this slot if 'none'
                st.session_state.menu_plan.pop((day, time), None)
                st.info(f"Cleared: {day} {time}")
            close_form()

        if cancel:
            close_form()

# ---------------------------
# Build the table from state
# ---------------------------
rows = []
for d, t in product(days, times):
    dish = st.session_state.menu_plan.get((d, t))
    ingredients = recipes.get(dish, []) if dish else []
    rows.append({"Day": d, "Time": t, "Dish": dish, "Ingredients": ingredients})

df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)
