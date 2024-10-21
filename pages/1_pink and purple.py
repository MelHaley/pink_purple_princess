import altair as alt
import pandas as pd
import streamlit as st

import graph_legos as gl

st.set_page_config(page_title="Pinks and Purples", layout="wide")

########################################################################
pink_and_purple = pd.read_pickle('./LegoData/Colors/pink_and_purple')
pink_df = pink_and_purple[pink_and_purple['category'] == 'pink']
purple_df = pink_and_purple[pink_and_purple['category'] == 'purple']

st.title("LEGO Analysis: Pinks and Purples")
col = st.columns((1, 1), gap='small')
with col[0]:
    st.write("After cleaning and compiling our data, we analyzed all \
    the unique LEGO sets to obtain answers to the following questions:")

########################################################################
# Colors and Metrics

with st.sidebar:
    st.image('LegoImages/Images/color_lego.png')
    col = st.columns((1, 1), gap='small')
    with col[0]:
        st.metric(label="PINK Colors", value=pink_df['color_name'].nunique(), delta="")
        st.metric(label="PINK Pieces", value=pink_df['quantity'].sum(), delta="")
        st.metric(label="PINK Sets", value=pink_df['set_num'].nunique(), delta="")
        st.metric(label="PINK Themes", value=pink_df['theme_name'].nunique(), delta="")
    with col[1]:
        st.metric(label="PURPLE Colors", value=purple_df['color_name'].nunique(), delta="")
        st.metric(label="PURPLE Pieces", value=purple_df['quantity'].sum(), delta="")
        st.metric(label="PURPLE Sets", value=purple_df['set_num'].nunique(), delta="")
        st.metric(label="PURPLE Themes", value=purple_df['theme_name'].nunique(), delta="")

########################################################################
# Pinks and Purples
with st.container(height=None, border=False):
    st.subheader("Which of the 209 lego colors are shades of pink and purple?")
    colB = st.columns((5, 1), gap='small')
    with colB[0]:
        st.title('16 pinks')
        st.write('*mouse over color for more info*')
        st.altair_chart(gl.plot_colors('./LegoData/Colors/pink_names'),
                        use_container_width=True)

        st.title('19 purples')
        st.altair_chart(gl.plot_colors('./LegoData/Colors/purple_names'),
                        use_container_width=True)

########################################################################
themes_tab, parts_tab, time_tab = st.tabs(['themes and sets', 'parts', 'timeline'])

########################################################################
# Themes and sets plots
with themes_tab:
    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("Which themes have the most pink and purple colors?")
            st.altair_chart(gl.plot_theme_colors('./LegoData/Colors/theme_colors'),
                            use_container_width=True)

            st.subheader("Which themes have the most pink and purple sets?")
            st.altair_chart(gl.plot_theme_sets('./LegoData/Colors/theme_sets',
                                               h=500, img_x='-80', dom=610),
                            use_container_width=True)

            st.subheader("Which sets have the most pink and purple colors?")
            st.altair_chart(gl.plot_set_colors(data_path='./LegoData/Colors/set_colors',
                                               setname='Diagon Alley',
                                               image_file='./LegoData/set_images',
                                               h=300,),
                            use_container_width=True)

            st.subheader("Which themes have the most pink and purple pieces?")
            st.altair_chart(gl.plot_theme_pieces('./LegoData/Colors/theme_pieces'),
                            use_container_width=True)

            st.subheader("Which sets have the most pink and purple pieces?")
            st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Colors/set_pieces',
                                                     setname="Andy Warhol's Marilyn Monroe",
                                                     image_file='./LegoData/set_images',
                                                     h=300),
                            use_container_width=True)

########################################################################
# Parts plots
with parts_tab:
    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("Which shapes come in the most colors?")
            st.altair_chart(gl.plot_parts_most_colors(data_path='./LegoData/Colors/parts_most_colors'),
                            use_container_width=True)

            st.subheader("Which color comes in the most shapes?")
            st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Colors/pink_and_purple', 
                                                  x_var='part_num', 
                                                  data_name='Shapes'),
                            use_container_width=True)

            st.subheader("What are the most common pink or purple pieces?")
            option3 = st.selectbox(label="most common pieces",
                                   options=['pink and purple', 'pink', 'purple'],
                                   label_visibility='hidden')
            if option3 == 'pink and purple':
                st.altair_chart(gl.plot_pieces(data_path='./LegoData/Colors/color_pieces', 
                                               category='all', 
                                               offset=200),
                                use_container_width=True)
            if option3 == 'pink':
                st.altair_chart(gl.plot_pieces(data_path='./LegoData/Colors/color_pieces', 
                                               category='pink', 
                                               offset=200),
                                use_container_width=True)
            if option3 == 'purple':
                st.altair_chart(gl.plot_pieces(data_path='./LegoData/Colors/color_pieces', 
                                               category='purple', 
                                               offset=200),
                                use_container_width=True)

            st.subheader("Which color has the most pieces?")
            st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Colors/pink_and_purple', 
                                                  x_var='quantity', 
                                                  data_name='Pieces'),
                            use_container_width=True)

########################################################################
# Timeline plots 
with time_tab:
    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("How many pink or purple colors were introduced each year?")
            st.altair_chart(gl.plot_by_year(data_path='./LegoData/Colors/plotByYear', 
                                            y_var='count(color_name)',
                                            data_name='Colors', 
                                            tooltip_opt=[alt.Tooltip('color_name', title="Color")]),
                            use_container_width=True)

            st.subheader("How many pink or purple pieces were introduced each year?")
            st.altair_chart(gl.plot_by_year(data_path='./LegoData/Colors/plotByYear', 
                                            y_var='quantity', 
                                            data_name='Pieces',
                                            tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                         alt.Tooltip('quantity', title="# of pieces")]),
                            use_container_width=True)

            st.subheader("How many themes with pink or purple pieces were introduced each year?")
            st.altair_chart(gl.plot_set_theme_by_year(data_path='./LegoData/Colors/pink_and_purple', 
                                                      y_var='theme_name', 
                                                      data_name='Theme',
                                                      d_choice=['pink', 'purple', 'all'],
                                                      r_choice=['hotpink', 'rebeccapurple', 'white']),
                            use_container_width=True)

            st.subheader("How many sets with pink or purple pieces were introduced each year?")
            st.altair_chart(gl.plot_set_theme_by_year(data_path='./LegoData/Colors/pink_and_purple', 
                                                      y_var='set_num', 
                                                      data_name='Set',
                                                      d_choice=['pink', 'purple', 'all'],
                                                      r_choice=['hotpink', 'rebeccapurple', 'white']),
                            use_container_width=True)

            st.subheader("How many unique shapes per color were introduced each year?")
            st.altair_chart(gl.plot_by_year(data_path='./LegoData/Colors/plotByYear', 
                                            y_var='part_num', 
                                            data_name='Shapes',
                                            tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                         alt.Tooltip('part_num', title="# of shapes")]),
                            use_container_width=True)

            st.subheader("How long was each color available?")
            st.altair_chart(gl.plot_color_timeline(data_path='./LegoData/Colors/pink_exit'),
                            use_container_width=True)

########################################################################
