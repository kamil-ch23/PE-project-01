from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now(),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({ 'status': 'up' }), 200

if __name__ == '__main__':

    #app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0')

#'/api/v1/details'
#'/api/v1/healthz'