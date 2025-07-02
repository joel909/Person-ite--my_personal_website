# Person-ite – My Personal Website

Welcome to my personal website built with Flask!  
This project is a showcase of my work, ideas, and ways to connect.  
I'm always happy to see others use, contribute, or fork this repo. If you find it useful or inspiring, let me know!

---

## Table of Contents

- [Project Overview](#project-overview)
- [Flask Routes](#flask-routes)
- [Getting Started](#getting-started)
- [Containerized Deployment (Preferred!)](#containerized-deployment-preferred)
- [Running With Gunicorn](#running-with-gunicorn)
- [Running With Flask (Not Preferred)](#running-with-flask-not-preferred)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

This is a minimal, developer-focused Flask web app.  
You’ll find my intro, links to projects, and a little about what I do.

## Flask Routes

The main routes are defined in `api/index.py`:

| Route            | Methods | Description                                   |
|------------------|---------|-----------------------------------------------|
| `/`              | GET     | Homepage. Renders `home.html`                 |
| `/favicon.ico`   | GET     | Serves the favicon                            |
| `/404`           | GET     | Custom 404 error page (`404.html`)            |
| `/insta`         | GET     | Instagram info (see note below)               |

**Note:**  
The `/insta` route does *not* reveal my Instagram. That page explains my personal boundaries about social media.

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/joel909/Person-ite--my_personal_website.git
cd Person-ite--my_personal_website
```

### 2. Install Python & dependencies

- Python 3.8+ recommended
- Install requirements:

```bash
pip install -r requirements.txt
```

---

## Containerized Deployment (Preferred!)

**I highly recommend running this with Docker and Gunicorn for production.**

### 1. Build the Docker image

Create a `Dockerfile` (sample below) if one isn’t present:

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "api.index:app"]
```

### 2. Build and Run

```bash
docker build -t my-personal-site .
docker run -d -p 5000:5000 my-personal-site
```

---

## Running With Gunicorn

If you don’t use Docker, you can still run with Gunicorn for better performance:

```bash
pip install gunicorn
gunicorn -b 0.0.0.0:5000 api.index:app
```

---

## Running With Flask (Not Preferred)

For development or testing only:

```bash
python api/index.py
```

Or:

```bash
export FLASK_APP=api/index.py
flask run --host=0.0.0.0 --port=5000
```

---

## Project Structure

```
.
├── api/
│   ├── index.py          # Flask app and routes
│   └── templates/
│       ├── home.html
│       ├── 404.html
│       └── insta.html
├── static/               # CSS, images, favicon, etc.
├── requirements.txt
└── README.md
```

---

## Contributing

- PRs are welcome!
- If you use this as a template or inspiration, I’d love to see what you build.  
- Suggestions, improvements, and forks are always appreciated.

---

## License

This project is open source under the [MIT License](LICENSE).

---

## Contact

Want to reach out?  
- Email: [me@joeljoby.com](mailto:me@joeljoby.com)
- Or open an issue or discussion on GitHub.

---

**Happy hacking, and thanks for checking out my site!**
