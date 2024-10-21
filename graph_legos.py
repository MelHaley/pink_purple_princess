"""
A group of functions used to create visualizations for LEGO
analysis.
"""

import altair as alt
import numpy as np
import pandas as pd


########################################################################
def plot_colors(data_path):
    """Generate an interactive plot of color shades  

    Args:
        data_path (str): pickled dataframe path 

    Return:
        altair chart
    """
    df = pd.read_pickle(data_path)
    selector = alt.selection_point(fields=['color_name'])
    color_order = list(df.sort_values(by='quantity',
                                      ascending=False)['color_name'])
    base = alt.Chart(df).encode(
        x=alt.X('color_name').sort(color_order)
        .title('Color Name')
        .axis(None)
    ).add_params(selector
                 ).properties(width=600, height=70)

    chart = base.mark_bar(cornerRadius=3, stroke='black',
                          ).encode(
        y=alt.Y('count(color_name)').scale(domain=[0, 1])
        .axis(None),
        color=alt.Color('hex').scale(None),
        tooltip=['image'])

    return chart


########################################################################
def plot_theme_colors(data_path):
    """
    Generates a horizontal bar plot of themes with most pink and 
    purple colors and theme logo. 
  
    Args:
        data_path (str): pickled dataframe path 

    Return:
        altair chart
    """
    df = pd.read_pickle(data_path)

    base = alt.Chart(df, title=alt.Title(f'Top Themes: Most Colors')
                     ).transform_calculate(
        image_x="-3"
    ).encode(
        x=alt.X('count(color_name)'),
        y=alt.Y('theme_name').sort('-x').axis(None),
    ).properties(width=500, height=600)

    image = base.mark_image(height=100, width=100,
                            ).encode(
        x=alt.X('image_x:Q').axis(None),
        url='image',
        tooltip=alt.value(None))

    bar = base.mark_bar(cornerRadius=3, height=25, stroke='black'
                        ).encode(
        x=alt.X('count(color_name)').axis(None),
        tooltip=[alt.Tooltip('theme_name', title="Theme"),
                 alt.Tooltip('color_name', title="Color")],
        color=alt.Color('hex').scale(None))

    text = base.mark_text(align='left', baseline='middle', dx=5, fontSize=18
                          ).encode(
        text=alt.Text('count(color_name)'))

    chart = alt.layer(bar, image, text
                      ).configure_view(stroke=None)

    return chart


########################################################################
def plot_theme_sets(data_path, category=None, h=400, img_x='-15', dom=125):
    """
    Generates a horizontal bar plot displaying the themes with the most 
    pink and purple sets, along with the corresponding theme logos.

    Args:
        data_path (str): Path to the pickled dataframe containing the theme and color data.
        category (str, optional): The category to filter the themes by (default is None).
        h (int, optional): Height of the plot (default is 400).
        img_x (str, optional): X-axis offset for the logo images (default is '-15').
        dom (int, optional): X-axis scaling (default is 125).

    Returns:
        altair.Chart: The generated Altair chart with themes and logos.
    """
    df = pd.read_pickle(data_path)
    if category:
        df = df[df['category'] == category]
    else:
        category = 'all'
    base = alt.Chart(df, title=alt.Title(f'Top Themes: Most Sets - {category.upper()}')
                     ).transform_calculate(
        image_x=img_x
    ).encode(
        x=alt.X('set_num'),
        y=alt.Y('theme_name').sort('-x').axis(None),
    ).properties(width=500, height=h)

    image = base.mark_image(height=100, width=100,
                            ).encode(
        x=alt.X('image_x:Q').axis(None),
        url='image',
        tooltip=alt.value(None))

    bar = base.mark_bar(cornerRadius=3, height=25, stroke='black', fill='white'
                        ).encode(
        x=alt.X('set_num').axis(None).scale(domain=[0, dom]),
        tooltip=[alt.Tooltip('theme_name', title="Theme"),
                 alt.Tooltip('set_num', title="# of Sets")])

    text = base.mark_text(align='left', baseline='middle', dx=5, fontSize=18
                          ).encode(
        text=alt.Text('set_num'))

    chart = alt.layer(bar, image, text
                      ).configure_view(stroke=None)

    return chart


########################################################################
def plot_set_colors(data_path, setname, image_file, h=150, category=None):
    """
    Generates a plot displaying the sets with the most pink and purple colors.

    Args:
        data_path (str): Path to the pickled dataframe containing the set and color data.
        setname (str): The specific set name to filter and display at start.
        image_file (str): Path to the pickled dataframe containing the set images.
        h (int, optional): Height of the plot (default is 150).
        category (str, optional): The category to filter the sets by (default is None).

    Returns:
        altair.Chart: The generated Altair chart showing the set color distribution.
    """
    df = pd.read_pickle(data_path)
    if category:
        source = df[df['category'] == category]
    else:
        source = df

    image_source = pd.read_pickle(image_file)

    selector = alt.selection_point(fields=['set_name'], value=setname, empty=False)

    base = alt.Chart(source, title=alt.Title(f'Top Sets: Most Pink and Purple Colors',
                                             subtitle=['', '*click bar to see set image']
                                             )).mark_bar(
        cornerRadius=3, height=25, stroke='black'
    ).encode(
        x=alt.X('count(color_name)').scale(domain=[0, 10]).axis(None),
        y=alt.Y('set_name').sort('-x'),
    ).add_params(selector).properties(height=h, width=250)

    img_faceted = alt.Chart(image_source,
                            width=375,
                            height=275).mark_image().encode(
        url='image',
        tooltip=[alt.Tooltip('set_name', title="Set Name"),
                 alt.Tooltip('theme_name', title='Theme')]
    ).facet(
        alt.Facet('image', title='', header=alt.Header(labelFontSize=0))
    ).transform_filter(selector)

    bar = base.mark_bar(cornerRadius=3, width=15, stroke='black'
                        ).encode(
        x=alt.X('count(color_name)').axis(None),
        # text=data_column,
        tooltip=[alt.Tooltip('color_name', title="Color"),
                 alt.Tooltip('theme_name', title="Theme")],
        color=alt.Color('hex').scale(None))

    text = base.mark_text(
        align='left',
        baseline='middle',
        dx=7,
        fontSize=18
    ).encode(
        text='count(color_name)',
        tooltip=[alt.Tooltip('theme_name', title='Theme'),
                 alt.Tooltip('count(color_name)', title='# of Colors')]
    ).add_params(selector)

    chart = (bar + text | img_faceted).configure(
        autosize=alt.AutoSizeParams(resize=True)
    ).configure_view(stroke=None).configure_axisY(
        labelFontSize=16,
        grid=False,
        domainOpacity=0,
        tickOpacity=0,
        labelLimit=10000,
        title='Set Name')
    return chart


########################################################################
def plot_theme_pieces(data_path):
    """
    Generates a horizontal bar plot displaying the themes with the most pink and 
    purple pieces, along with the corresponding theme logos.

    Args:
        data_path (str): Path to the pickled dataframe containing theme and piece color data.

    Returns:
        altair.Chart: The generated Altair chart showing the themes and their logos.
    """
    df = pd.read_pickle(data_path)

    base = alt.Chart(df, title=alt.Title(f'Top Themes: Most Pieces')
                     ).transform_calculate(
        image_x='-3000'
    ).encode(
        x=alt.X('sum(quantity):Q'),
        y=alt.Y('theme_name').sort('-x').axis(None),
    ).properties(width=500, height=500)

    image = base.mark_image(height=100, width=100,
                            ).encode(
        x=alt.X('image_x:Q').axis(None),
        url='image',
        tooltip=alt.value(None))

    bar = base.mark_bar(cornerRadius=3, height=25, stroke='black'
                        ).encode(
        x=alt.X('quantity').axis(None),
        tooltip=[alt.Tooltip('theme_name', title="Theme"),
                 alt.Tooltip('color_name', title="Color"),
                 alt.Tooltip('quantity', title="# of Pieces")],
        color=alt.Color('hex').scale(None))

    text = base.mark_text(align='left', baseline='middle', dx=5, fontSize=18
                          ).encode(
        text=alt.Text('sum(quantity)'))

    chart = alt.layer(bar, image, text
                      ).configure_view(stroke=None)

    return chart


########################################################################
def plot_sets_most_pieces(data_path, setname, image_file, h=150, category=None):
    """
    Generates an interactive plot displaying the sets with the most pink and purple 
    pieces, including set images.

    Args:
        data_path (str): Path to the pickled dataframe containing set and piece color data.
        setname (str): The specific set name to filter and plot.
        image_file (str): Path to the pickled dataframe containing the set images.
        h (int, optional): Height of the plot (default is 150).
        category (str, optional): The category to filter the sets by (default is None).

    Returns:
        altair.Chart: The generated Altair chart showing the sets, their piece counts, and images.
    """
    df = pd.read_pickle(data_path)
    if category:
        df = df[df['category'] == category]
    else:
        category = 'all'

    image_source = pd.read_pickle(image_file)
    selector = alt.selection_point(fields=['set_name'], value=setname, empty=False)

    base = alt.Chart(df, title=alt.Title(f'Top Sets: Most Pink and Purple Pieces - {category.upper()}',
                                         subtitle=['', '*click bar to see set image']
                                         )).mark_bar(
        cornerRadius=3, height=25, stroke='black'
    ).encode(
        x=alt.X('sum(quantity)'),  # .scale(domain=[0,10]).axis(None),
        y=alt.Y('set_name:N').sort('-x'),
    ).add_params(selector).properties(height=h, width=250)

    img_faceted = alt.Chart(image_source,
                            width=375,
                            height=375).mark_image().encode(
        url='image',
        tooltip=[alt.Tooltip('set_name:N', title="Set Name"),
                 alt.Tooltip('theme_name:N', title="Theme")]
    ).facet(
        alt.Facet('image', title='', header=alt.Header(labelFontSize=0))
    ).transform_filter(selector)

    bar = base.mark_bar(cornerRadius=3, width=15, stroke='black'
                        ).encode(
        x=alt.X('quantity').axis(None),
        tooltip=[alt.Tooltip('color_name', title="Color"),
                 alt.Tooltip('quantity', title="# of Pieces")],
        color=alt.Color('hex').scale(None))

    text = base.mark_text(
        align='left',
        baseline='middle',
        dx=7,
        fontSize=18
    ).encode(
        text='sum(quantity)',
        tooltip=[alt.Tooltip('theme_name:N', title='Theme'),
                 alt.Tooltip('sum(quantity)', title="# of Pieces")]
    ).add_params(selector)

    chart = (bar + text | img_faceted).configure(
        autosize=alt.AutoSizeParams(resize=True)
    ).configure_view(stroke=None).configure_axisY(
        labelFontSize=16,
        grid=False,
        domainOpacity=0,
        tickOpacity=0,
        labelLimit=10000,
        title='Set Name')
    return chart


########################################################################
def plot_parts_most_colors(data_path):
    """
    Generates a bar plot showing the piece count by color, along with images 
    for pieces that come in the most colors.

    Args:
        data_path (str): Path to the pickled dataframe containing piece and color data.

    Returns:
        altair.Chart: The generated Altair chart displaying piece counts by color with images.
    """
    df = pd.read_pickle(data_path)

    base = alt.Chart(df,
                     title=alt.Title('Pieces With the Most Pink and Purple Shades')
                     ).transform_calculate(
        image_y="datum.num_colors + 2.5"
    ).encode(
        x=alt.X('part_num:N').axis(labels=False).sort('-y').axis(None),
    )

    image = base.mark_image(
        height=45,
        width=45,
    ).encode(
        y=alt.Y('image_y:Q').axis(None),
        url='image',
        tooltip=[alt.Tooltip('part_num', title="Part #"),
                 alt.Tooltip('num_colors', title="Colors")]
    )

    bar = base.mark_bar(
        cornerRadius=3,
        width=30,
        stroke='black',
    ).encode(
        y=alt.Y('fraction').title('Number of Colors'),
        color=alt.Color('hex').scale(None),
        tooltip=[alt.Tooltip('part_num', title="Part #"),
                 alt.Tooltip('color_name', title='Color'),
                 alt.Tooltip('quantity', title='Quantity')]
    )

    text = image.mark_text(
        align='center',
        baseline='bottom',
        dy=40,
        fill='gray',
        fontSize=18
    ).encode(
        text='num_colors',
    )

    chart = alt.layer(bar, image, text
                      ).configure_view(
        stroke=None
    )

    return chart


########################################################################
def plot_pieces_shapes(data_path, x_var='quantity', data_name='Pieces', category=None):
    """
    Generates a horizontal bar plot showing either shape count or piece 
    count per color.

    Args:
        data_path (str): Path to the pickled dataframe containing piece and color data.
        x_var (str, optional): Column name for the x-axis variable (default is 'quantity').
        data_name (str, optional): Label for the variable being plotted (default is 'Pieces').
        category (str, optional): The category to filter the pieces by (default is None).

    Returns:
        altair.Chart: The generated Altair chart displaying shape or piece counts per color.
    """
    df = pd.read_pickle(data_path)
    if category:
        source = df[df['category'] == category].groupby('color_name') \
            .agg({'part_num': 'nunique', 'quantity': 'sum', 'hex': 'max'}) \
            .reset_index()
    else:
        source = df.groupby('color_name') \
            .agg({'part_num': 'nunique', 'quantity': 'sum', 'hex': 'max'}) \
            .reset_index()

    base = alt.Chart(source, title=f'{data_name} per Color').mark_bar(
        cornerRadius=3,
        stroke='black',
    ).encode(
        y=alt.Y('color_name:N').title('Color').sort('-x'),
        x=x_var,
        color=alt.Color('hex').scale(None),
        tooltip=[alt.Tooltip('color_name', title="Color"),
                 alt.Tooltip(x_var, title=data_name)]
    )
    text = base.mark_text(
        align='left',
        baseline='middle',
        dx=5,
        color='hex',
        fontWeight=500,
        fontSize=18
    ).encode(
        text=x_var,
    )
    chart = alt.layer(base, text).configure_axisBottom(
        disable=True,
    ).configure_axisY(grid=False,
                      ).configure_view(stroke=None)

    return chart


########################################################################
def plot_pieces(data_path, category, offset):
    """
    Generates a bar plot displaying the piece count, along with images of the most common pieces 
    in the specified color or category.

    Args:
        data_path (str): Path to the pickled dataframe containing piece data.
        category (str): The color or category to filter by (e.g., pink, purple, pink and purple, 
            princesses, unicorns, mermaids, fairies, or kitties).
        offset (int): The distance between the image and the top of each bar in the plot.

    Returns:
        altair.Chart: The generated Altair chart showing piece counts and corresponding images.
    """
    df = pd.read_pickle(data_path)
    if category == 'all':
        source = df.sort_values(by='quantity', ascending=False)[:10] \
            .set_index([pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]).reset_index()
    else:
        source = df[df['category'] == category].sort_values(by='quantity', ascending=False)[:10].reset_index()

    base = alt.Chart(source, title=alt
                     .Title(f'Most Common Pieces: {category.upper()}',
                            subtitle="Total count across all unique sets")
                     ).transform_calculate(image_y=f"datum.quantity + {offset}",
                                           ).encode(
        x=alt.X('index:O').sort('-y').axis(None),
    ).properties(width=600, height=400)

    image = base.mark_image(height=50, width=50,
                            ).encode(
        y=alt.Y('image_y:Q').axis(None),
        url='image',
        tooltip=[alt.Tooltip('color_name', title="Color"),
                 alt.Tooltip('part_num', title="Part #"),
                 alt.Tooltip('quantity', title="Quantity")])

    bar = base.mark_bar(cornerRadius=3, width=25, stroke='black',
                        ).encode(
        y=alt.Y('quantity').axis(None),
        color=alt.Color('hex').scale(None),
        tooltip=[alt.Tooltip('color_name', title="Color"),
                 alt.Tooltip('part_num', title="Part #"),
                 alt.Tooltip('quantity', title="Quantity")])

    text = bar.mark_text(
        fill='black',
        align='center',
        baseline='bottom',
        dx=0,
        dy=-1.5,
        fontSize=18,
    ).encode(
        text='quantity')

    chart = alt.layer(bar, image, text
                      ).configure_view(stroke=None)

    return chart


########################################################################
def plot_by_year(data_path, y_var, data_name, tooltip_opt=None, category=None):
    """
    Generates a bar graph showing the total amount of a specified variable (y_var) 
    available each year.

    Args:
        data_path (str): Path to the pickled dataframe containing the data.
        y_var (str): Column name for the y-axis variable (the variable to be totaled by year).
        data_name (str): Name of the variable being plotted (used in the chart labels).
        tooltip_opt (list, optional): Optional list of tooltip specifications for additional information 
            on hover (default is None).
        category (str, optional): Category to filter the data by (default is None).

    Returns:
        altair.Chart: The generated bar graph showing totals by year.
    """
    df = pd.read_pickle(data_path)
    if category:
        source = df[df['category'] == category]
    else:
        source = df
    chart_title = f'{data_name} Introduced Per Year'
    y_title = f"Number of {data_name}"
    years = np.arange(1991, 2024, 1)
    chart = alt.Chart(source, title=chart_title).mark_bar(
        cornerRadius=3,
        stroke='black',
    ).encode(
        x=alt.X('year:O').title('Year').stack(None).scale(domain=years),
        y=alt.Y(y_var).title(y_title),
        color=alt.Color('hex').scale(None),
        tooltip=tooltip_opt
    ).properties(width=600, height=500
                 ).configure_axisY(labelLimit=1000)
    return chart


########################################################################
def plot_set_theme_by_year(data_path, y_var, data_name,
                           d_choice=['princess', 'unicorn', 'fairy', 'mermaid', 'kitty', 'all'],
                           r_choice=['hotpink', 'darkmagenta', 'rebeccapurple', 'deeppink', 'plum', 'white']):
    """
    Generates a bar plot showing the number of themes or sets containing pink, 
    purple, or both colors by year.
    
    Args:
        data_path (str): Path to the pickled dataframe containing the data.
        y_var (str): Name of the column representing the y-axis variable (e.g., theme or set count).
        data_name (str): Label for the y variable (used in the chart).
        d_choice (list, optional): List of themes to filter by (default includes 'princess', 
            'unicorn', 'fairy', 'mermaid', 'kitty', and 'all').
        r_choice (list, optional): List of colors to filter by (default includes 'hotpink', 
            'darkmagenta', 'rebeccapurple', 'deeppink', 'plum', and 'white').
    
    Returns:
        altair.Chart: The generated bar plot showing the number of themes or sets by year.
    """
    df = pd.read_pickle(data_path)
    source1 = df.groupby(['year', 'category'])[y_var] \
        .nunique().reset_index()
    source2 = df.groupby('year')[y_var].nunique().reset_index()
    source2['category'] = 'all'
    chart_title = f'{data_name}s Introduced Per Year'
    selector = alt.selection_point(fields=['category'], bind='legend')
    years = np.arange(1991, 2024, 1)

    both = alt.Chart(source2, title=chart_title
                     ).mark_bar(
        fill='white',
        cornerRadius=3,
        stroke='black',
    ).encode(
        x=alt.X('year:O').title('Year').scale(domain=years),
        y=alt.Y(y_var).stack(None).title(f'{data_name} Count'),
        opacity=alt.condition(selector, alt.value(1), alt.value(0)),
        color=alt.Color('category').scale(domain=d_choice, range=r_choice)
        .title(None),
        tooltip=[alt.Tooltip(y_var, title=f'{data_name}s:')]
    ).properties(width=600, height=500
                 ).add_params(selector)

    by_color = alt.Chart(source1).mark_bar(
        cornerRadius=3,
        stroke='black',
    ).encode(
        x=alt.X('year:O').title('Year').scale(domain=years),
        y=alt.Y(y_var).title(f'{data_name} Count').stack(None),
        opacity=alt.condition(selector, alt.value(1), alt.value(0)),
        color=alt.Color('category').scale(domain=d_choice, range=r_choice)
        .title(None),
        tooltip=[alt.Tooltip(y_var, title=f"{data_name}s:"),
                 alt.Tooltip('category', title="Color")]
    ).add_params(selector)

    return both + by_color


#######################################################################
def plot_color_timeline(data_path):
    """
    Generates a timeline plot illustrating the distribution of colors over time.

    Args:
        data_path (str): Path to the pickled dataframe containing color data and timestamps.

    Returns:
        altair.Chart: The generated timeline plot showing color distribution over time.
    """
    df = pd.read_pickle(data_path)
    domain = np.arange(1990, 2026, 1)
    chart = alt.Chart(df, title='Color Timespan').mark_bar(
        stroke='black',
        cornerRadius=3
    ).transform_calculate(
        years='datum.last - datum.first'
    ).encode(
        x=alt.X('first:O').scale(domain=domain).title('Year'),
        x2=alt.X2('last:O'),
        y=alt.Y('color_name').title('Color'),
        color=alt.Color('hex:N').scale(None),
        tooltip=[alt.Tooltip('color_name', title='Color'),
                 alt.Tooltip('years:Q', title='Years')]
    ).configure_view(stroke=None
                     ).configure(autosize=alt.AutoSizeParams(resize=True))
    return chart


#######################################################################
def plot_category_info(data_path, data_name, border):
    """
    Generates a plot displaying the number of sets, themes, and colors for each category.

    Args:
        data_path (str): Path to the dataframe containing category data.
        data_name (str): Name of the variable being plotted (used in the chart labels).
        border (str): Color of bar borders in plot.

    Returns:
        altair.Chart: The generated plot showing counts of sets, themes, and colors per category.
    """
    df = pd.read_pickle(data_path)
    source = df[df['category'] == data_name]

    domain = ['sets', 'themes', 'colors']
    color_range = ['white', 'lightgray', 'gray']
    base = alt.Chart(source, title=alt.Title(
        data_name,
        fontSize=24,
        dy=15,
        anchor='middle')
                     ).transform_fold(
        ['sets', 'themes', 'colors'],
    ).mark_bar(
        stroke=border,
        cornerRadius=3
    ).encode(
        alt.X('key:N').axis(None),
        alt.Y('value:Q').axis(None).scale(domain=[0, 130]),
        color=alt.Color('key:N').scale(domain=domain, range=color_range).legend(None),
        tooltip=alt.value(None),
    ).properties(
        width=70,
        height=200
    )

    text = base.mark_text(
        fill='black',
        fontSize=14,
        dy=-12
    ).encode(
        text='stat_text:N',
        tooltip=alt.value(None)
    ).transform_calculate(
        stat_text='datum.value + " " + datum.key'
    )
    return base + text


#######################################################################
def waterfall(data_path):
    """
    Creates a waterfall chart visualizing the changes in the number of sets 
    over a specified period.

    Args:
        data_path (str): Path to the data source containing the set information.

    Returns:
        altair.Chart: The generated waterfall chart displaying the net changes in set numbers.
    """
    source = pd.read_pickle(data_path)
    axis_min = source['count'].min() - 5
    axis_max = source['count'].max() + 5
    base = alt.Chart(source).transform_window(
        lead_year="lead(year)",
        axis_min="min(count)"
    ).transform_calculate(
        previous="datum.year === 2007 ? 0 : datum.count - datum.change",
        lead_year="datum.lead_year === null ? datum.year : datum.lead_year",
        text_middle="datum.year === 2007 ? null : datum.count - (datum.change)/2",
        positive="datum.change > 0 || datum.year === 2007 ? datum.count : null",
        change_text="datum.change > 0 ? '+' + datum.change : datum.change",
        negative="datum.change < 0 || datum.year === 2024 ? datum.count : null",
        text_offset="datum.change > 0 ? datum.count - 4 : datum.count + 4",
    ).encode(
        alt.X("year:O").axis(title="Year", labelAngle=0),
    )
    color_coding = {
        "condition": [
            {"test": "datum.year === 2024", "value": "#878d96"},
            {"test": "datum.change > 0", "value": "#FF1493"},
        ],
        "value": "#663399",
    }

    bar = base.mark_bar().encode(
        alt.Y("count:Q").scale(domain=(axis_min, axis_max), clamp=True).axis(title="Number of Sets"),
        alt.Y2("previous:Q"),
        color=color_coding,
        tooltip=[alt.Tooltip('year', title='Year'),
                 alt.Tooltip('count', title='# of sets'),
                 alt.Tooltip('change_text:N', title='Net change')]
    )
    rule = base.mark_rule(
        xOffset=-24,
        x2Offset=24,
    ).encode(
        y="count:Q",
        x2="lead_year",
        tooltip=alt.value(None),
    )
    text_coding = {
        "condition": [
            {"test": "datum.change > 0", "value": "datum.count - 5"},
            {"test": "datum.change < 0", "value": "datum.count + 5"},
        ]}
    text_increase = base.mark_text(
        baseline="bottom",
        dy=-4,
        fontSize=16
    ).encode(
        text=alt.Text("count:Q"),
        y="positive:Q",
        tooltip=alt.value(None),
    )
    text_decrease = base.mark_text(
        baseline="top",
        dy=4,
        fontSize=16
    ).encode(
        text=alt.Text("count:Q"),
        y="negative:Q",
        tooltip=alt.value(None),
    )
    text_change = base.mark_text(
        baseline="middle",
    ).encode(
        text=alt.Text("change_text:N"),
        y="text_middle:Q",
        color=alt.value("white"),
        tooltip=alt.value(None),
    )
    return alt.layer(
        bar,
        rule,
        text_increase,
        text_decrease,
        text_change,
    ).properties(
        width=800,
        height=400
    )


#######################################################################
def plot_prices(data_path):
    """
    Generates a plot visualizing the price distribution of items in the dataset.

    Args:
        data_path (str): Path to the data source containing pricing information.

    Returns:
        altair.Chart: The generated plot showing the distribution of prices.
    """
    df = pd.read_pickle(data_path)
    plot = alt.Chart(df).mark_boxplot(color='#663399', extent="min-max").encode(
        alt.Y("theme_name_x:N").axis(title="Theme"),
        alt.X("us_retail:Q").axis(title="Retail Price (US$)", format='$,.2f'),
        tooltip=[
            alt.Tooltip("us_retail:Q", format=",.2f"),
        ],
    ) + alt.Chart(df).mark_circle(color='#FF1493', size=50).encode(
        y='theme_name_x:N',
        x='mean(us_retail):Q',
    ) + alt.Chart(df).transform_aggregate(
        min="min(us_retail)",
        max="max(us_retail)",
        mean="mean(us_retail)",
        median="median(us_retail)",
        q1="q1(us_retail)",
        q3="q3(us_retail)",
        count="count()",
        groupby=['theme_name_x']
    ).mark_bar(opacity=0).encode(
        y='theme_name_x:N',
        x='q1:Q',
        x2='q3:Q',
        tooltip=[alt.Tooltip('theme_name_x:N', title='Theme'),
                 alt.Tooltip('min:Q', title='Min', format='$,.2f'),
                 alt.Tooltip('median:Q', title='Median', format='$,.2f'),
                 alt.Tooltip('mean:Q', title='Mean', format='$,.2f'),
                 alt.Tooltip('max:Q', title='Max', format='$,.2f')]
    )
    return plot
