# Markdown to HTML
* Markdown is awesome! All your README.md are made in Markdown, but do you know how Github are rendering them? It’s time to code a Markdown to HTML!

### Tasks

#### 0. Start a script #advanced
Write a script markdown2html.py that takes an argument 2 strings:

* First argument is the name of the Markdown file
* Second argument is the output file name

#### 1. Headings #advanced
Improve markdown2html.py by parsing Headings Markdown syntax for generating HTML:

| Markdown          | HTML generated           |
| :---------------- | :---------------------- |
| # Heading level 1 | `<h1>`Heading level 1`</h1>` |
| ## Heading level 2 | `<h2>`Heading level 2`</h2>` |
| ### Heading level 3 | `<h3>`Heading level 3`</h3>` |
| #### Heading level 4 | `<h4>`Heading level 4`</h4>` |
| ##### Heading level 5 | `<h5>`Heading level 5`</h5>` |
| ###### Heading level 6 | `<h6>`Heading level 6`</h6>` |

#### 2. Unordered listing #advanced
Improve markdown2html.py by parsing Unordered listing syntax for generating HTML

Markdown: 
```
- Hello
- Bye
```
HTML Generated: 
```
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>
```
```
guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
guillaume@vagrant:~/$
```

#### 3. Ordered listing #advanced
Improve markdown2html.py by parsing Ordered listing syntax for generating HTML:

Markdown: 
```
* Hello
* Bye
```
HTML Generated: 
```
<ol>
    <li>Hello</li>
    <li>Bye</li>
</ol>
```
```
guillaume@vagrant:~/$ cat README.md
# My title
* Hello
* Bye

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ol>
<li>Hello</li>
<li>Bye</li>
</ol>
guillaume@vagrant:~/$
```

#### 4. Simple text #advanced
Improve markdown2html.py by parsing paragraph syntax for generating HTML:

Markdown: 
```
Hello

I'm a text
with 2 lines
```
HTML Generated: 
```
<p>
    Hello
</p>
<p>
    I'm a text
        <br />
    with 2 lines
</p>
```
```
guillaume@vagrant:~/$ cat README.md
# My title
- Hello
- Bye

Hello

I'm a text
with 2 lines

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>Hello</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm a text
<br/>
with 2 lines
</p>
guillaume@vagrant:~/$ 
```

#### 5. Bold and emphasis text #advanced
Improve markdown2html.py by parsing bold syntax for generating HTML:

| Markdown    | HTML generated |
| :---------- | :------------- |
| `**Hello**` | `<b>Hello</b>` |
| `__Hello__` | `<em>Hello</em>` |
```
guillaume@vagrant:~/$ cat README.md
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

**Or in bold**

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<ul>
<li>He<b>l</b>lo</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm <b>a</b> text
<br/>
with <em>2 lines</em>
</p>
<p>
<b>Or in bold</b>
</p>
guillaume@vagrant:~/$ 
```
