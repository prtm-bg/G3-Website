# G3 Website

This is a Django-based web application for managing and sharing academic materials, notices, and resources for Group 3.

## Features
- Material upload and categorization by subject and type
- Notice board for important updates
- Search functionality for materials and notices
- Google Drive integration for resource sharing
- Gallery and PDF viewing

## Requirements
- Python 3.8+
- Django 4.2.6
- See `g3website/requirements.txt` for all dependencies

## Setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r g3website/requirements.txt
   ```
4. Run migrations:
   ```bash
   python g3website/manage.py migrate
   ```
5. Start the development server:
   ```bash
   python g3website/manage.py runserver
   ```

## License
MIT License. See `LICENSE` for details.
