# Core Pkgs
import streamlit as st

# Additional Pkgs

# Fxns

def main():
    """All your code goes here"""
    st.title("Hello, There!!")
    st.header("This is a header")
    st.subheader("This is a subheader")

    st.markdown("### This is markdown")

    #Displaying colored Text/Bootstrap Alerts
    st.success("Hoorray!")
    st.warning("Holly Moly!")
    st.info("Today is the day!")
    st.error("Oooops something was wrong!")
    st.exception("What happen!")

    #Superfunction
    def addSum(a, b):
        return a + b
    st.write("Normal Text")
    st.write("## Whaaat this is so cool is markdown!!")
    st.write(addSum(1, 2))

    st.write(dir(st))

    # Help Info
    st.help(range)

    




if __name__ == '__main__':
    main()
