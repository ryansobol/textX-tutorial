https://tomassetti.me/quick-domain-specific-languages-in-python-with-textx/

```
brew install python poetry graphviz
git clone <url>
cd <path>
poetry install
poetry run black .
poetry run textx generate turtle.tx --target=dot --overwrite
dot -Tpng -O turtle.dot
open turtle.dot.png
poetry run python main.py
poetry run black .
```
