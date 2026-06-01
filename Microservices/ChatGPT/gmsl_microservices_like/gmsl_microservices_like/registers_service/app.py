from flask import Flask, jsonify, request
import threading

def create_app():
    app = Flask(__name__)

    # Simple in-memory register map (8-bit registers)
    register_map = {0x01: 0b00000000}
    lock = threading.Lock()

    @app.route('/registers', methods=['GET'])
    def get_registers():
        with lock:
            # return as hex keys for readability
            return jsonify({hex(k): v for k, v in register_map.items()})

    @app.route('/registers/0x01', methods=['GET'])
    def get_reg_01():
        with lock:
            return jsonify({'address': '0x01', 'value': register_map.get(0x01, 0)})

    @app.route('/registers/0x01/set_tx_rate', methods=['POST'])
    def set_tx_rate():
        data = request.get_json() or {}
        rate = data.get('rate')
        if rate not in ('3Gbps', '6Gbps'):
            return jsonify({'error': 'rate must be "3Gbps" or "6Gbps"'}), 400
        with lock:
            if rate == '3Gbps':
                # set bit1 = 1, bit2 = 0
                register_map[0x01] = (register_map[0x01] | (1 << 1)) & ~(1 << 2)
            else:
                # 6Gbps: set bit1 = 0, bit2 = 1
                register_map[0x01] = (register_map[0x01] & ~(1 << 1)) | (1 << 2)
            return jsonify({'address': '0x01', 'value': register_map[0x01], 'bin': bin(register_map[0x01])})

    return app

if __name__ == '__main__':
    app = create_app()
    # Run on port 5002
    app.run(host='127.0.0.1', port=5002, debug=False, use_reloader=False)
