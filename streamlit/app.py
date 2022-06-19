import streamlit as st
import preprocessing, functions
import matplotlib.pyplot as plt

st.sidebar.title("Chat Analyser" )

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data= bytes_data.decode("utf-8")
    df = preprocessing.preprocess(data)

    assert isinstance(df, object)
    st.dataframe(df)

    # List of users
    users_coll= df['user'].unique().tolist()
    users_coll.remove('group_notification')
    users_coll.sort()
    users_coll.insert(0,"Complete Group Analysis")

    selected_user = st.sidebar.selectbox("Analysis of which User ? ",users_coll)

    if st.sidebar.button("Analysis Start"):

        messages_count, words, links= functions.fetch_stats(selected_user,df)
        col1 , col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(messages_count)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Total Links")
            st.title(links)


    if selected_user=='Complete Group Analysis':
        st.title('Most Active Users')
        x ,df_active= functions.most_active(df)
        fig,ax = plt.subplots()


        col1, col2 = st.columns(2)

        with col1:
            ax.bar(x.index, x.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.dataframe(df_active)
