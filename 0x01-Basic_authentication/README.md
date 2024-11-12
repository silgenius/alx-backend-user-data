# 0x01 - Basic Authentication

## Project Overview

This project demonstrates the implementation of basic authentication for a web application using Python and Flask. The main objective is to securely authenticate users using HTTP Basic Authentication and protect specific resources on the server.

## Technologies Used

- Python 3
- Flask
- HTTP Basic Authentication

## Project Description

In this project, we will:

- Create a simple Flask application.
- Implement basic authentication using Python's `base64` module.
- Secure an endpoint with basic authentication and return appropriate responses based on authentication success or failure.

### Requirements

- Python 3.x
- Flask (`pip install Flask`)

## Features

- **Basic Authentication**: The app uses a username and password sent via HTTP headers to authenticate users.
- **Protected Endpoint**: An endpoint (`/`) that requires authentication to access. If the user is not authenticated, they will receive a `401 Unauthorized` status.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/0x01-Basic_authentication.git

