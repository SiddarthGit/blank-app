import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Stock Manager",
    page_icon="🛒",
    layout="centered"
)

# --- Page Title ---
st.title("🛒 Stock")
st.markdown("Add, view, and manage your stock items in real-time.")

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

# --- Add New Stock Section ---
st.header("Add New Stock Item")

with st.form("new_stock_form", clear_on_submit=True):
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        new_stock_name = st.text_input("Stock Name", placeholder="e.g., Tomato")
    with col2:
        # Ask for the unit beforehand
        new_stock_unit = st.radio("Unit", ["Numbers", "Kgs"], horizontal=True)

    submitted = st.form_submit_button("➕ Add Stock")

    if submitted and new_stock_name:
        if any(stock['name'].lower() == new_stock_name.lower() for stock in st.session_state.stocks):
            st.warning(f"Stock '{new_stock_name}' already exists.")
        else:
            # Add the new stock with its specified unit
            st.session_state.stocks.append({
                "name": new_stock_name,
                "unit": new_stock_unit,
                "quantity": 0 # Default quantity is 0
            })
            st.success(f"Added '{new_stock_name}' to your stock list!")

st.markdown("---")

# --- Display Current Stock List ---
st.header("Current Stock")

if not st.session_state.stocks:
    st.info("Your stock list is empty. Add an item above to get started!")
else:
    for i in range(len(st.session_state.stocks)):
        stock = st.session_state.stocks[i]
        
        # Create columns for layout: [Delete Icon, Name/Unit, Quantity Input]
        col1, col2, col3 = st.columns([0.15, 0.6, 0.25])

        # Column 1: Delete Button
        with col1:
            st.button("🗑️", key=f"delete_{i}", on_click=delete_stock, args=(i,))

        # Column 2: Stock Name and its unit
        with col2:
            st.markdown(f"#### {stock['name']}")
            st.caption(f"Unit: {stock['unit']}")

        # Column 3: Quantity Input (handles int or float based on unit)
        with col3:
            if stock["unit"] == "Numbers":
                # Input for Integers
                quantity = st.number_input(
                    "Quantity",
                    min_value=0,
                    step=1,
                    value=int(stock["quantity"]),
                    key=f"quantity_{i}",
                    label_visibility="collapsed",
                    format="%d" # Ensures input is treated as an integer
                )
            else: # For "Kgs"
                # Input for Floats
                quantity = st.number_input(
                    "Quantity",
                    min_value=0.0,
                    step=0.1,
                    value=float(stock["quantity"]),
                    key=f"quantity_{i}",
                    label_visibility="collapsed"
                )
            # Update the quantity in the session state
            st.session_state.stocks[i]['quantity'] = quantity
            
    st.markdown("---")
