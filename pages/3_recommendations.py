import pandas as pd
import streamlit as st

import graph_legos as gl

########################################################################
st.set_page_config(page_title="Recommendations", layout='wide')

with st.sidebar:
    st.image('LegoData/Images/color_lego.png')

st.title("LEGO Analysis: Recommendations")

st.write("Once our initial analysis was complete, we summarized the key findings, highlighting the insights that we "
         "felt were most important in guiding purchasing strategy going forward.")

########################################################################
# Theme rankings
with st.container(height=None, border=False):
    st.subheader("Theme Rankings")

    col = st.columns((5, 1), gap='small')
    with col[0]:
        st.write(
            "We ranked the themes to identify those most likely to contain high value targets.  We calculated the "
            "probability that given a theme, we would be able to find a set from the pink/purple group or the "
            "princess/unicorn/fairy/mermaid/kitty group. We then selected the top 15 themes that had the highest "
            "probability of containing sets from either group to include in our recommendations.  Duplo themes and "
            "themes with only 1 set were excluded.")

        p_table = pd.read_pickle('./LegoData/Recs/probability_df')
        st.dataframe(
            p_table,
            hide_index=True,
            use_container_width=True,
        )

########################################################################
# Set availability
with st.container(height=None, border=False):
    st.subheader("Availability")
    col = st.columns((5, 1), gap='small')
    with col[0]:
        st.write("Our data set included all unique Lego sets, including retired sets. We performed a net change "
                 "analysis to see how many sets are in current production versus how many would need to be sourced "
                 "from secondhand vendors.")
        st.altair_chart(gl.waterfall(data_path='./LegoData/Recs/net_sets'), use_container_width=True)

########################################################################
# Set pricing
with st.container(height=None, border=False):
    st.subheader("Pricing")
    col = st.columns((5, 1), gap='small')
    with col[0]:
        st.write(
            "An important consideration for any future acquisition is price, so we compiled a summary of the price "
            "distribution of sets within our top 20 themes.")
        st.altair_chart(gl.plot_prices('./LegoData/Recs/to_purchase'), use_container_width=True)

########################################################################
# Recommendation chart
with st.container(height=None, border=False):
    st.subheader("Target Assets to Purchase")
    col = st.columns((5, 1), gap='small')
    with col[0]:
        st.write(
            "We compiled our final acquisition recommendations in the following table.  Users can sort the items "
            "based on their priorities (theme, piece total, category, price, new/used, etc.). Doubleclick on "
            "thumbnails to view set image.  To purchase, click 'BUY' link to go to brickset.com to view a compilation "
            "of available purchasing options for new or used sets.")
        df = pd.read_pickle('./LegoData/Recs/purchase_df')
        theme_options = st.multiselect("Pick Theme:",
                                       options=['All'] + list(df['Theme'].unique()),
                                       default='All')

        if theme_options == ['All']:
            df = df

        else:
            df = df[df['Theme'].isin(theme_options)]

        st.dataframe(
            df,
            column_config={
                "Set Name": st.column_config.Column(
                    width='medium'
                ),
                "Pink/Purple Pieces": st.column_config.Column(
                    width='small'
                ),
                "Piece Total": st.column_config.NumberColumn(
                    format="%f", width='small'
                ),
                "MSRP": st.column_config.NumberColumn(
                    format="$%.2f",
                ),
                'Set Image': st.column_config.ImageColumn(
                ),
                "Retired": st.column_config.CheckboxColumn(
                    default=True
                ),
                "Purchase Link": st.column_config.LinkColumn(
                    display_text="BUY"
                ),
            },
            hide_index=True, use_container_width=True
        )
