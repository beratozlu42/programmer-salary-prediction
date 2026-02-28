import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

def clean_age(x):
    if x > 60:
        return 60
    if x < 18:
        return 18
    return x

@st.cache_resource
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "Age", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df[df["Age"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] > 10000]
    df = df[df["Country"] != 'Other']

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    df['Age'] = df['Age'].apply(clean_age)

    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
        ### Stack Overflow Developer Survey (2020)
    """
    )

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()

    wedges, texts, autotexts = ax1.pie(
        data,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90
    )

    ax1.axis("equal")

    ax1.legend(
        wedges,
        data.index,
        title="Countries",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    st.write("""#### Number of data from different countries""")

    st.pyplot(fig1)

    st.write(
        """
        #### Mean Salary Based on Country
        """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data) 

    st.write(
        """
        #### Mean Salary Based on Experience
        """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.write(
        """
        #### Mean Salary Based on Age
        """
    )

    data = df.groupby(["Age"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)