import streamlit as st
import pandas as pd
import math

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1146532466/photo/abstract-blue-digital-background.jpg?b=1&s=170667a&w=0&k=20&c=dSA5-nFFQ2szrdDxg8qHy67azMPkshnzPgtBgSsECkY=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
def main():

    add_bg_from_url()

    st.write('# FOR SALE COMPARISON')
    st.caption('by deto')
    st.text("""
            This app compare two csv files from the same profile,
            returning the records for sale difference.
            The files must be formatted in the same way.
            """)

    upload_file1 = st.file_uploader("UPLOAD OLDEST CSV:", type="csv")

    if upload_file1:
        df1 = pd.read_csv(upload_file1)
        df1 = df1.drop_duplicates(subset='url').reset_index(drop=True)
        st.dataframe(df1)

    upload_file2 = st.file_uploader("UPLOAD MOST RECENT CSV:", type="csv", key='file2')

    if upload_file2:
        df2 = pd.read_csv(upload_file2)
        df2 = df2.drop_duplicates(subset='url').reset_index(drop=True)
        st.dataframe(df2)

    if upload_file1 and upload_file2:
        st.markdown("## Analysis")
        result_raw = df2.merge(df1, on="url",suffixes=('_rec', '_old'))
        result = result_raw[['url', 'for_sale_rec','for_sale_old']]
        result['difference'] = result['for_sale_rec'] - result['for_sale_old']
        st.dataframe(result.sort_values(by=['difference']))

        st.markdown("### Substantial Difference")
        perc = st.number_input('Insert number for the percentage ( recent for sale / 100 * <percentage>)')
        st.dataframe(result[result['difference'].apply(lambda x: abs(x)) > ((result['for_sale_rec'])/100)*perc])
        



if __name__ == '__main__':
    main()
