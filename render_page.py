from jinja2 import Template

import configparser

icon_config = configparser.ConfigParser()
icon_config.read('./icons.ini')

class Icon(object):
  pass

icons = list()

for icon_name in icon_config.sections():
  icon = Icon()
  icon.name = icon_name
  icon.url = 'http://localhost'
  icon.image = 'default.jpg'
  icon.label = 'No label'
  for (field_name, field_value) in icon_config.items(icon_name):
    if field_name == 'url':
      icon.url = field_value
    if field_name == 'image':
      icon.image = field_value
    if field_name == 'label':
      icon.label = field_value
  icons.append(icon)

with open('index.html.jinja') as f:
  template = Template(f.read())

with open('index.html', 'w') as f:
  f.write(template.render(icons = icons))

