# 0x03. User Authentication Service

This repository contains a basic implementation of a **User Authentication Service**, built with modern web technologies. It allows users to register, log in, and securely authenticate using a variety of methods.

The service is designed to handle common authentication workflows such as:

- **User Registration**: Allows new users to create accounts.
- **User Login**: Allows existing users to log in to their accounts.
- **Password Hashing and Storage**: Ensures user passwords are securely stored.
- **Session Management**: Manages user sessions with JWT (JSON Web Tokens).

---

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [POST /register](#post-register)
  - [POST /login](#post-login)
  - [GET /profile](#get-profile)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## Technologies Used

- **Node.js**: Runtime environment for building the service.
- **Express.js**: Web framework for handling HTTP requests and responses.
- **JWT (JSON Web Tokens)**: Secure method for transmitting authentication tokens.
- **bcrypt**: Password hashing library.
- **MongoDB**: NoSQL database for storing user data.

---

## Features

- **User Registration**: Registers new users by collecting their username, email, and password.
- **User Login**: Authenticates existing users using username/email and password.
- **Password Hashing**: Passwords are hashed using `bcrypt` to prevent plain text storage.
- **JWT Authentication**: Provides secure user authentication with JWT tokens for maintaining sessions.
- **Profile Management**: Users can view and update their profile data after logging in.

---

## Installation

To get started with the User Authentication Service, clone this repository and install the dependencies.

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/0x03-user_authentication_service.git
    cd 0x03-user_authentication_service
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Set up your environment variables in a `.env` file:
    ```env
    MONGO_URI=mongodb://localhost:27017/authentication_service
    JWT_SECRET=your_jwt_secret_key
    ```

4. Start the server:
    ```bash
    npm start
    ```

By default, the service runs on port `3000`.

---

## Usage

Once the service is running, you can use the API endpoints to register, log in, and manage user profiles.

### API Endpoints

#### POST /register

**Description**: Registers a new user with the provided username, email, and password.

**Request Body**:
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "strongPassword123"
}

