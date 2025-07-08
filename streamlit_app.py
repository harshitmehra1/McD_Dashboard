import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- LOAD DATA ---
df = pd.read_csv("./data/Scored_mcd.csv")

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(
    page_title="McDonald's Health Score Tracker",
    layout="wide",
    page_icon="🍔"
)

st.title("🍔 McDonald's Menu Health Score Tracker")
st.markdown("""
This dashboard helps you explore how healthy each McDonald's menu category is, based on key nutrients like protein, fat, sugar, sodium, and fiber.

✅ Scoring scale: **0 to 100**  
🟢 **Healthy (Score > 70)**, 🟡 **Moderate (40–70)**, 🔴 **Unhealthy (< 40)**
""")

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Menu")
category_filter = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df['Category'].unique()),
    default=sorted(df['Category'].unique())
)

score_range = st.sidebar.slider("Health Score Range", 0, 100, (0, 100))

high_protein = st.sidebar.checkbox("High Protein (≥20g)")
low_sodium = st.sidebar.checkbox("Low Sodium (≤400mg)")

# --- FILTERING LOGIC ---
df_filtered = df[
    (df['Category'].isin(category_filter)) &
    (df['Health Score'] >= score_range[0]) &
    (df['Health Score'] <= score_range[1])
]

if high_protein:
    df_filtered = df_filtered[df_filtered['Protein'] >= 20]
if low_sodium:
    df_filtered = df_filtered[df_filtered['Sodium'] <= 400]

# --- RESET INDEX FOR DISPLAY ---
df_filtered = df_filtered.reset_index(drop=True)
df_filtered.index = df_filtered.index + 1

# --- SUMMARY KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("🍽️ Total Items", len(df_filtered))
col2.metric("📈 Avg Health Score", f"{df_filtered['Health Score'].mean():.2f}")
col3.metric("💪 High Protein Items", (df_filtered['Protein'] >= 20).sum())

# --- COLOR TAG FUNCTION ---
def get_score_tag(score):
    if score >= 70:
        return "🟢 Healthy"
    elif score >= 40:
        return "🟡 Moderate"
    else:
        return "🔴 Unhealthy"

df_filtered['Tag'] = df_filtered['Health Score'].apply(get_score_tag)

# --- TABLE VIEW ---
st.subheader("📋 Filtered Menu Items")
st.dataframe(
    df_filtered[['Item', 'Category', 'Calories', 'Protein', 'Sodium', 'Sugars', 'Health Score', 'Tag']]
        .sort_values(by='Health Score', ascending=False),
    use_container_width=True
)

# --- BAR CHART ---
st.subheader("🏆 Top Healthiest Items")
top_items = df_filtered.sort_values(by='Health Score', ascending=False).head(10)
fig = px.bar(
    top_items,
    x='Health Score',
    y='Item',
    color='Health Score',
    color_continuous_scale='Greens',
    orientation='h',
    title='Top Healthiest Items',
    height=500
)
st.plotly_chart(fig, use_container_width=True)



# --- CATEGORY NUTRIENT PROFILE VIEW ---
st.subheader("🍱 Nutrient Profile by Category")
category_selected = st.selectbox("Select a Category to Explore", sorted(df_filtered['Category'].unique()))

category_data = df_filtered[df_filtered['Category'] == category_selected]
category_avg = category_data[['Protein', 'Dietary Fiber', 'Saturated Fat', 'Sodium', 'Sugars', 'Calories']].mean()
category_avg['Sodium'] = category_avg['Sodium'] / 1000  # convert mg to grams

# Remove calories and prepare the rest
calories_avg = category_avg.pop('Calories')

nutrient_labels = ['Protein', 'Dietary Fiber', 'Saturated Fat', 'Sodium', 'Sugars']
nutrient_values = category_avg.values

nutrient_df = pd.DataFrame({
    'Nutrient': nutrient_labels,
    'Average': nutrient_values
})

# Define custom colors

color_map = {
    'Protein': '#ff4d6d',
    'Dietary Fiber': '#59cd90',
    'Saturated Fat': '#ffe066',
    'Sodium': '#5bc0eb',
    'Sugars': '#ffc2d1'
}
nutrient_df['Color'] = nutrient_df['Nutrient'].map(color_map)

# Layout with metric card for calories
col_chart, col_calories = st.columns([4, 1])

with col_chart:
    fig_category = px.bar(
        nutrient_df,
        x='Nutrient',
        y='Average',
        color='Nutrient',
        color_discrete_map=color_map,
        text_auto='.2s',
        title=f'Average Nutrients in "{category_selected}" Items',
        height=500
    )
    fig_category.update_layout(
        yaxis_title="Average per item (grams)",
        legend_title_text="",  # no legend title
    )
    st.plotly_chart(fig_category, use_container_width=True)

with col_calories:
    st.metric(label="🔥 Avg Calories (kcal)", value=f"{calories_avg:.1f}")



# --- FOOTER ---
st.markdown("""
---
👨‍💻 Built by Harshit Mehra | Powered by Python + Streamlit + Plotly
""")
