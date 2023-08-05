
from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.23'
DESCRIPTION = 'Use customized GUI'
LONG_DESCRIPTION = '''A package that allows you to use styles and widget of super level in tkinter like
class EntryBtns:
    def __init__(self, parent, saved_data_holder, entry_tags, entry_fr_height = h(50),
                        entry_fr_side = TOP, fill = X, widget_2_create = 'entry'
                        , browse = False, ent_id_width = 5, default = None):
        
        self.saved_data_holder = saved_data_holder
        self.entry_tags = entry_tags
        self.entry_fr_height = entry_fr_height
        self.entry_fr_side = entry_fr_side
        self.widget_2_create = widget_2_create
        self.default = default

        self.fr = frame(master = parent)
        self.fr.pack(side=entry_fr_side, fill=fill, padx = w(2), expand = True)
        
        if widget_2_create == 'entry':
            self.ent = entry(self.fr, fg="gray50", default=default)
            self.ent.pack(side=LEFT, fill=X, ipadx=w(40), expand = True, pady = h(2))

        elif widget_2_create == 'text':
            self.ent = Textb(self.fr, default=default, height = h(4))
            self.ent.pack(padx = w(1), pady=h(1), side = LEFT, expand = True, fill = X)
                

        self.ent_id = entry(self.fr, width = ent_id_width)
        self.ent_id.pack(side=LEFT, padx = w(2), pady = h(2))'''

# Setting up
setup(
    name="irene_pro",
    version=VERSION,
    author="Irene coldsober",
    author_email="<irene.study.2023@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["pywin32", "opencv-python", "pyperclip", "tkcalendar", "ttkthemes"],
    keywords=['tkinter', 'widget', 'gui'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)