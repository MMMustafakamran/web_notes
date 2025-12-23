# LECTURE #5: React Router, HOCs, Axios & More

## 1. Recap & Virtual DOM

- **App.js** – Container component.
- **ninjas** – Data passed as props.
- **Ninjas.js** – UI component.
- **addNinja** – Function to add ninjas.
- **AddNinja.js** – Container component.

**Virtual DOM Flow:**

- JSX templates generate a new Virtual DOM.
- This is compared with the current Virtual DOM.
- Differences are updated in the actual DOM (Browser).

---

## 2. React Router

### How it Works:

1. Initial request to `/home` is sent to the server.
2. Server returns `index.html`.
3. React Router renders the matching component (e.g., `Home.js`).

### Example Setup:

**Home.js:**

```jsx
import React from "react";

const Home = () => {
  return (
    <div className="container">
      <h4 className="center">Home</h4>
      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit...</p>
    </div>
  );
};

export default Home;
```

**About.js:**

```jsx
import React from "react";

const About = () => {
  return (
    <div className="container">
      <h4 className="center">About</h4>
      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit...</p>
    </div>
  );
};

export default About;
```

**Contact.js:**

```jsx
import React from "react";

const Contact = () => {
  return (
    <div className="container">
      <h4 className="center">Contact</h4>
      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit...</p>
    </div>
  );
};

export default Contact;
```

**Navbar.js (with anchor tags):**

```jsx
import React from "react";

const Navbar = () => {
  return (
    <nav className="nav-wrapper red darken-3">
      <div className="container">
        <a className="brand-logo">PokeTimes</a>
        <ul className="right">
          <li>
            <a href="/">Home</a>
          </li>
          <li>
            <a href="/about">About</a>
          </li>
          <li>
            <a href="/contact">Contact</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
```

**App.js (Basic Routing):**

```jsx
import React, { Component } from "react";
import Navbar from "./components/Navbar";
import { BrowserRouter, Route } from "react-router-dom";
import Home from "./components/Home";
import Contact from "./components/Contact";
import About from "./components/About";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar />
          <Route path="/" component={Home} />
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
```

**Issue:** Without `exact`, `/about` also matches `/` and shows both components.

**Fix:** Use `exact` for the home route:

```jsx
<Route exact path="/" component={Home} />
```

---

## 3. Links & NavLinks

Replace `<a href="...">` with `<Link to="...">` or `<NavLink to="...">` to prevent page reloads.  
**NavLink** adds an `active` class automatically.

**Navbar.js (with React Router links):**

```jsx
import React from "react";
import { Link, NavLink } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="nav-wrapper red darken-3">
      <div className="container">
        <a className="brand-logo">PokeTimes</a>
        <ul className="right">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <NavLink to="/about">About</NavLink>
          </li>
          <li>
            <NavLink to="/contact">Contact</NavLink>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
```

---

## 4. Programmatic Redirects

Use `props.history.push('/path')` to redirect from inside a component.

**Example (Contact.js redirects after 2 seconds):**

```jsx
import React from "react";

const Contact = (props) => {
  setTimeout(() => {
    props.history.push("/about");
  }, 2000);
  return (
    <div className="container">
      <h4 className="center">Contact</h4>
      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit...</p>
    </div>
  );
};

export default Contact;
```

**Note:** `props.history` is available in components rendered by `<Route>`.  
For other components (e.g., Navbar), wrap with `withRouter`:

```jsx
import { withRouter } from "react-router-dom";
export default withRouter(Navbar);
```

---

## 5. Higher Order Components (HOCs)

A HOC is a function that takes a component and returns a new enhanced component.

**Example (Rainbow HOC):**

```jsx
const Rainbow = (WrappedComponent) => {
  const colours = ["red", "pink", "orange", "blue", "green", "yellow"];
  const randomColour = colours[Math.floor(Math.random() * 5)];
  const className = randomColour + "-text";

  return (props) => {
    return (
      <div className={className}>
        <WrappedComponent {...props} />
      </div>
    );
  };
};

export default Rainbow;
```

**Usage:**

```jsx
import Rainbow from "./Rainbow";
export default Rainbow(About);
```

---

## 6. Using Axios for Data Fetching

Axios is used to make HTTP requests (e.g., from REST APIs).

**Example (Fetching posts in Home.js):**

```jsx
import React, { Component } from "react";
import axios from "axios";

class Home extends Component {
  state = {
    posts: [],
  };

  componentDidMount() {
    axios.get("https://jsonplaceholder.typicode.com/posts").then((res) => {
      this.setState({
        posts: res.data.slice(0, 10),
      });
    });
  }

  render() {
    const { posts } = this.state;
    const postList = posts.length ? (
      posts.map((post) => {
        return (
          <div className="post card" key={post.id}>
            <div className="card-content">
              <span className="card-title">{post.title}</span>
              <p>{post.body}</p>
            </div>
          </div>
        );
      })
    ) : (
      <div className="center">No posts yet</div>
    );

    return (
      <div className="container">
        <h4 className="center">Home</h4>
        {postList}
      </div>
    );
  }
}

export default Home;
```

---

## 7. Route Parameters

Route parameters are dynamic parts of the URL (e.g., `/post/:post_id`).

**App.js (adding a route with a parameter):**

```jsx
<Route path="/post/:post_id" component={Post} />
```

**Post.js (accessing the parameter):**

```jsx
import React, { Component } from "react";
import axios from "axios";

class Post extends Component {
  state = {
    post: null,
  };

  componentDidMount() {
    let id = this.props.match.params.post_id;
    axios
      .get("https://jsonplaceholder.typicode.com/posts/" + id)
      .then((res) => {
        this.setState({
          post: res.data,
        });
      });
  }

  render() {
    const post = this.state.post ? (
      <div className="container">
        <h4>{this.state.post.title}</h4>
        <p>{this.state.post.body}</p>
      </div>
    ) : (
      <div className="center">Loading post...</div>
    );

    return post;
  }
}

export default Post;
```

---

## 8. Switch Tag

`<Switch>` ensures only the first matching route is rendered.

**App.js (using Switch):**

```jsx
import { BrowserRouter, Route, Switch } from "react-router-dom";

<BrowserRouter>
  <div className="App">
    <Navbar />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/about" component={About} />
      <Route path="/contact" component={Contact} />
      <Route path="/post/:post_id" component={Post} />
    </Switch>
  </div>
</BrowserRouter>;
```

---

## 9. Importing Images

Images can be imported and used in components.

**Example (Adding a Pokeball image in Home.js):**

```jsx
import Pokeball from "./pokeball.png";

// Inside the map function:
<img src={Pokeball} alt="A pokeball" />;
```

**Enhanced Home.js with links to posts:**

```jsx
import { Link } from "react-router-dom";

posts.map((post) => {
  return (
    <div className="post card" key={post.id}>
      <img src={Pokeball} alt="A pokeball" />
      <div className="card-content">
        <Link to={"/post/" + post.id}>
          <span className="card-title">{post.title}</span>
        </Link>
        <p>{post.body}</p>
      </div>
    </div>
  );
});
```
