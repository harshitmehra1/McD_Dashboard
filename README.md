# 🍔 McDonald's Health Score Tracker 🍟

An interactive, visually rich dashboard to explore and compare the **nutritional health** of McDonald's menu items using a simple, transparent **Health Score system**.

Built using **Python**, **Streamlit**, and **Plotly**, this app empowers users to make smarter food choices based on actual nutrient data — without sacrificing clarity or design.
&nbsp;

## 🚀 Features

### 🧮 Nutritional Scoring System
Each menu item receives a **Health Score (0–100)** based on:
- 🥩 Protein
- 🧈 Saturated Fat
- 🍭 Sugars
- 🧂 Sodium
- 🌿 Dietary Fiber

🔢 **Scoring scale:**
- 🟢 **Healthy** → Score > 70  
- 🟡 **Moderate** → Score 40–70  
- 🔴 **Unhealthy** → Score < 40
&nbsp;

---

### 🧾 Filtered Menu Table
- Full list of items with nutritional values.
- Real-time filtering by:
  - 🍳 **Category** (Breakfast, Beverages, etc.)
  - 📊 **Health Score range**
  - 💪 **High Protein (≥ 20g)**
  - 🧂 **Low Sodium (≤ 400mg)**
- Items are dynamically re-indexed for clarity.
&nbsp;

---

### 🏅 Top Healthiest Items
- Displays a **horizontal bar chart** of the **Top 10 healthiest items** based on calculated scores.

&nbsp;

---


### 📊 Category Nutrient Explorer
- Select a category (e.g., Beverages, Burgers)
- View **average values of nutrients** like Protein, Sugar, Sodium, etc.
- 🌈 **Color-coded bar chart** with clear units
- 📌 Average **calorie count** shown as a side badge

&nbsp;

## 🛠️ Tech Stack

- **🐍 Python 3.11+**
- **🧩 Streamlit** – for building the interactive dashboard
- **📈 Plotly – vibrant**, responsive charts
- **🧮 Pandas & NumPy** – for data processing and analysis

&nbsp;

## 🌐 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/harshitmehra1/McD_Dashboard.git
    cd McD_Dashboard
    ```


## ⚙ Install Dependencies

1.  **Install required packages**
    ```bash
    pip install -r requirements.txt
    ```


## 🚀 Launch the App

1.  **Run the Streamlit application**
    ```bash
    streamlit run streamlit_app.py
    ```


## 👨‍🍳 Made By

**Harshit Mehra**   
🎓 Data Scientist   |   📊 Visual Thinker   |   🍔 Food Enthusiast  
📧 harshitmehra122@gmail.com



## ❤️ Why This App?

This dashboard aims to:

* Help everyday users quickly compare fast food options.
* Offer simple visuals and filters for better health awareness.
* Showcase how data science + design can improve lifestyle decisions.

