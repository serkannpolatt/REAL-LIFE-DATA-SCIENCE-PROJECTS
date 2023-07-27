import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

import matplotlib.pyplot as plt
import pandas_bokeh
import missingno

def create_correlation_chart(corr_df): ## Create Correlation Chart using Matplotlib
    fig = plt.figure(figsize=(15,15))
    plt.imshow(corr_df.values, cmap="Blues")
    plt.xticks(range(corr_df.shape[0]), corr_df.columns, rotation=90, fontsize=15)
    plt.yticks(range(corr_df.shape[0]), corr_df.columns, fontsize=15)
    plt.colorbar()

    for i in range(corr_df.shape[0]):
        for j in range(corr_df.shape[0]):
            plt.text(i,j, "{:.2f}".format(corr_df.values[i, j]), color="red", ha="center", fontsize=14, fontweight="bold")

    return fig

def create_missing_values_bar(df):
    missing_fig = plt.figure(figsize=(10,5))
    ax = missing_fig.add_subplot(111)
    missingno.bar(df, figsize=(10,5), fontsize=12, ax=ax)

    return missing_fig

def find_cat_cont_columns(df): ## Logic to Separate Continuous & Categorical Columns
    cont_columns, cat_columns = [],[]
    for col in df.columns:        
        if len(df[col].unique()) <= 25 or df[col].dtype == np.object_: ## If less than 25 unique values
            cat_columns.append(col.strip())
        else:
            cont_columns.append(col.strip())
    return cont_columns, cat_columns

st.set_page_config(page_icon=":bar_chart:", page_title="EDA Automated using Python")

st.title("Automate EDA")
st.caption("Upload CSV file to see various Charts related to EDA. Please upload a file that has both continuous columns and categorical columns.", unsafe_allow_html=True)
upload = st.file_uploader(label="Upload File Here:", type=["csv"])

if upload: ## File as Bytes
    df = pd.read_csv(upload)

    tab1, tab2, tab3 = st.tabs(["Dataset Overview :clipboard:", "Individual Column Stats :bar_chart:", "Explore Relation Between Features :chart:"])

    with tab1: ## Dataset Overview Tab        
        st.subheader("1. Dataset")
        st.write(df)

        cont_columns, cat_columns = find_cat_cont_columns(df)

        st.subheader("2. Dataset Overview")
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Rows", df.shape[0]), unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Duplicates", df.shape[0] - df.drop_duplicates().shape[0]), unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Features", df.shape[1]), unsafe_allow_html=True)
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Categorical Columns", len(cat_columns)), unsafe_allow_html=True)
        st.write(", ".join(cat_columns))
        st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Continuous Columns", len(cont_columns)), unsafe_allow_html=True)
        st.write(", ".join(cont_columns))
        
        corr_df = df[cont_columns].corr()
        corr_fig = create_correlation_chart(corr_df)
        
        st.subheader("3. Correlation Chart")
        st.pyplot(corr_fig, use_container_width=True)

        st.subheader("4. Missing Values Distribution")
        missing_fig = create_missing_values_bar(df)
        st.pyplot(missing_fig, use_container_width=True)

    with tab2: ## Individual Column Stats
        df_descr = df.describe()
        st.subheader("Analyze Individual Feature Distribution")

        st.markdown("#### 1. Understand Continuous Feature")        
        feature = st.selectbox(label="Select Continuous Feature", options=cont_columns, index=0)

        if feature:  # Check if feature is not None or empty
            na_cnt = df[feature].isna().sum()
            st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Count", df_descr[feature]['count']), unsafe_allow_html=True)
            st.markdown("<span style='font-weight:bold;'>{}</span> : {} / ({:.2f} %)".format("Missing Count", na_cnt, na_cnt/df.shape[0]), unsafe_allow_html=True)
            st.markdown("<span style='font-weight:bold;'>{}</span> : {:.2f}".format("Mean", df_descr[feature]['mean']), unsafe_allow_html=True)
            st.markdown("<span style='font-weight:bold;'>{}</span> : {:.2f}".format("Standard Deviation", df_descr[feature]['std']), unsafe_allow_html=True)
            st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Minimum", df_descr[feature]['min']), unsafe_allow_html=True)
            st.markdown("<span style='font-weight:bold;'>{}</span> : {}".format("Maximum", df_descr[feature]['max']), unsafe_allow_html=True)
            st.markdown("<span style='font-weight:bold;'>{}</span> :".format("Quantiles"), unsafe_allow_html=True)
            st.write(df_descr[[feature]].T[['25%', "50%", "75%"]])
            ## Histogram
            hist_fig = df.plot_bokeh.hist(y=feature, bins=50, legend=False, vertical_xlabel=True, show_figure=False)
            st.bokeh_chart(hist_fig, use_container_width=True)
        else:
            st.warning("Please select a continuous feature from the dropdown.")

        st.markdown("#### 2. Understand Categorical Feature")
        feature = st.selectbox(label="Select Categorical Feature", options=cat_columns, index=0)
        ### Categorical Columns Distribution        
        cnts = Counter(df[feature].values)
        df_cnts = pd.DataFrame({"Type": cnts.keys(), "Values": cnts.values()})
        bar_fig = df_cnts.plot_bokeh.bar(x="Type", y="Values", color="tomato", legend=False, show_figure=False)
        st.bokeh_chart(bar_fig, use_container_width=True)

    # ... (previous code)

    with tab3: ## Explore Relation Between Features
        st.subheader("Explore Relationship Between Features of Dataset")
        
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox(label="X-Axis", options=[None] + cont_columns, index=0)
        with col2:
            y_axis = st.selectbox(label="Y-Axis", options=[None] + cont_columns, index=0)  # Set default index to 0

        color_encode = st.selectbox(label="Color-Encode", options=[None,] + cat_columns)

        if x_axis and y_axis:  # Check if both x_axis and y_axis are not None
            scatter_fig = df.plot_bokeh.scatter(x=x_axis, y=y_axis, category=color_encode if color_encode else None, 
                                    title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()),
                                    figsize=(600,500), fontsize_title=20, fontsize_label=15,
                                    show_figure=False)
            st.bokeh_chart(scatter_fig, use_container_width=True)
        else:
            st.warning("Please select both X-Axis and Y-Axis columns from the dropdowns.")

    # ... (remaining code)

