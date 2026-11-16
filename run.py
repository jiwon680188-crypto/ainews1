import streamlit as st

urls=[
    'https://www.youtube.com/watch?v=KR8ddnPjCtk',
    'https://www.youtube.com/watch?v=Gv9_4yMHFhI',
    'https://www.youtube.com/watch?v=MP8R6kBykzE'

    ]
images=['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmhSNJGrrK7GNNwzYnikLsOrFAiKTX3xm06-UVMxCGwg&s=10']
st.title('This is my first webapp')
con1,con2 = st.columns((4,1))
with con1:
    with st.expander('Content...'):
        for i in range(len(urls)):
            st.video(urls[i])
        pass
with con2:
    with st.expander('Tips...'):
        st.image(images[0])
        pass


con3,con4 = st.columns((4,1))
with con3:
    with st.expander('Content...'):
       import pandas as pd
       df = pd.read_csv('./data.csv')
       st.write(df)
with con4:
    with st.expander('Tips...'):
        with open('./ml.txt','r', encoding='UTF-8') as f:
            mytxt = f.read()
            st.markdown(mytxt)
            
        st.image(images[0])

        pass