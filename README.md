# JeongBeom Baek (Eric) — Personal Website & Portfolio

Welcome to the source code for my personal website and portfolio, hosted on GitHub Pages. This site serves as a central hub for my academic activities, independent research projects (like **J.A.R.V.I.S.**), and technical skills.

## 🌐 Live Website

[ericbaek0828-netizen.github.io/github.io](https://ericbaek0828-netizen.github.io/github.io)

## 🏗️ Architecture & Theme

This site is built using [Jekyll](https://jekyllrb.com/) and is heavily customized from the [al-folio](https://github.com/alshedivat/al-folio) theme, tailored for academic and developer portfolios.

- **`_pages/`**: Contains core routing pages (e.g., `about.md`, `journey.md`, `skills.md`).
- **`_projects/`**: Markdown files documenting individual projects and research notes.
- **`_posts/`**: Blog entries and technical notes.
- **`_news/`**: Short announcements and key events.
- **`_teachings/`**: Mentoring, TA, and lecture-related content.

## 🚀 Local Development

You can run this site locally using either Ruby/Bundler natively, or by utilizing Docker/Devcontainers to ensure a consistent environment.

### 1. Using Ruby & Bundler (Native)

If you have Ruby installed:
```bash
# Install dependencies
bundle install

# Serve the site locally
bundle exec jekyll serve
```

### 2. Using VSCode Devcontainer (Recommended)

This repository includes a `.devcontainer` configuration.
1. Open the repository in VS Code.
2. Install the **Dev Containers** extension.
3. Click "Reopen in Container" when prompted.
4. Once inside the container, run:
```bash
bundle exec jekyll serve
```

### 3. Using Docker Compose

```bash
# Start the container
docker compose up -d

# The site will be available at http://127.0.0.1:8080/github.io/
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
