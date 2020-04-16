```
brew install python poetry graphviz
git clone <url>
cd <path>
poetry install
poetry run textx generate turtle.tx --target=dot --overwrite
dot -Tpng -O turtle.dot
open turtle.dot.png
```
