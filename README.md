# JeongBeom Baek (Eric) — Personal Website & Portfolio

Welcome to the source code for my personal website and portfolio, hosted on GitHub Pages. This site serves as a central hub for my academic activities, independent research projects (like **J.A.R.V.I.S.**), and technical skills.

## 🌐 Live Website

[ericbaek0828-netizen.github.io/github.io](https://ericbaek0828-netizen.github.io/github.io)

## 🏗️ Architecture & Theme

This site is built using [Jekyll](https://jekyllrb.com/) and is heavily customized from the [al-folio](https://github.com/alshedivat/al-folio) theme, tailored for academic and developer portfolios.

- **`_pages/`**: Contains core routing pages (e.g., `about.md`, `research.md`, `skills.md`).
- **`_projects/`**: Markdown files documenting individual projects and research notes.
- **`_posts/`**: Blog entries and technical notes.

## 🚀 Local Development

You can run this site locally using Docker to ensure a consistent environment without needing to install Ruby or Jekyll directly on your host machine.

### Running via Docker

```bash
# Start the container
docker compose up -d

# The site will be available at http://127.0.0.1:8080/github.io/
# (The path is determined by the `baseurl` in _config.yml)

# View logs
docker compose logs -f

# Stop the container
docker compose down
```

## 🤖 AI Agent Integration

This repository is configured as an AI-friendly workspace, integrating multi-agent orchestration files:

- **`.agents/skills/`**: Contains workflow skills and instructions for autonomous AI orchestration.
- **`.claude/` & `.gemini/`**: Environment configurations and context constraints for Claude and Gemini developer agents.
- **`AGENTS.md` & `CLAUDE.md`**: Core rule sets, boundaries, and working agreements for AI interactions within this codebase.

## 📜 Deployment

This repository is automatically deployed using **GitHub Pages**. Pushing to the `main` branch triggers a GitHub Actions workflow that builds the Jekyll site and deploys it.

## 📄 License

This repository is based on the `al-folio` theme which is open-sourced under the MIT License.
