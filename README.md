#SliqueHTML

Python library that lets you generate HTML using DOM-like objects. 

##Purpose

Prototyping HTML typically requires frequest, manual modification of HTML 
markup, which cause the following tasks to be very time-consuming and 
error prone: 

*   keeping track of closing tags 
*   generating diffirent flavors of similar HTML for for comparison
*   propogating changes to all relevant templates

SliqueHTML generates valid HTML, uses inheritance to allow related DOM objects
to reuse code, and inherently makes propogating UI tweaks through code reuse
and the use of objects. 

SliqueHTML can be either used by designers-that-code to generate templates and 
comps, or by developers in production.

##How to use SliqueHTML

Once the SliqueHTML _src_ folder is on the path, import the _new_ object:

    from slique.html.html import new

You can use the _new_ object to generate _element_ objects, that act much like
DOM elements. 

    new_anchor = new.a(href="http://bab.as")    # returns an element object
    
    # <a href="http://bab.as"></a>

You can modify _element_ objects several ways:

    new_anchor.add('Personal Homepage')         # string escaped
    new_anchor.set(id="homepage_link")          # sets id
    
    # modifications can be chained
    # new_anchor.add('Personal Homepage').add(id='homepage_link')
    
    # <a href="http://bab.as" id="homepage_link">Personal Homepage</a>
    
Some attributes are special. For example, _class_ is a python keyword, so using
the _set_ method would not work, so instead you can either:

    new_anchor.set(cls="new_class") # setting
    # or
    new_anchor.addClass("new_class") # appending
    # <a href="http://bab.as" id="homepage_link" class="new_class">Personal Homepage</a>
    
Look at the [element object definition](https://github.com/ctoscano/SliqueHTML/blob/master/src/slique/html/element.py) for more details.

Finally, you can also extend element objects for convenience. Such an extension 
could be as simple as adding helper functions to the table object, or extending 
it further to automatically place added items into a single column. 

See the table object and the VerticleTable object defined [here](https://github.com/ctoscano/SliqueHTML/blob/master/src/slique/html/table.py).

For convenience, there is also another basic type, the [document](https://github.com/ctoscano/SliqueHTML/blob/master/src/slique/html/document.py) type. It can be 
used as a shell containing the doctype, as well as the html, head, and body 
tags. 

An example of the document inheritance in use can be found [here](https://github.com/ctoscano/pluma/blob/master/pysrc/pluma/views/pages/__init__.py) and [here](https://github.com/ctoscano/pluma/blob/master/pysrc/pluma/views/pages/inbox.py). 


SliqueHTML is a work in progress. We are doing what we can to make it an 
efficient, effective, and pleasant way to generate HTML. Please let me know if 
you have any comments, complaints, or suggestions we can use to make it better; 
or better yet, please share your improvements.

Sincerely,
Cesar Toscano 
 

##Security

SliqueHTML by default escapes all string inputs, including element attributes. 
Raw HTML can be added by using an element's _addHTML_ method. 

