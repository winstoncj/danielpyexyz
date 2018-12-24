import sys
import os
from datetime import datetime

TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day}
Tags:
Category:
Slug: {slug}
Summary:
"""

def create_post(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    directory = f'content/{today.year}'
    if not os.path.exists(directory):
        os.mkdir(directory)
    f_create = f'{directory}/{slug}.md'
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
        print('File created --> ' + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        create_post(sys.argv[1])
    else:
        print("No title given")
