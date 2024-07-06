# Spam Detection and User Identification API

A REST API for spam detection and user identification by phone number, designed for mobile app integration.

## Project Description

This project provides a REST API to be consumed by a mobile app, similar to popular apps that identify spam numbers and allow users to search for a person's name by their phone number.

## Features

- **User Registration**: Register a new user with their name, phone number, email, and password.
- **User Lookup**: Retrieve user details by their ID.
- **Contact Management**: Add contacts for a user.
- **Spam Reporting**: Report phone numbers as spam.
- **Search Users**: Search for users by name or phone number.

## Endpoints

### User Endpoints

- `POST /users/` - Create a new user.
- `GET /users/{user_id}` - Get user details by user ID.

### Contact Endpoints

- `POST /users/{user_id}/contacts/` - Create a new contact for a user.

### Spam Report Endpoints

- `POST /spam/` - Report a phone number as spam.

### Search Endpoints

- `GET /search/users/` - Search for users by name.
- `GET /search/phone/` - Search for users by phone number.




## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Chiragj2003/SpamApi-using-FastAPI.git
   cd spam_api
