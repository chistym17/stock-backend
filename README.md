# Stock Management Backend

This is a Flask-based backend for stock management

## Features

- Add new stock (POST)
- Retrieve all stocks with pagination (GET)
- Retrieve a single stock by ID (GET)
- Update stock by ID (PUT)
- Delete stock by ID (DELETE)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chistym17/stock-backend.git
   cd stock-backend
   pip install -r requirements.txt
   add a .env file-
   DATABASE_URL=postgresql://username:password@localhost/yourdatabase
   python run.py
