        
import os
import sys
import ipynbname
import json
import re
from IPython.lib import clipboard
from IPython.core.magic import Magics, magics_class, line_magic

@magics_class
class MyMagics(Magics):
    
    @line_magic
    def replace_content(self, line):
        self.shell.set_next_input(line, replace=True)
        
ip = get_ipython()
ip.register_magics(MyMagics)

def cite(cb=None):
    if cb is None:
        cb = clipboard.osx_clipboard_get()
    bibtex_entries = re.findall(r'\@[^\@]+', cb)
    cite_list = []
    for i, entry in enumerate(bibtex_entries):

        match = re.search(r'@\w+{([^,]+).*year = {(\d+)}.*title = {{(.*)}}.*author = {([^,]+)', entry, re.DOTALL)
        if match:
            url, year, title, author = match.groups()
            if len(bibtex_entries) == 1:
                cite_list.append(f'[({author} {year})](https://doi.org/{url} "{author} et al.\n{year}\n{title}\nDOI:{url}")')
            else:
                if i == 0:
                    cite_list.append(f'[({author} {year},](https://doi.org/{url} "{author} et al.\n{year}\n{title}\nDOI:{url}")')
                elif i+1 == len(bibtex_entries):
                    cite_list.append(f'[{author} {year})](https://doi.org/{url} "{author} et al.\n{year}\n{title}\nDOI:{url}")')
                else:
                    cite_list.append(f'[{author} {year},](https://doi.org/{url} "{author} et al.\n{year}\n{title}\nDOI:{url}")')
    content = ' '.join(cite_list)
    if content:
        get_ipython().run_line_magic('replace_content', f"{content}") 
    else:
        print('clipboard is not bibtex:', cb)
        
def incite(cb=None):
    if cb is None:
        cb = clipboard.osx_clipboard_get()
    bibtex_entries = re.findall(r'\@[^\@]+', cb)
    if len(bibtex_entries) > 1:
        print('clipboard has bibtex entries:', cb)
    else:
        match = re.search(r'@\w+{([^,]+).*year = {(\d+)}.*title = {{(.*)}}.*author = {([^,]+)',
            cb, re.DOTALL)
        if match:
            ref_list = {}
            url, year, title, author = match.groups()
            content = f'{author} et al. [({year})](https://doi.org/{url} "{author} et al.\n{year}\n{title}\nDOI:{url}")'
            get_ipython().run_line_magic('replace_content', f"{content}") 
        else:
            print('clipboard is not bibtex:', cb)
        

def ref_format_callback(i, ref):
    return f"{i}. {ref['author']}, {ref['year']}, _{ref['title']}_, [{ref['doi']}](https://doi.org/{ref['doi'].replace('DOI:', '')})"

def reflist(file_base_name=None, format_fun=ref_format_callback):
    regex = re.compile(r'\d+\s+"([^"]+)"')
    references = {}
    if file_base_name is None:
        file_base_name = ipynbname.name()
    if type(file_base_name) is not list:
        file_base_names = [file_base_name]
    else:
        file_base_names = file_base_name
    for name in file_base_names:
        with open(os.path.abspath(name+'.ipynb')) as f:
            notebook_json = json.load(f)
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'markdown':
                source = ''.join(cell['source'])
                for ref in regex.findall(source):
                    try:
                        author, year, title, doi = ref.split('\n')
                        references[ref] = dict(author=author.strip(),
                                            year=year.strip(), 
                                            title=title.strip(),
                                            doi=doi.strip())
                    except ValueError:
                        print(f'Skipping invalid ref: {ref}', file=sys.stderr)

    lst = []
    for i, (key, ref) in enumerate(sorted(references.items())):
        lst.append(format_fun(i+1, ref))
    content = "\n".join(lst)
    content = '## References\n\n' + content
    get_ipython().run_line_magic('replace_content', f"{content}") 
            
    