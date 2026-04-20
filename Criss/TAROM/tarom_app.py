import streamlit as st
import pandas as pd
import plotly.express as px

# DARK MODE
st.set_page_config(
    page_title="Dashboard TAROM",
    layout="wide"
)

st.markdown("""
    <style>
    body {background-color: #0E1117; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title(" Dashboard TAROM - Analiza Zboruri")

# Citire CSV
df = pd.read_csv("tarom_data.csv")


# #  SIDEBAR (filtre)
# st.sidebar.header("Filtre")
#
# # Filtru destinații
# destinatii = st.sidebar.multiselect(
#     "Alege destinatii:",
#     df["Destinatie"].unique(),
#     default=df["Destinatie"].unique()
# )
#
# # Slider preț
# pret_min, pret_max = st.sidebar.slider(
#     "Interval pret (€):",
#     int(df["Pret Mediu (€)"].min()),
#     int(df["Pret Mediu (€)"].max()),
#     (int(df["Pret Mediu (€)"].min()), int(df["Pret Mediu (€)"].max()))
# )
#
# # Aplicare filtre
# df_filtered = df[
#     (df["Destinatie"].isin(destinatii)) &
#     (df["Pret Mediu (€)"] >= pret_min) &
#     (df["Pret Mediu (€)"] <= pret_max)
# ]
#
# #  Dacă nu există date
# if df_filtered.empty:
#     st.warning("Nu exista date pentru filtrele selectate!")
#     st.stop()
#
#
# # cards KPI
# col1, col2, col3 = st.columns(3)
#
# col1.metric("Total Pasageri", "590")
# col2.metric("Pret mediu", "204 €")
# col3.metric("Grad ocupare", "75%")
#
#
# #
# # LAYOUT PE COLOANE
# col1, col2 = st.columns(2)
#
#
# #  1. BAR CHART
# with col1:
#     st.subheader("Pasageri per destinatie")
#
#     df_sorted = df_filtered.sort_values(by="Pasageri", ascending=False)
#
#     fig_bar = px.bar(
#         df_sorted,
#         x="Destinatie",
#         y="Pasageri",
#         color="Pasageri",
#         text="Pasageri"
#     )
#
#     fig_bar.update_traces(textposition='inside')
#     st.plotly_chart(fig_bar, use_container_width=True)
#
#
# #  2. LINE + AREA
# with col2:
#     st.subheader("Pret mediu bilete")
#
#     fig_line = px.line(
#         df_filtered,
#         x="Destinatie",
#         y="Pret Mediu (€)",
#         markers=True
#     )
#
#     fig_line.add_scatter(
#         x=df_filtered["Destinatie"],
#         y=df_filtered["Pret Mediu (€)"],
#         fill='tozeroy'
#     )
#
#     st.plotly_chart(fig_line, use_container_width=True)
#
#
# #  3. DONUT
# col3, col4 = st.columns(2)
#
# with col3:
#     st.subheader("Grad ocupare")
#
#     fig_pie = px.pie(
#         df_filtered,
#         names="Destinatie",
#         values="Grad Ocupare (%)",
#         hole=0.4
#     )
#
#     fig_pie.update_traces(textinfo="percent+value")
#     st.plotly_chart(fig_pie, use_container_width=True)
#
#
# #  4. SCATTER
# with col4:
#     st.subheader("Pret vs Pasageri")
#
#     fig_scatter = px.scatter(
#         df_filtered,
#         x="Pret Mediu (€)",
#         y="Pasageri",
#         size="Pasageri",
#         color="Pret Mediu (€)",
#         hover_name="Destinatie",
#         size_max=60
#     )
#
#     st.plotly_chart(fig_scatter, use_container_width=True)
#
#
# #  TABEL DATE
# st.subheader("Date filtrate")
# st.dataframe(df_filtered)