import  pygal
from pygal.style import  LightColorizedStyle as LCS, LightenStyle as  LS

my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_lengend=False)

chart.title="Python Project"
chart.x_labels=['httple','django','flask']
plot_dicts=[
    {'value':16101,'label':'Description of httple'},
    {'value':15028,'label':'Description of django'},
    {'value':14798,'label':'Description of falsk'}
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')