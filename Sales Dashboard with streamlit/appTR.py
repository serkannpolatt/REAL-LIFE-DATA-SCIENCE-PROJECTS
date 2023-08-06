import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- EXCEL'DEN VERİ OKUMA ----
@st.cache_data()
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- YAN PANEL ----
st.sidebar.header("Lütfen Buradan Filtreleyin:")
city = st.sidebar.multiselect(
    "Şehir Seçin:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Müşteri Türünü Seçin:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Cinsiyeti Seçin:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)

# ---- ANA SAYFA ----
st.title(":bar_chart: Satış Gösterge Paneli")
st.markdown("##")

# KPI'lar
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Toplam Satış:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Ortalama Değerlendirme:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Ortalama İşlem Başına Satış:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# ÜRÜN LİNE'INA GÖRE SATIŞLAR [BAR GRAFİĞİ]
@st.cache_resource()
def calculate_sales_by_product_line(df):
    sales_by_product_line = (
        df.groupby(by=["Product line"])["Total"].sum().sort_values()
    )
    return sales_by_product_line

sales_by_product_line = calculate_sales_by_product_line(df_selection)

fig_product_sales = px.bar(
    sales_by_product_line,
    x=sales_by_product_line.values,
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Ürün Linede Satışlar</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SAATE GÖRE SATIŞLAR [BAR GRAFİĞİ]
@st.cache_data()
def calculate_sales_by_hour(df):
    sales_by_hour = df.groupby(by=["hour"])["Total"].sum()
    return sales_by_hour

sales_by_hour = calculate_sales_by_hour(df_selection)

fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y=sales_by_hour.values,
    title="<b>Saate Göre Satışlar</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

# ---- STREAMLIT STİLİNİ GİZLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
