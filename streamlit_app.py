import streamlit as st


#enabling multiple pages 
main_page = st.Page("main_page.py", title="Menu", icon="🎈")
page_2 = st.Page("baskets.py", title="Baskets", icon="❄️")
page_3 = st.Page("stocks.py", title="Stocks", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()