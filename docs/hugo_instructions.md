# Hugo instructions

## [Page bundles](https://gohugo.io/content-management/organization/#page-bundles)

### Folders schema
```
. // root
└── content
    └── about
    |   └── index.md  // <- https://example.com/about/
    ├── posts
    |   ├── firstpost.md   // <- https://example.com/posts/firstpost/
    |   ├── happy
    |   |   └── ness.md  // <- https://example.com/posts/happy/ness/
    |   └── secondpost.md  // <- https://example.com/posts/secondpost/
    └── quote
        ├── first.md       // <- https://example.com/quote/first/
        └── second.md      // <- https://example.com/quote/second/
```

## [_index.md](https://gohugo.io/content-management/organization/#index-pages-_indexmd)
It allows you to add front matter and content to your list templates.

Example `_index.md` file:
```
---
title: My Go Journey
date: 2017-03-23
publishdate: 2017-03-24
---

I decided to start learning Go in March 2017.

Follow my journey through this new blog.
```
Then this can be used on [_templates_](#Templates)

Example of template:
```html
{{ define "main" }}
<main>
    <article>
        <header>
            <h1>{{.Title}}</h1>
        </header>
        <!-- "{{.Content}}" pulls from the markdown content of the corresponding _index.md -->
        {{.Content}}
    </article>
    <ul>
    <!-- Ranges through content/posts/*.md -->
    {{ range .Pages }}
        <li>
            <a href="{{.Permalink}}">{{.Date.Format "2006-01-02"}} | {{.Title}}</a>
        </li>
    {{ end }}
    </ul>
</main>
{{ end }}
```
Output will be:
```html
<!--top of your baseof code-->
<main>
    <article>
        <header>
            <h1>My Go Journey</h1>
        </header>
        <p>I decided to start learning Go in March 2017.</p>
        <p>Follow my journey through this new blog.</p>
    </article>
    <ul>
        <li><a href="/posts/post-01/">Post 1</a></li>
        <li><a href="/posts/post-02/">Post 2</a></li>
    </ul>
</main>
<!--bottom of your baseof-->
```

## [Templates](https://gohugo.io/templates/introduction/)

### [Variables](https://gohugo.io/templates/introduction/#variables)
Scoped variables with `.`
```html
<title>{{ .Title }}</title>
<!-- {{ .Title }} will be replaced with 'Title' variable from _index.md -->
```
Custom variables with `$`
```
{{ $address := "123 Main St." }}
{{ $address }}
```
Other operations
```
{{ $var := "Hugo Page" }} // set variable
{{ if .IsHome }} // conditional
    {{ $var = "Hugo Home" }} // reset variable
{{ end }}
Var is {{ $var }} // show variable value
```

### [Functions](https://gohugo.io/templates/introduction/#functions)
Adding numbers
```
{{ add 1 2 }}
<!-- prints 3 -->
```
Comparing numbers
```
{{ lt 1 2 }}
<!-- prints true (i.e., since 1 is less than 2) -->
```

### [Partials](https://gohugo.io/templates/introduction/#partial)
The partial function is used to include partial templates using the syntax
`{{ partial "<PATH>/<PARTIAL>.<EXTENSION>" . }}.`

Example of including a layouts/partials/header.html partial:
```
{{ partial "header.html" . }}
```

## [Logic](https://gohugo.io/templates/introduction/#logic)

### [Iteration](https://gohugo.io/templates/introduction/#iteration)
Using context `.`
```
{{ range $array }}
    {{ . }} <!-- The . represents an element in $array -->
{{ end }}
```
Declaring a variable name for an array element’s value
```
{{ range $elem_val := $array }}
    {{ $elem_val }}
{{ end }}
```
Declaring variable names for an array element’s index and value
```
{{ range $elem_index, $elem_val := $array }}
   {{ $elem_index }} -- {{ $elem_val }}
{{ end }}
```
Declaring variable names for a map element’s key and value
```
{{ range $elem_key, $elem_val := $map }}
   {{ $elem_key }} -- {{ $elem_val }}
{{ end }}
```
Conditional on empty map, array, or slice.
```
{{ range $array }}
    {{ . }}
{{else}}
    <!-- This is only evaluated if $array is empty -->
{{ end }}
```

### [Conditionals](https://gohugo.io/templates/introduction/#conditionals)

`with`
It is common to write “if something exists, do this” kind of statements using `with`.

It skips the block if the variable is absent, or if it evaluates to “false” as explained above.
```
{{ with .Params.title }}
    <h4>{{ . }}</h4>
{{ end }}
```

`with .. else`

```
{{ with .Param "description" }}
    {{ . }}
{{ else }}
    {{ .Summary }}
{{ end }}
```

`if`

```
{{ if isset .Params "title" }}
    <h4>{{ index .Params "title" }}</h4>
{{ end }}
```
```
{{ if (isset .Params "description") }}
    {{ index .Params "description" }}
{{ else }}
    {{ .Summary }}
{{ end }}
```
```
{{ if (isset .Params "description") }}
    {{ index .Params "description" }}
{{ else if (isset .Params "summary") }}
    {{ index .Params "summary" }}
{{ else }}
    {{ .Summary }}
{{ end }}
```
```
{{ if (and (or (isset .Params "title") (isset .Params "caption")) (isset .Params "attr")) }}
```

