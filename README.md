# Home page for your web browser

### Description

This page offers a set of links to your favorite web applications.

### Overview

It is generated by a Python script rendering the template file *index.html.jinja*. The diplayed icons are configured in the configuration file *icons.ini* and the images have to be provided beforehands in directory *pictograms/*. The style is defined in the file *styles.css* and the responsive design is managed by a library in the git submodule [*jquery.mosaicflow*](https://github.com/sapegin/jquery.mosaicflow).

### Usage

Clone the repository, render the page and open *index.html* in your favorite web browser.

    $ git clone https://github.com/odeblic/homepage.git
    $ cd homepage
    $ git submodule init
    $ git submodule update
    $ python render_page.py

