# Prodb 
> .csv database for pros


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

Frequently during develoment:  
### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_build_lib` 


### 2. 📝 **Build docs** from notebooks  
> `nbdev_build_docs` 

## Install

`pip install prodb`
