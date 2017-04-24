from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot, plot_mpl
from plotly.graph_objs import *
# import numpy as np
# import pandas as pd

def output_markdown(output_file, content):
    with open(output_file, "w") as text_file:
        for cont in content:
            text_file.write("\n%s\n" % (cont))
            
def base_md(base_file):
    with open(base_file, "r") as text_file:
        return text_file.read()

data = [Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

# With plotly.js source code included
content_to_add = [
    base_md("simple_plotly_markdown_base.md"),
    plot(data, show_link=False, include_plotlyjs=True, output_type='div')
]
output_markdown("simple_plotly_markdown_with_included_plotly_js_code.md", content_to_add)

# Without plotly.js
content_to_add = [
    base_md("simple_plotly_markdown_base.md"),
    plot(data, show_link=False, include_plotlyjs=False, output_type='div')
]
output_markdown("simple_plotly_markdown_without_plotly_js.md", content_to_add)

# with plotly.js link to online js
content_to_add = [
    base_md("simple_plotly_markdown_base.md"),
    "\n%s\n" % ("""<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>"""),
    plot(data, show_link=False, include_plotlyjs=False, output_type='div')
]
output_markdown("simple_plotly_markdown_with_online_polotly_js.md", content_to_add)
