import fastbook
from fastbook import *
from fastai.text.all import *
import pathlib

path = pathlib.Path('D:\Dev\repos\examples\word_language_model\data')

files = get_text_files(path)