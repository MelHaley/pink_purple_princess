import altair as alt
import streamlit as st
import graph_legos as gl

st.set_page_config(page_title="Princesses, etc.", layout='wide')

########################################################################
with st.sidebar:
    st.image('LegoData/Images/color_lego.png')

st.title("LEGO Analysis: Princesses, Unicorns, Fairies, Mermaids, and Kitties")

########################################################################
# Categories and Metrics
with st.container(height=None, border=False):
    st.subheader("Sets, Themes, and Colors per Category")
    switch = st.radio(label='metric radio',
                      options=['all colors', 'pink and purple'],
                      horizontal=True,
                      label_visibility='hidden',
                      key='metric')
    if switch == "all colors":
        col = st.columns((1, 1, 1, 1, 1), gap='medium')
        with col[0]:
            st.image('./LegoData/Images/princess.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/all_stats', 
                                                  data_name='princess', 
                                                  border='black'),
                            use_container_width=True)
        with col[1]:
            st.image('./LegoData/Images/unicorn.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/all_stats', 
                                                  data_name='unicorn', 
                                                  border='black'),
                            use_container_width=True)
        with col[2]:
            st.image('./LegoData/Images/fairy.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/all_stats', 
                                                  data_name='fairy', 
                                                  border='black'),
                            use_container_width=True)
        with col[3]:
            st.image('./LegoData/Images/mermaid.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/all_stats', 
                                                  data_name='mermaid', 
                                                  border='black'),
                            use_container_width=True)
        with col[4]:
            st.image('./LegoData/Images/kitty.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/all_stats', 
                                                  data_name='kitty', 
                                                  border='black'),
                            use_container_width=True)

    if switch == "pink and purple":
        col = st.columns((1, 1, 1, 1, 1), gap='medium')
        with col[0]:
            st.image('./LegoData/Images/princess.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/pink_stats', 
                                                  data_name='princess', 
                                                  border='orchid'),
                            use_container_width=True)
        with col[1]:
            st.image('./LegoData/Images/unicorn.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/pink_stats', 
                                                  data_name='unicorn', 
                                                  border='orchid'),
                            use_container_width=True)
        with col[2]:
            st.image('./LegoData/Images/fairy.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/pink_stats', 
                                                  data_name='fairy', 
                                                  border='orchid'),
                            use_container_width=True)
        with col[3]:
            st.image('./LegoData/Images/mermaid.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/pink_stats', 
                                                  data_name='mermaid', 
                                                  border='orchid'),
                            use_container_width=True)
        with col[4]:
            st.image('./LegoData/Images/kitty.png')
            st.altair_chart(gl.plot_category_info(data_path='./LegoData/Category/pink_stats', 
                                                  data_name='kitty', 
                                                  border='orchid'),
                            use_container_width=True)

########################################################################
themes_tab, parts_tab, time_tab = st.tabs(['themes and sets', 'parts', 'timeline'])

########################################################################
# Themes and sets plots
with themes_tab:
    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("Which themes have the most sets per category?")
            all_tab1, princess_tab1, unicorn_tab1, fairy_tab1, mermaid_tab1, kitty_tab1 = \
                st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
            with all_tab1:
                st.altair_chart(gl.plot_theme_sets('./LegoData/Category/all_cat_theme_sets', h=400, img_x='-15'),
                                use_container_width=True)
            with princess_tab1:
                st.altair_chart(gl.plot_theme_sets('./LegoData/Category/cat_theme_sets',
                                                   category='princess'),
                                use_container_width=True)
            with unicorn_tab1:
                st.altair_chart(gl.plot_theme_sets('./LegoData/Category/cat_theme_sets',
                                                   category='unicorn'),
                                use_container_width=True)
            with fairy_tab1:
                st.altair_chart(gl.plot_theme_sets('./LegoData/Category/cat_theme_sets',
                                                   category='fairy'),
                                use_container_width=True)
            with mermaid_tab1:
                st.altair_chart(gl.plot_theme_sets('./LegoData/Category/cat_theme_sets',
                                                   category='mermaid'),
                                use_container_width=True)
            with kitty_tab1:
                st.altair_chart(gl.plot_theme_sets('./LegoData/Category/cat_theme_sets',
                                                   category='kitty'),
                                use_container_width=True)

    with st.container(height=None, border=False):
        col2 = st.columns((5, 1), gap='small')
        with col2[0]:
            st.subheader("Which sets per category have the most pink and purple colors?")
            all_tab2, princess_tab2, unicorn_tab2, fairy_tab2, mermaid_tab2, kitty_tab2 = \
                st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
            with all_tab2:
                st.altair_chart(gl.plot_set_colors('./LegoData/Category/all_set_colors',
                                                   setname='The Enchanted Treehouse',
                                                   image_file='./LegoData/Images/set_images'),
                                use_container_width=True)
            with princess_tab2:
                st.altair_chart(gl.plot_set_colors('./LegoData/Category/cat_set_colors',
                                                   setname='The Enchanted Treehouse',
                                                   category='princess',
                                                   image_file='./LegoData/Images/set_images'),
                                use_container_width=True)
            with unicorn_tab2:
                st.altair_chart(gl.plot_set_colors('./LegoData/Category/cat_set_colors',
                                                   setname='Unicorn Creative Family Pack',
                                                   category='unicorn',
                                                   image_file='./LegoData/Images/set_images'),
                                use_container_width=True)
            with fairy_tab2:
                st.altair_chart(gl.plot_set_colors('./LegoData/Category/cat_set_colors',
                                                   setname="Sleeping Beauty's Fairytale Castle",
                                                   category='fairy',
                                                   image_file='./LegoData/Images/set_images'),
                                use_container_width=True)
            with mermaid_tab2:
                st.altair_chart(gl.plot_set_colors('./LegoData/Category/cat_set_colors',
                                                   setname='The Little Mermaid Royal Clamshell',
                                                   category='mermaid',
                                                   image_file='./LegoData/Images/set_images'),
                                use_container_width=True)
            with kitty_tab2:
                st.altair_chart(gl.plot_set_colors('./LegoData/Category/cat_set_colors',
                                                   setname='Unikingdom Fairground Fun',
                                                   category='kitty',
                                                   image_file='./LegoData/Images/set_images'),
                                use_container_width=True)

    with st.container(height=None, border=False):
        col2 = st.columns((5, 1), gap='small')
        with col2[0]:
            st.subheader("Which sets per category have the most pink and purple pieces?")
            all_tab3, princess_tab3, unicorn_tab3, fairy_tab3, mermaid_tab3, kitty_tab3 = \
                st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
            with all_tab3:
                st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Category/all_pink_pieces',
                                                         setname="The Enchanted Treehouse",
                                                         image_file='./LegoData/Images/set_images'),
                                use_container_width=True)
            with princess_tab3:
                st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Category/cat_pink_pieces',
                                                         setname='The Enchanted Treehouse',
                                                         image_file='./LegoData/Images/set_images',
                                                         category='princess'),
                                use_container_width=True)
            with unicorn_tab3:
                st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Category/cat_pink_pieces',
                                                         setname='Unicorn Creative Family Pack',
                                                         image_file='./LegoData/Images/set_images',
                                                         category='unicorn'),
                                use_container_width=True)
            with fairy_tab3:
                st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Category/cat_pink_pieces',
                                                         setname="Sleeping Beauty's Fairytale Castle",
                                                         image_file='./LegoData/Images/set_images',
                                                         category='fairy'),
                                use_container_width=True)
            with mermaid_tab3:
                st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Category/cat_pink_pieces',
                                                         setname='The Mermaid Castle',
                                                         image_file='./LegoData/Images/set_images',
                                                         category='mermaid'),
                                use_container_width=True)
            with kitty_tab3:
                st.altair_chart(gl.plot_sets_most_pieces(data_path='./LegoData/Category/cat_pink_pieces',
                                                         setname='Unikingdom Fairground Fun',
                                                         image_file='./LegoData/Images/set_images',
                                                         category='kitty'),
                                use_container_width=True)
                
########################################################################
# Parts plots
with parts_tab:
    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("What are the most common pieces per category?")
            switch0 = st.radio(label='metric radio',
                               options=['all colors', 'pink and purple'],
                               horizontal=True,
                               label_visibility='hidden',
                               key='parts')
            if switch0 == "all colors":
                all_tab7, princess_tab7, unicorn_tab7, fairy_tab7, mermaid_tab7, kitty_tab7 = \
                    st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
                with all_tab7:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/cat_top_pieces', 
                                                   category='all', 
                                                   offset=25),
                                    use_container_width=True)
                with princess_tab7:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/cat_top_pieces', 
                                                   category='princess', 
                                                   offset=25),
                                    use_container_width=True)
                with unicorn_tab7:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/cat_top_pieces', 
                                                   category='unicorn', 
                                                   offset=10),
                                    use_container_width=True)
                with fairy_tab7:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/cat_top_pieces', 
                                                   category='fairy', 
                                                   offset=5),
                                    use_container_width=True)
                with mermaid_tab7:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/cat_top_pieces', 
                                                   category='mermaid', 
                                                   offset=10),
                                    use_container_width=True)
                with kitty_tab7:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/cat_top_pieces', 
                                                   category='kitty', 
                                                   offset=5),
                                    use_container_width=True)

            if switch0 == "pink and purple":
                all_tab8, princess_tab8, unicorn_tab8, fairy_tab8, mermaid_tab8, kitty_tab8 = \
                    st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
                with all_tab8:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/pink_top_pieces', 
                                                   category='all', 
                                                   offset=25),
                                    use_container_width=True)
                with princess_tab8:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/pink_top_pieces', 
                                                   category='princess', 
                                                   offset=25),
                                    use_container_width=True)
                with unicorn_tab8:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/pink_top_pieces', 
                                                   category='unicorn', 
                                                   offset=9),
                                    use_container_width=True)
                with fairy_tab8:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/pink_top_pieces', 
                                                   category='fairy', 
                                                   offset=3),
                                    use_container_width=True)
                with mermaid_tab8:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/pink_top_pieces', 
                                                   category='mermaid', 
                                                   offset=3),
                                    use_container_width=True)
                with kitty_tab8:
                    st.altair_chart(gl.plot_pieces(data_path='./LegoData/Category/pink_top_pieces', 
                                                   category='kitty', 
                                                   offset=4),
                                    use_container_width=True)

    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("Which color has the most pieces per category?")
            all_tab4, princess_tab4, unicorn_tab4, fairy_tab4, mermaid_tab4, kitty_tab4 = \
                st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
            with all_tab4:
                st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Category/category_pink_purple'),
                                use_container_width=True)
            with princess_tab4:
                st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Category/category_pink_purple',
                                                      category='princess'),
                                use_container_width=True)
            with unicorn_tab4:
                st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Category/category_pink_purple',
                                                      category='unicorn'),
                                use_container_width=True)
            with fairy_tab4:
                st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Category/category_pink_purple',
                                                      category='fairy'),
                                use_container_width=True)
            with mermaid_tab4:
                st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Category/category_pink_purple',
                                                      category='mermaid'),
                                use_container_width=True)
            with kitty_tab4:
                st.altair_chart(gl.plot_pieces_shapes(data_path='./LegoData/Category/category_pink_purple',
                                                      category='kitty'),
                                use_container_width=True)
                
########################################################################
# Timeline plots 
with time_tab:
    with st.container(height=None, border=False):
        col = st.columns((5, 1), gap='small')
        with col[0]:
            st.subheader("How many sets were introduced each year per category?")
            st.altair_chart(gl.plot_set_theme_by_year(data_path='./LegoData/Category/category_df', 
                                                      y_var='set_num', 
                                                      data_name='Set'),
                            use_container_width=True)

            st.subheader("How many colors were introduced each year per category?")
            switch1 = st.radio(label='metric radio',
                               options=['all colors', 'pink and purple'],
                               horizontal=True,
                               label_visibility='hidden',
                               key='colors')
            if switch1 == "all colors":
                all_tab5, princess_tab5, unicorn_tab5, fairy_tab5, mermaid_tab5, kitty_tab5 = \
                    st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
                with all_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/all_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")]),
                                    use_container_width=True)
                with princess_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='princess'), use_container_width=True)
                with unicorn_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='unicorn'), use_container_width=True)
                with fairy_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='fairy'), use_container_width=True)
                with mermaid_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='mermaid'), use_container_width=True)
                with kitty_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='kitty'), use_container_width=True)
            if switch1 == "pink and purple":
                all_tab5, princess_tab5, unicorn_tab5, fairy_tab5, mermaid_tab5, kitty_tab5 = \
                    st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
                with all_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/color_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")]),
                                    use_container_width=True)
                with princess_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='princess'), use_container_width=True)
                with unicorn_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='unicorn'), use_container_width=True)
                with fairy_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='fairy'), use_container_width=True)
                with mermaid_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='mermaid'), use_container_width=True)
                with kitty_tab5:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='count(color_name)',
                                                    data_name='Colors', 
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color")],
                                                    category='kitty'), use_container_width=True)

            st.subheader("How many pieces were introduced each year per category?")
            switch2 = st.radio(label='metric radio',
                               options=['all colors', 'pink and purple'],
                               horizontal=True,
                               label_visibility='hidden',
                               key='pieces')
            if switch2 == "all colors":
                all_tab6, princess_tab6, unicorn_tab6, fairy_tab6, mermaid_tab6, kitty_tab6 = \
                    st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
                with all_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/all_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")]),
                                    use_container_width=True)
                with princess_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='princess'), use_container_width=True)
                with unicorn_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='unicorn'), use_container_width=True)
                with fairy_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='fairy'), use_container_width=True)
                with mermaid_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='mermaid'), use_container_width=True)
                with kitty_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/cat_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='kitty'), use_container_width=True)
            if switch2 == "pink and purple":
                all_tab6, princess_tab6, unicorn_tab6, fairy_tab6, mermaid_tab6, kitty_tab6 = \
                    st.tabs(['all', 'princess', 'unicorn', 'fairy', 'mermaid', 'kitty'])
                with all_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/color_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")]),
                                    use_container_width=True)
                with princess_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='princess'), use_container_width=True)
                with unicorn_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='unicorn'), use_container_width=True)
                with fairy_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='fairy'), use_container_width=True)
                with mermaid_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='mermaid'), use_container_width=True)
                with kitty_tab6:
                    st.altair_chart(gl.plot_by_year(data_path='./LegoData/Category/pink_by_year', 
                                                    y_var='quantity', 
                                                    data_name='Pieces',
                                                    tooltip_opt=[alt.Tooltip('color_name', title="Color"),
                                                                 alt.Tooltip('quantity', title="# of pieces")],
                                                    category='kitty'), use_container_width=True)
