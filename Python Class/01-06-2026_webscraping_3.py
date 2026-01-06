from bs4 import BeautifulSoup
html_doc = """<html>

	<head> <title> Title example </title> </head>
	
	
	<body>

		<h1> Main title </h1>
		<h2> Second title </h2>
		<h3> Third title </h3>
		<p> This is the first paragraph </p>
		<p> This is the second paragraph </p>
		<a href="https://www.makerfaire.com"> Click here </a>
	
	
	</body>



</html>
"""

soup = BeautifulSoup(html_doc , 'html.parser')
print(soup.prettify())

# title
print(soup.title)
# just the title
print(soup.title.name)
# title string
print(soup.title.string)

