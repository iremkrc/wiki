# wiki
An online encyclopedia website like wikipedia.

**[Youtube Demo](https://youtu.be/xC1Yeg8TmPQ) of the project.**

## Features:
- Search for pages
- Add a new page
- Get a random page
- Edit an existing page

![image](https://user-images.githubusercontent.com/66200657/161732720-898e4694-8551-4c38-a457-e746b2de2761.png)


### Search for pages
You can search for pages using the search box. If your searched word exactly matches with an article page in the encyclopedia, the page directly opens. 
Otherwise, you see a results page that shows article names that contain your searched word.

### Edit existing pages or add a new page
You can add pages with the Add New Page button on the left, edit existing pages with Edit Page button found on the article page. 
In the text box you are expected to write in Markdown format.

### Get a random page
Random Page button gets you a random article from existing pages.


## Run wiki locally

### Step 1: clone the project
    git clone https://github.com/iremkrc/search.git
    cd wiki
    
### Step 2: install needed packages if they are not exist
    sudo apt install pip
    pip install django
    pip install django-markdown2
    
### Step 3: run the project
    python3 manage.py runserver
