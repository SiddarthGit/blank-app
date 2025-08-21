import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Weekly Menu Planner", layout="wide", initial_sidebar_state="collapsed")
st.title("🍽️ Weekly Menu Planner")
st.markdown("Plan your meals, define recipes, and see your week at a glance.")

# --- Data & Session State Initialization ---
def initialize_data():
    # Hard-coded recipes with estimated per-person quantities
    if "recipes" not in st.session_state:
        st.session_state.recipes = {
            "Poha": {
                "Poha (rice flakes)": {"qty": 0.1, "unit": "kg"},
                "Peanuts": {"qty": 0.02, "unit": "kg"},
                "Onion": {"qty": 0.05, "unit": "kg"},
                "Mustard Seeds": {"qty": 0.005, "unit": "kg"},
                "Oil": {"qty": 0.01, "unit": "L"},
                "Salt": {"qty": 0.002, "unit": "kg"},
            },
            "Idli": {
                "Rice": {"qty": 0.1, "unit": "kg"},
                "Urad dal": {"qty": 0.04, "unit": "kg"},
                "Salt": {"qty": 0.002, "unit": "kg"},
            },
            "Upma": {
                "Rava (semolina)": {"qty": 0.1, "unit": "kg"},
                "Onion": {"qty": 0.05, "unit": "kg"},
                "Mustard Seeds": {"qty": 0.005, "unit": "kg"},
                "Curry leaves": {"qty": 0.005, "unit": "kg"},
                "Oil": {"qty": 0.01, "unit": "L"},
                "Salt": {"qty": 0.002, "unit": "kg"},
            },
            "Veg Pulao": {
                "Rice": {"qty": 0.15, "unit": "kg"},
                "Mixed veg": {"qty": 0.1, "unit": "kg"},
                "Whole spices": {"qty": 0.005, "unit": "kg"},
                "Oil": {"qty": 0.01, "unit": "L"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Rajma Chawal": {
                "Rajma": {"qty": 0.1, "unit": "kg"},
                "Rice": {"qty": 0.15, "unit": "kg"},
                "Onion": {"qty": 0.05, "unit": "kg"},
                "Tomato": {"qty": 0.05, "unit": "kg"},
                "Spices": {"qty": 0.01, "unit": "kg"},
                "Oil": {"qty": 0.01, "unit": "L"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Dal Tadka": {
                "Toor dal": {"qty": 0.1, "unit": "kg"},
                "Ghee": {"qty": 0.01, "unit": "kg"},
                "Cumin": {"qty": 0.005, "unit": "kg"},
                "Garlic": {"qty": 0.005, "unit": "kg"},
                "Chili": {"qty": 1, "unit": "pcs"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Paneer Butter Masala": {
                "Paneer": {"qty": 0.1, "unit": "kg"},
                "Butter": {"qty": 0.03, "unit": "kg"},
                "Cream": {"qty": 0.02, "unit": "L"},
                "Tomato": {"qty": 0.15, "unit": "kg"},
                "Spices": {"qty": 0.01, "unit": "kg"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Chole": {
                "Chickpeas": {"qty": 0.1, "unit": "kg"},
                "Onion": {"qty": 0.05, "unit": "kg"},
                "Tomato": {"qty": 0.1, "unit": "kg"},
                "Spices": {"qty": 0.01, "unit": "kg"},
                "Oil": {"qty": 0.01, "unit": "L"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Veg Biryani": {
                "Basmati rice": {"qty": 0.15, "unit": "kg"},
                "Mixed veg": {"qty": 0.1, "unit": "kg"},
                "Spices": {"qty": 0.015, "unit": "kg"},
                "Oil": {"qty": 0.015, "unit": "L"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Khichdi": {
                "Rice": {"qty": 0.1, "unit": "kg"},
                "Moong dal": {"qty": 0.05, "unit": "kg"},
                "Ghee": {"qty": 0.01, "unit": "kg"},
                "Turmeric": {"qty": 0.002, "unit": "kg"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Aloo Paratha": {
                "Wheat flour": {"qty": 0.15, "unit": "kg"},
                "Potato": {"qty": 0.1, "unit": "kg"},
                "Oil": {"qty": 0.015, "unit": "L"},
                "Spices": {"qty": 0.005, "unit": "kg"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
            "Sambar Rice": {
                "Rice": {"qty": 0.15, "unit": "kg"},
                "Toor dal": {"qty": 0.05, "unit": "kg"},
                "Sambar powder": {"qty": 0.015, "unit": "kg"},
                "Tamarind": {"qty": 0.01, "unit": "kg"},
                "Veggies": {"qty": 0.1, "unit": "kg"},
                "Oil": {"qty": 0.01, "unit": "L"},
                "Salt": {"qty": 0.003, "unit": "kg"},
            },
        }

    # Hard-coded weekly menu plan
    if "menu_plan" not in st.session_state:
        st.session_state.menu_plan = {
            ("Mon","Breakfast"): "Poha",
            ("Mon","Lunch"): "Veg Pulao",
            ("Mon","Dinner"): "Paneer Butter Masala",
            ("Tue","Breakfast"): "Idli",
            ("Tue","Lunch"): "Rajma Chawal",
            ("Tue","Dinner"): "Chole",
            ("Wed","Breakfast"): "Upma",
            ("Wed","Lunch"): "Dal Tadka",
            ("Wed","Dinner"): "Veg Biryani",
            ("Thur","Breakfast"): "Aloo Paratha",
            ("Thur","Lunch"): "Sambar Rice",
            ("Thur","Dinner"): "Paneer Butter Masala",
            ("Fri","Breakfast"): "Poha",
            ("Fri","Lunch"): "Veg Pulao",
            ("Fri","Dinner"): "Khichdi",
        }

    if "person_counts" not in st.session_state:
        st.session_state.person_counts = {}
    
    if "show_management_panel" not in st.session_state:
        st.session_state.show_management_panel = False

initialize_data()

# --- Main Actions ---
if st.button("✏️ Manage Menu & Recipes", use_container_width=True):
    st.session_state.show_management_panel = not st.session_state.show_management_panel

# --- Conditionally display the management panel ---
if st.session_state.show_management_panel:
    with st.container(border=True):
        tab1, tab2 = st.tabs(["🗓️ Set Menu Slot", "🍲 Manage Recipes"])

        # --- Tab 1: Set Menu Slot ---
        with tab1:
            with st.form("set_menu_form"):
                st.subheader("Assign a dish to a time slot")
                # Using full day names for the form
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                times = ["Breakfast", "Lunch", "Dinner"]
                
                col1, col2 = st.columns(2)
                day = col1.selectbox("Day", days)
                time = col2.selectbox("Time", times)
                
                dish_options = ["— Clear Slot —"] + sorted(st.session_state.recipes.keys())
                current_dish = st.session_state.menu_plan.get((day, time))
                default_idx = dish_options.index(current_dish) if current_dish in dish_options else 0
                
                dish = st.selectbox("Select Dish", dish_options, index=default_idx)

                submitted = st.form_submit_button("💾 Save Slot")
                if submitted:
                    if dish == "— Clear Slot —":
                        st.session_state.menu_plan.pop((day, time), None)
                    else:
                        st.session_state.menu_plan[(day, time)] = dish
                    
                    st.session_state.show_management_panel = False
                    st.rerun()

        # --- Tab 2: Manage Recipes ---
        with tab2:
            st.subheader("Add, Edit, or Delete a Recipe")
            recipe_to_edit = st.selectbox("Select a recipe", ["✨ Add New Recipe"] + sorted(st.session_state.recipes.keys()))

            if recipe_to_edit == "✨ Add New Recipe":
                ingredients_key = "new_recipe_ingredients"
            else:
                ingredients_key = f"edit_{recipe_to_edit}_ingredients"

            if ingredients_key not in st.session_state:
                 st.session_state[ingredients_key] = [{"name": "", "qty": 0.1, "unit": "kg"}] if recipe_to_edit == "✨ Add New Recipe" else [{"name": k, **v} for k, v in st.session_state.recipes[recipe_to_edit].items()]

            with st.form(f"{recipe_to_edit}_form"):
                new_name = st.text_input("Recipe Name", value=recipe_to_edit if recipe_to_edit != "✨ Add New Recipe" else "")
                st.markdown("**Ingredients (per person)**")

                for i, ing in enumerate(st.session_state[ingredients_key]):
                    c1, c2, c3 = st.columns([2, 1, 1])
                    st.session_state[ingredients_key][i]['name'] = c1.text_input("Ingredient", value=ing['name'], key=f"{ingredients_key}_{i}_name")
                    st.session_state[ingredients_key][i]['qty'] = c2.number_input("Qty", min_value=0.0, step=0.01, value=ing['qty'], key=f"{ingredients_key}_{i}_qty")
                    st.session_state[ingredients_key][i]['unit'] = c3.selectbox("Unit", ["kg", "g", "L", "ml", "pcs"], index=["kg", "g", "L", "ml", "pcs"].index(ing['unit']), key=f"{ingredients_key}_{i}_unit")

                c1,c2 = st.columns(2)
                if c1.form_submit_button("➕ Add Ingredient"):
                    st.session_state[ingredients_key].append({"name": "", "qty": 0.1, "unit": "kg"})
                    st.rerun()
                if c2.form_submit_button("➖ Remove Last") and len(st.session_state[ingredients_key]) > 1:
                    st.session_state[ingredients_key].pop()
                    st.rerun()
                
                st.markdown("---")
                save_btn, del_btn, cancel_btn = st.columns(3)
                if save_btn.form_submit_button("💾 Save Recipe", use_container_width=True):
                    if new_name:
                        recipe_data = {ing['name']: {'qty': ing['qty'], 'unit': ing['unit']} for ing in st.session_state[ingredients_key] if ing['name']}
                        st.session_state.recipes[new_name] = recipe_data
                        if recipe_to_edit != "✨ Add New Recipe" and recipe_to_edit != new_name:
                            del st.session_state.recipes[recipe_to_edit]
                        del st.session_state[ingredients_key]
                        st.rerun()
                
                if recipe_to_edit != "✨ Add New Recipe":
                    if del_btn.form_submit_button("🗑️ Delete", use_container_width=True):
                        del st.session_state.recipes[recipe_to_edit]
                        del st.session_state[ingredients_key]
                        st.rerun()

                if cancel_btn.form_submit_button("✖️ Close", use_container_width=True):
                    if ingredients_key in st.session_state:
                        del st.session_state[ingredients_key]
                    st.session_state.show_management_panel = False
                    st.rerun()

st.markdown("---")

# --- Weekly Timetable Display ---
st.header("📅 Weekly Menu Timetable")
# Using full day names for the display
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
meal_times = ["Breakfast", "Lunch", "Dinner"]

cols = st.columns(len(days_of_week) + 1)
cols[0].markdown("### Time")
for i, day in enumerate(days_of_week):
    cols[i+1].markdown(f"### {day}")

for time in meal_times:
    cols = st.columns(len(days_of_week) + 1)
    cols[0].markdown(f"**{time}**")
    for i, day in enumerate(days_of_week):
        slot_key = (day, time)
        dish = st.session_state.menu_plan.get(slot_key)
        if dish:
            with cols[i+1].container(border=True):
                st.markdown(f"**{dish}**")
                person_count = st.number_input(
                    "Persons", min_value=0, step=1,
                    value=st.session_state.person_counts.get(slot_key, 1),
                    key=f"persons_{day}_{time}", label_visibility="collapsed"
                )
                st.session_state.person_counts[slot_key] = person_count
        else:
            cols[i+1].markdown("—")