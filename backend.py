
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample endpoint for court dates
@app.route('/api/court-dates', methods=['GET', 'POST'])
def court_dates():
    if request.method == 'POST':
        new_date = request.json
        # Here, you would normally save to a database
        return jsonify(new_date), 201
    return jsonify([])  # Replace with database fetch

if __name__ == '__main__':
    app.run(debug=True)
