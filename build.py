from os import listdir
import jinja2
import markdown


def build(mdfile):
    '''
    adapted from https://gist.github.com/jiffyclub/5015986
    added highlight.js to support code
    ```python
    print(1)
    ```
    '''
    TEMPLATE = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/atelier-forest-light.min.css">
        <style>
            blockquote{
                background-color: #f8ffba;
                border-left: 5px solid #dde68f;
                margin: 20px;
                padding: 10px;
            }
        </style>
    </head>
    <body>
    <div class="container">
    <a href="index.html">Home</a> | <a href="https://github.com/Abdur-rahmaanJ/pyfaq">Edit on Github</a>

    {{content}}

    <a href="index.html">Home</a>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
    </div>
    </body>
    </html>
    """

    name = mdfile[:-3]
    md_file = 'md/{}.md'.format(name)
    html_file = 'docs/{}.html'.format(name)

    with open(md_file, 'r', encoding='utf8') as f:
        md = f.read()

    extensions = ['extra', 'smarty']

    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    doc = jinja2.Template(TEMPLATE).render(content=html)
    with open(html_file, 'w+', encoding='utf8') as f:
        f.write(doc)

def get_all_mdfile():
    return listdir('md/')

def build_all():
    global files
    for mdfile in get_all_mdfile():
        files.append(mdfile[:-3])
        build('{}'.format(mdfile))

def build_index():
    global files
    TEMPLATE = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/atelier-forest-light.min.css">
        <style>

        </style>
    </head>
    <body>

    <div class="container">
    <a href="https://github.com/Abdur-rahmaanJ/pyfaq">Edit on Github</a>
    <br>
    {% for file in files %}
        <a href='{{file}}.html'>{{file.replace('__', '@').replace('_', ' ').replace('@', '__')}}</a><br>
    {% endfor %}
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
    </div>
    </body>
    </html>
    """
    doc = jinja2.Template(TEMPLATE).render(files=files)
    with open('docs/index.html', 'w+', encoding='utf8') as f:
        f.write(doc)

files = []
if __name__ == '__main__':
    build_all()
    build_index()
    print('terminated')