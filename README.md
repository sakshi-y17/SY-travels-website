# SY Travels - Bus Booking Platform

## Project Structure
- `index.html` - Landing page with booking form
- `app.py` - Flask server
- `requirements.txt` - Python dependencies

## Setup Instructions

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Flask Server
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 3. Open the Landing Page
Open `index.html` in your browser or navigate to:
```
http://localhost:5000/
```

## API Endpoints

### GET `/` 
- Serves the landing page

### POST `/api/bookings`
- Create a new booking
- Body: `{ email, age, gender, password }`
- Returns: Booking confirmation

### GET `/api/buses`
- Get list of available buses
- Returns: Array of bus objects

### GET `/api/routes`
- Get available travel routes
- Returns: Array of route objects

## Features
- ✅ Responsive landing page
- ✅ Flask backend server
- ✅ RESTful API endpoints
- ✅ Booking form integration
- ✅ Real-time data fetching from server

## Troubleshooting

If you get CORS errors, install flask-cors:
```bash
pip install flask-cors
```

Then update `app.py` to include:
```python
from flask_cors import CORS
CORS(app)
```
