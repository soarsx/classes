
import requests
import pygal
from pygal.style import LightColorizedStyle, LightenStyle

# Make an API call and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status code:', r.status_code)

# Store API response in a variable
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

# Explore the information about the repositories
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {}
    if repo_dict['stargazers_count']:
        plot_dict['value'] = repo_dict['stargazers_count']
    
    if repo_dict['description']:
        plot_dict['label'] = repo_dict['description']

    if repo_dict['html_url']:
        plot_dict['xlink'] = repo_dict['html_url']
        
    plot_dicts.append(plot_dict)

# Make visualitzation.
my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
my_config = pygal.Config()

my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides  = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')