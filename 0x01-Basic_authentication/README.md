# 0x01. Basic Authentication

This repository contains a project that demonstrates the implementation of basic authentication in a web application. It introduces the concept of securing access to an API or a web service using simple authentication mechanisms.

## Project Overview

In this project, you'll learn how to:

- Implement basic HTTP authentication.
- Understand and handle `Authorization` headers in HTTP requests.
- Use `Base64` encoding to transmit authentication credentials securely (though it's not truly secure on its own).
- Set up an API endpoint that requires basic authentication to access.

## Files in the repository

### 1. **`basic_auth.py`**

This file contains the implementation of basic authentication. The `BasicAuth` class implements the `Authorization` header parsing and user verification logic.

### 2. **`app.py`**

The main application file where a basic API is set up using Flask. This includes routes that require basic authentication.

### 3. **`README.md`**

This file, which explains the basic authentication implementation and provides instructions on how to use it.

### 4. **`requirements.txt`**

Contains the list of Python dependencies needed for this project. You can install these dependencies using `pip install -r requirements.txt`.

## Features

- **Basic Authentication:** The implementation expects a `username:password` pair encoded in Base64, sent in the `Authorization` header of an HTTP request.
- **Secure Access:** Requests without the proper credentials or with invalid credentials will be rejected with a `401 Unauthorized` status.
- **Flask App Setup:** A simple Flask API is used to showcase the authentication mechanism.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt

