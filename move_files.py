import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find all categories and the items inside them.
# The structure might be a section containing a category title, and then a grid.
# Let's see the section titles.
matches = re.finditer(r'<h3[^>]*>(.*?)</h3>', content)
categories = []
for m in matches:
    cat_name = m.group(1).strip()
    # Normalize category name for folder
    folder_name = cat_name.lower().replace(' & ', '_').replace(' ', '_').replace('-', '_')
    categories.append({'name': cat_name, 'folder': folder_name, 'start': m.end()})

print(categories)
