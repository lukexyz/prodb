# Prodb 
> .csv database for pros


<p align="center">
  <img src="https://github.com/lukexyz/prodb/blob/master/img/prodb.png?raw=true">
</p>

#### 🌐 Demo
> 🔗 https://share.streamlit.io/lukexyz/prodb/app.py
#### 📝 Documentation
> 🔗 https://lukexyz.github.io/prodb/ (github pages)

## Setup environment and `nbdev`
First time only:

* Ubuntu / WSL
```
conda create -n prodb python=3.9 jupyter pip nbdev twine
conda activate prodb  
git clone https://github.com/lukexyz/prodb.git  
pip install -r requirements.txt  
```
  
  
* Install githooks from project folder  
```
nbdev_install_git_hooks
```

* Package auto-manager
```
make release
```
WSL error work around for: [Errno 16] Device or resource busy
```
 ubuntu $ make release
windows > python setup.py sdist bdist_wheel
 ubuntu $ twine upload --repository pypi dist/*
```


Frequently during develoment:  
### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_build_lib` 


### 2. 📝 **Build docs** from notebooks  
> `nbdev_build_docs` 

## Install

`pip install prodb`
