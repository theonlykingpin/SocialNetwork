# SocialNetwork

A modern Pinterest-like social web application for discovering, sharing, and bookmarking images, built with Django.

## Overview

**SocialNetwork** is a full-featured social platform designed for sharing images, inspired by Pinterest. Users can register, upload and bookmark images, like and comment on others' posts, follow users, and enjoy a personalized dashboard experience.

## Features

- **User Authentication**  
  Secure registration, login, and profile management using Django's built-in authentication and custom profile models.
- **Image Sharing & Bookmarking**  
  Users can upload images, organize their collection, and bookmark images from across the web using a custom JavaScript bookmarklet.
- **Like System**  
  Like images, see who else liked them, and track popularity.
- **Social Interactions**  
  Follow/unfollow other users, view a feed of their activities, and explore the network.
- **Personal Dashboard**  
  See your images, profile stats, and recent activities in a clean, responsive dashboard.
- **AJAX-powered Actions**  
  Many social interactions (like/follow) are powered by AJAX for seamless user experience.
- **Responsive UI**  
  Modern design using custom CSS for a visually pleasing interface.

## Tech Stack

- **Backend:** Django 3.2
- **Frontend:** Django Templates, jQuery, custom CSS
- **Database:** SQLite (default, can be swapped)
- **Other:**  
  - `django-extensions`
  - `easy-thumbnails` (for image previews)
  - `social_django` (for potential social login integrations)

## Getting Started

### Prerequisites

- Python 3.7+
- pip
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/theonlykingpin/SocialNetwork.git
   cd SocialNetwork
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Visit the app:**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Bookmarklet Setup

To quickly bookmark images from any website:

1. Go to your dashboard after logging in.
2. Drag the "Bookmark it" button to your browser's bookmarks bar.
3. Click the bookmarklet on any page to save images directly to your SocialNetwork account.

## Folder Structure

- `account/` — User authentication, profiles, and social graph (follow system)
- `images/` — Image upload, listing, detail views, and bookmarklet logic
- `actions/` — User activity feed and social actions
- `SocialNetwork/` — Project configuration and settings

## Configuration

- **Settings:**  
  - All settings are in `SocialNetwork/settings.py`
  - Default database is SQLite; change as needed
  - Includes static and media settings for user uploads and static files

## Development

- **Static files** are stored in each app's `static/` directory.
- **Templates** are in each app's `templates/` directory, using Django's template system.
- Use `python manage.py runserver` for local development.
- Extend user profiles via the `Profile` model in `account/models.py`.

## Screenshots

> _Add screenshots here to showcase the dashboard, image list, and social features._

## License

MIT License

---

Built with ❤️ using Django.
