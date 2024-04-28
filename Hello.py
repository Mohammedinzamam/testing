

import streamlit as st
def main():
    st.title("Jobs")
    img=['/workspaces/testing/image/TCS-logo.jpg', '/workspaces/testing/image/TCS-logo.jpg','/workspaces/testing/image/swiggy.jpeg']
    role=['Data Scientist','Web Developer','Data Scientist']
    for f in range(3):
            col1, col2,col3=st.columns(3)
            with col1:
                st.image(img[f], width=120)
            with col2:
                st.subheader(role[f])
                if f==0:
                    st.text("""Tata Consultancy Service
Chennai,Tamilnadu,India""")
                elif f==1:
                    st.text("""Tata Consultancy Services
Hyderabad,Telangana,India""")
                else:
                    st.text("""Swiggy
Bengaluru,Karnataka,India""")
    st.button("View More")
def main2():                
    st.title("Internships")
    img=['/workspaces/testing/image/TCS-logo.jpg', '/workspaces/testing/image/TCS-logo.jpg','/workspaces/testing/image/wipro2.jpeg']
    role=['Data Scientist','Web Developer','machine learning']
    for f in range(3):
            col1, col2,col3=st.columns(3)
            with col1:
                st.image(img[f], width=120)
            with col2:
                st.subheader(role[f])
                if f==0:
                    st.text("""Tata Consultancy Service
3 months
Chennai,Tamilnadu,India""")
                elif f==1:
                    st.text("""Tata Consultancy Services
6 months
Hyderabad,Telangana,India""")
                else:
                    st.text("""Wipro
1 months
Bengaluru,Karnataka,India""")
    st.button("View More",key="some")

if __name__ == "__main__":
    main()
    main2()

