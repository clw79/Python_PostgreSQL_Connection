# Python PostgreSQL Jenkins Test Lab

This project is a small home lab testing setup using Python, pytest, Playwright, and PostgreSQL. It validates database connectivity and basic browser automation, with the goal of running the test suite automatically through Jenkins.

## Project Purpose

The purpose of this project is to practice building a simple automated testing workflow that connects multiple real-world tools:

- Python for scripting and test code
- PostgreSQL as the database
- psycopg2 as the Python PostgreSQL driver
- pytest as the test runner
- Playwright for browser automation testing
- Jenkins for continuous integration

This project is part of a larger home lab environment running on Docker and Proxmox.

## Current Environment

The home lab currently includes:

- Proxmox host
- Ubuntu Docker VM
- Jenkins running in Docker with the web UI mapped to a host port
- PostgreSQL running in Docker with the database port available to the test environment

Jenkins is intended to pull this repository, install the required dependencies, and run the test suite automatically.

## Local Port Usage

This project assumes the following services are reachable from the test runner:

| Service | Default Container Port | Purpose |
|---|---:|---|
| PostgreSQL | 5432 | Database connection for pytest |
| Jenkins | 8080 | Jenkins web UI inside the container |

In this home lab, host port mappings may differ depending on what other services are already using those ports. For example, Jenkins may be mapped to a different host port if another container is already using `8080`.

Connection values should be provided through environment variables instead of being hardcoded in the project files.

## Technologies Used

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| pytest | Runs and validates automated tests |
| psycopg2 | Connects Python to PostgreSQL |
| Playwright | Browser automation testing |
| PostgreSQL | Database being tested |
| Jenkins | Runs tests through CI |
| GitHub | Source control repository |



## Project Files

```text
python_postgresql_connection/
│
├── .gitignore
├── README.md
├── requirements.txt
├── pytest.ini
├── test_postgres_connection.py
└── test_playwright_ui.py

