# Web Development: HTML Fundamentals

This document provides a comprehensive overview of HTML (HyperText Markup Language) based on the lecture slides.

---

## 1. Introduction to the Web and HTML

### Internet vs. Web
- **Internet**: A global network of networks (inter-networking) that supports various services like Email (SMTP/POP), File Transfers (FTP), VoIP, and Mobile Apps.
- **World Wide Web (WWW)**: Just one of the services running over the internet.
- **HTTP**: The protocol used to access web content over the internet (usually via port 80).
- **URL**: Uniform Resource Locator used to identify resources/pages on the web.

### What is HTML?
- **Created by**: Tim Berners-Lee in 1989.
- **Stands for**: HyperText Markup Language.
- **Nature**: It is a **presentational/markup language**, not a programming language (no logic or algorithms).
- **Function**: Defines the structure of web pages and is directly interpreted by the browser.
- **Case Sensitivity**: HTML is **not** case-sensitive.
- **White Space**: Multiple spaces and new lines are ignored by the browser.

---

## 2. Basic Structure of an HTML Page

Every HTML document follows a standard structure:

```html
<!DOCTYPE html> <!-- Document Type Declaration (Standard for HTML5) -->
<html> <!-- Root element -->
<head> <!-- Contains metadata (not visible on page) -->
    <meta charset="UTF-8"> <!-- Specifies character encoding -->
    <title>Page Title</title> <!-- Appears in browser tab -->
</head>
<body> <!-- Contains visible content -->
    <h1>Main Heading</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

### Key Terms:
1.  **Tags**: The keywords surrounded by angle brackets (e.g., `<html>`, `<p>`). Most tags come in pairs: **Opening** (`<tag>`) and **Closing** (`</tag>`).
2.  **Elements**: The complete component from the start tag to the end tag, including content.
3.  **Attributes**: Provide additional information about an element (e.g., `href` in `<a>`, `src` in `<img>`). They are placed inside the opening tag.

---

## 3. Core HTML Elements

### Text Formatting Tags
| Tag | Meaning | Purpose |
| :--- | :--- | :--- |
| `<b>` | Bold | Highlight important information |
| `<strong>` | Strong | Semantic bold (important text) |
| `<i>` | Italic | Denote text |
| `<em>` | Emphasized | Semantic italics (stress) |
| `<mark>` | Marked | Highlight background |
| `<small>` | Small | Shrink text |
| `<strike>` | Strikethrough | Horizontal line through text |
| `<u>` | Underlined | Links or highlights |
| `<ins>` | Inserted | Underlined to show addition |
| `<sub>` | Subscript | Stylistic choice |
| `<sup>` | Superscript | Stylistic choice |

### Headings
- Ranges from `<h1>` (most important) to `<h6>` (least important).
- Search engines use these to decipher page structure.

### Lists
- **Unordered List (`<ul>`)**: Uses bullets. List items are defined with `<li>`.
  - Types: `disc`, `circle`, `square`.
- **Ordered List (`<ol>`)**: Uses numbers/letters. List items are defined with `<li>`.
  - Types: `1`, `A`, `a`, `I`, `i`.
  - Attributes: `start`, `reversed`, `value` (to change sequence mid-list).

---

## 4. Hyperlinks and Navigation

Links are created using the anchor tag `<a>`.

- **Internal Links**: Link to pages within the same website (relative paths, e.g., `<a href="contact.html">`).
- **External Links**: Link to different websites (absolute paths, e.g., `<a href="https://google.com">`).
- **Attributes**:
    - `target="_blank"`: Opens the link in a new tab.
- **Smooth Scrolling**: Can be achieved via CSS: `html { scroll-behavior: smooth; }`.

---

## 5. Media: Images, Audio, and Video

### Images (`<img>`)
- An empty tag (no closing tag).
- **Required Attributes**:
    - `src`: Path to the image.
    - `alt`: Alternate text for accessibility and broken links.
- **Image Maps**: Used to create multiple clickable "hotspots" on a single image.
    - Uses `<map>` and `<area>` tags.

### Video (`<video>`)
- Introduced in HTML5.
- Attributes: `controls`, `autoplay`, `muted`, `loop`, `width`, `height`.
```html
<video controls>
    <source src="movie.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
```

### Audio (`<audio>`)
- Introduced in HTML5.
- Attributes: `controls`, `autoplay`, `muted`, `loop`.

---

## 6. Tables

Tables display data in a grid (rows and columns).

- **Structure**:
    - `<table>`: Wraps the table.
    - `<caption>`: Adds a title to the table.
    - `<tr>`: Table Row.
    - `<th>`: Table Header (centered and bold by default).
    - `<td>`: Table Data (cell).
- **Attributes**:
    - `rowspan`: Span a cell across multiple rows.
    - `colspan`: Span a cell across multiple columns.
    - Layout attributes (legacy): `border`, `align`, `bgcolor`, `cellpadding`.

---

## 7. Forms

Forms are used to submit user data to a server.

- **Attributes**:
    - `action`: Backend URL that processes the data.
    - `method`: `GET` (data in URL) or `POST` (data in body).
- **Input Types**:
    - `type="text"` / `password` / `hidden` / `file`.
    - `type="checkbox"` / `radio` (for selections).
    - `type="submit"` / `reset`.
    - `<textarea>`: Multi-line text.
    - `<select>`: Dropdown list.
- **HTML5 Enhancements**:
    - New types: `email`, `date`, `number`, `color`.
    - Attributes: `required`, `placeholder`, `pattern` (regex), `disabled`, `readonly`, `autocomplete`.

---

## 8. Semantic HTML

Semantic HTML refers to using tags that describe their **meaning/purpose** rather than just their appearance.

### Benefits:
- Accessibility (screen readers).
- SEO (search engine optimization).
- Easier maintenance.

### Block vs. Inline:
- **Block-level**: Starts on a new line, takes full width (e.g., `<div>`, `<h1>`, `<p>`, `<section>`).
- **Inline-level**: Does not start on a new line, only takes necessary width (e.g., `<span>`, `<a>`, `<img>`).

### Structure Elements (HTML5):
- `<header>`: Top section.
- `<nav>`: Navigation links.
- `<main>`: Central content of the document.
- `<section>`: Specific thematic sections.
- `<article>`: Independent/self-contained content.
- `<aside>`: Sidebar or secondary content.
- `<footer>`: Bottom section (copyright, etc.).

---

## 9. Special Characters and Comments

- **Special Characters**: Use entities for symbols not on the keyboard.
  - `&nbsp;`: Non-breaking space.
  - `&copy;`: Copyright sign.
  - `&euro;`: Euro sign.
  - `&gt;`: Greater than sign.
- **Comments**: Used to explain code. They are not visible to the user.
  - Syntax: `<!-- This is a comment -->`
