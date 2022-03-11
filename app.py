# Core Pkgs
import streamlit as st

# Additional Pkgs
import pandas as pd

# Fxns

def main():
    """All your code goes here"""

    # Display Data
    df = pd.read_csv("iris.csv")

    # Method 1
    #st.dataframe(df)

    # Adding a color style from pandas
    st.dataframe(df.style.highlight_max(axis=0))

    # Method 2 
    #st.table(df)

    # Method 3 
    st.write(df.head())

    # Display JSON Data
    st.json({'data': 'name'})

    # Display Code
    mycode = """
    def helloStreamlit():
    print("Hello Streamlit!!!")
    """
    st.code(mycode)


if __name__ == '__main__':
    main()
