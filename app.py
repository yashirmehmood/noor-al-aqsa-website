from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'Invalid data'}), 400

    name = data.get('name', '').strip()
    phone = data.get('phone', '').strip()
    service = data.get('service', '').strip()
    message = data.get('message', '').strip()

    if not name or not phone:
        return jsonify({'success': False, 'message': 'Name and phone are required'}), 400

    # Log request — replace with DB save or email in production
    print(f"[Contact] Name: {name} | Phone: {phone} | Service: {service} | Msg: {message}")

    return jsonify({'success': True, 'message': 'Request received!'})


if __name__ == '__main__':
    app.run(debug=True)
