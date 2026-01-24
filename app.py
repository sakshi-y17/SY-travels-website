from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    """Serve the landing page"""
    return render_template('index.html')

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """Handle booking requests"""
    try:
        data = request.json
        # Add your booking logic here
        return jsonify({
            'success': True,
            'message': 'Booking request received',
            'data': data
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400

@app.route('/api/buses', methods=['GET'])
def get_buses():
    """Get available buses"""
    buses = [
        {'id': 1, 'name': 'SY Express', 'seats': 45, 'price': 500},
        {'id': 2, 'name': 'SY Luxury', 'seats': 32, 'price': 800},
        {'id': 3, 'name': 'SY Comfort', 'seats': 50, 'price': 600}
    ]
    return jsonify(buses), 200

@app.route('/api/routes', methods=['GET'])
def get_routes():
    """Get available routes"""
    routes = [
        {'id': 1, 'from': 'Mumbai', 'to': 'Bangalore', 'distance': 1000},
        {'id': 2, 'from': 'Mumbai', 'to': 'Goa', 'distance': 600},
        {'id': 3, 'from': 'Bangalore', 'to': 'Hyderabad', 'distance': 570}
    ]
    return jsonify(routes), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
