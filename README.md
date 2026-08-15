# 🚀 DevOps ChatOps Automation Bot

A DevOps-focused Telegram ChatOps bot that allows an administrator to monitor and manage Docker containers directly through Telegram commands.

The project combines **Python, Telegram Bot API, Docker, Docker CLI, and container monitoring** to demonstrate basic DevOps automation and self-healing infrastructure concepts.

---

## 📌 Project Overview

This project provides a Telegram-based interface for managing Docker infrastructure.

Instead of manually checking Docker containers from the terminal, the administrator can send commands through Telegram to:

- Check running containers
- Monitor storage metrics
- Deploy an Nginx container
- View container logs
- Automatically restart a failed container
- Monitor the production container continuously
- Receive infrastructure alerts

The project demonstrates the concept of **ChatOps**, where infrastructure operations are performed through a communication platform.

---

## 🏗️ Architecture

```text
                    Telegram
                       │
                       ▼
              ┌─────────────────┐
              │   ChatOps Bot   │
              │    Python       │
              │  python-telegram-bot
              └────────┬────────┘
                       │
                 Docker CLI
                       │
                 Docker Socket
                       │
              ┌────────▼────────┐
              │ Docker Engine   │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ test-web-server │
              │     Nginx       │
              │    Port 8080    │
              └─────────────────┘
