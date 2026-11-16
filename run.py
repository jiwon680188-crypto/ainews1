import streamlit as st

urls=[''
   

    ]
images=['https://thumbnail.10x10.co.kr/webimage/image/add1/291/A002910028_01.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false']
st.title('여러분, 안녕하세요 반갑습니다')
con1,con2 = st.columns((4,1))
with con1:
    with st.expander('Tips...'):
        with open('./ml.txt','r', encoding='UTF-8') as f:
            mytxt = f.read()
            st.markdown(mytxt)
            

    with st.expander('여기를 누르세요...'):
        st.image(images[0])
        pass