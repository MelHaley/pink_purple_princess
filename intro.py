import streamlit as st


st.set_page_config(layout='wide')

#######################################################################


col = st.columns((3, 2), gap='medium')
with col[0]:
    st.title("Pink, Purple, Princesses*")
    st.subheader("a LEGO Analysis")
    st.caption("*and unicorns, fairies, and kitties")
    st.caption("*and mermaids")

with col[1]:
    st.container(height=80, border=False)
    st.image('LegoData/Images/unicorn_large.png')

with col[0]:
    st.container(height=20, border=False)
    st.write(
        "Recently, I was approached by one of my organization's key stakeholders to conduct some analysis that would "
        "inform the direction and focus of the organization's future Lego acquisitions. As a lifelong LEGO "
        "enthusiast, I was excited to jump in and began by downloading publicly available datasets (Kaggle, "
        "Rebrickable, and Brickset) for preliminary data exploration")

    st.write(
        "Meetings with the stakeholder gave me a better understanding of their needs and questions, and together we "
        "formulated a clear and specific focus for the analysis. These discussions were crucial in pinpointing what "
        "my stakeholder's priorities were:")

with col[0]:
    st.subheader('"*more pink, purple, and princess legos*"')
    st.container(height=10, border=False)
    st.write(
        "Specifically, we wanted to gain insight into the history, prevalence, and distribution of pink, purple, "
        "and princess legos (this was later expanded to include fairies, unicorns, kitties, and mermaids).  The "
        "analysis results would then be used to generate a list of high-value sets and themes to target for future "
        "LEGO aquistions.")
    st.write(
        "With these actionable insights, we (and our trusted partner organizations: Santa, Grandma, etc.) were able "
        "to optimize our time and resource investment and streamline our LEGO procurement strategy to better align "
        "with key business objectives.")
    st.container(height=10, border=False)
    st.write('Use the links in the sidebar to explore the analysis results and conclusions.')

with st.sidebar:
    st.image('LegoData/Images/color_lego.png')
