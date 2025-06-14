# Feelify Backend

Feelify is a music web application that lets users generate personalized Spotify playlists based on their mood, favorite genres, and artists. The backend is built with Django, Django REST Framework, and integrates with the Spotify API and OpenRouter AI for playlist generation.

## Features

- **Spotify OAuth Authentication**: Users log in with their Spotify account. The backend handles the OAuth flow, exchanges the code for tokens, and fetches user info.
- **JWT Authentication**: After Spotify login, users receive JWT access and refresh tokens for secure API access.
- **Custom User Model**: The app uses a custom user model with support for Spotify ID and avatar.
- **Playlist Generation**: Users can generate playlists by providing mood, genres, and artists. The backend uses OpenRouter AI to suggest tracks and can create playlists in the user's Spotify account.
- **Track and Playlist Models**: Playlists and tracks are stored in the database and linked to users. Users can view all their generated playlists and tracks.
- **Logout and Token Blacklisting**: Secure logout with refresh token blacklisting and support for HTTP-only cookies.
- **CORS Support**: Configured for frontend-backend communication during development.

## API Endpoints

- `POST /api/auth/v1/spotify/login/` — Start Spotify OAuth login
- `POST /api/auth/v1/spotify/callback/` — Handle Spotify OAuth callback, issue JWTs
- `POST /api/auth/v1/logout/` — Logout and blacklist refresh token
- `GET /api/users/v1/me/` — Get current user info
- `POST /api/playlist/v1/generate/` — Generate a playlist using AI and save it
- `GET /api/playlist/v1/my/` — List all playlists for the current user

## Technologies Used
- Python 3.12
- Django 5.x
- Django REST Framework
- SimpleJWT (JWT authentication)
- django-cors-headers
- Spotify Web API
- OpenRouter AI API

## Development Setup

1. Clone the repository and install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Set up your `.env` file with Spotify and OpenRouter credentials.
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Frontend
- The backend is designed to work with any frontend (Next.js, Streamlit, etc.).
- CORS is enabled for local development.

## Notes
- Make sure to register your redirect URIs with Spotify.
- For production, update CORS and cookie settings for security.

---
Feel free to extend the project with more features, such as playlist editing, user analytics, or advanced AI recommendations!
