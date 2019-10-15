#!/bin/bash
# directories
mkdir environments
mkdir -p app/main/controllers
mkdir -p app/main/models
mkdir -p app/test
touch app/__init__.py
touch app/main/__init__.py
touch app/main/controllers/__init__.py
touch app/main/models/__init__.py
touch app/test/__init__.py
touch environments/requirements
# shell script files
echo "#!/bin/bash
pip3 install -r environments/requirements
pip3 freeze > environments/requirements" > environments/install-packages.sh
echo "#!/bin/bash
virtualenv -p python3.7 .venv
source .venv/bin/activate
pip3 install -r environments/requirements" > environments/init.sh
# python script files
echo "" > run.py
# .gitignore
echo "# Environments
.venv
.idea

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# C extensions
*.so

# Distribution / packaging
bin/
build/
develop-eggs/
dist/
eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
.tox/
.coverage
.cache
nosetests.xml
coverage.xml

# Translations
*.mo

# Mr Developer
.mr.developer.cfg
.project
.pydevproject

# Rope
.ropeproject

# Django stuff:
*.log
*.pot

# Sphinx documentation
docs/_build/"> .gitignore
# Run init script
source environments/init.sh
pip3 install flask
# git init
git init
git add .
git commit --allow-empty -m"Initial commit"
echo "Falsk Initailize Complete"
