import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Stock Manager",
    page_icon="🛒",
    layout="centered"
)

# --- Page Title ---
st.title("🛒 Stock Management")

# --- Initialize Session State ---
if 'stocks' not in st.session_state:
    # Initialize with example data
    st.session_state.stocks = [
        {"name": "Roti", "unit": "Numbers", "quantity": 50},
        {"name": "Onion", "unit": "Kgs", "quantity": 5.5},
        {"name": "Turmeric Powder", "unit": "Kgs", "quantity": 0.5}
    ]

# --- Function to Delete a Stock Item ---
def delete_stock(index_to_delete):
    st.session_state.stocks.pop(index_to_delete)

# --- Add New Stock Section (inside a popover) ---
# The form is now hidden behind this button, keeping the UI clean.
with st.popover("➕ Add New Item"):
    st.markdown("#### Add a new item to your stock")
    with st.form("new_stock_form"):
        new_stock_name = st.text_input("Stock Name", placeholder="e.g., Tomato")
        new_stock_unit = st.radio("Unit", ["Numbers", "Kgs"], horizontal=True, label_visibility="collapsed")
        
        submitted = st.form_submit_button("✔️ Add Stock")

        if submitted and new_stock_name:
            if any(stock['name'].lower() == new_stock_name.lower() for stock in st.session_state.stocks):
                st.warning(f"Stock '{new_stock_name}' already exists.")
            else:
                st.session_state.stocks.append({
                    "name": new_stock_name,
                    "unit": new_stock_unit,
                    "quantity": 0
                })
                # A success message is not needed here as the popover will close
                # and the new item will appear in the list, providing visual feedback.

st.markdown("---")

# --- Display Current Stock List ---
# Using a smaller header for a more compact look.
st.subheader("Current Stock List")

if not st.session_state.stocks:
    st.info("Your stock list is empty. Add an item to get started!")
else:
    for i in range(len(st.session_state.stocks)):
        stock = st.session_state.stocks[i]
        
        col1, col2, col3 = st.columns([0.15, 0.6, 0.25])

        with col1:
            st.button("🗑️", key=f"delete_{i}", on_click=delete_stock, args=(i,))

        with col2:
            st.markdown(f"**{stock['name']}**")
            st.caption(f"Unit: {stock['unit']}")

        with col3:
            if stock["unit"] == "Numbers":
                quantity = st.number_input(
                    "Quantity", min_value=0, step=1, value=int(stock["quantity"]),
                    key=f"quantity_{i}", label_visibility="collapsed", format="%d"
                )
            else: # For "Kgs"
                quantity = st.number_input(
                    "Quantity", min_value=0.0, step=0.1, value=float(stock["quantity"]),
                    key=f"quantity_{i}", label_visibility="collapsed"
                )
            st.session_state.stocks[i]['quantity'] = quantity
