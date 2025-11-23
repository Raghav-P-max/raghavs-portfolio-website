## FLASK MODULE

Using flask module, we import Flask, render_template, url_for and redirect classes.
Then, we create an object using Flask class called 'app'.

## MAIN ROUTES

Using @app.route(), we define a url path to visit each html page.

The /index code loads and shows the 'index.html' page. 
The /about code loads and shows the 'about.html' page.
The /form code loads and shows the 'form.html' page which asks the user to input his details such as first name, last name and occupation.

## BACKUP ROUTES

We can also create a backup route to display a error message in case the user adds an extension to the website different than the '/index','/about' or '/form' page.
For example, if we add extension -'/raghav', it displays an error message saying :"Hello there! you have entered /raghav at the end of url. Kindly enter only /about or /index at the end if you want to know more about me!

## OUTPUT OF THE ROUTES

Click here to see output for '/index' extension : http://127.0.0.1:5000/index
Click here to see output for '/about' extension : http://127.0.0.1:5000/about
Click here to see output for '/form' extension : http://127.0.0.1:5000/form
Click here to see output for '/raghav' extension : http://127.0.0.1:5000/raghav

