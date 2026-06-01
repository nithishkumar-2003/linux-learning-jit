from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/devices/serializers')
    def serializers():
        return jsonify(["MAX96717", "MAX96793", "MAX9295D"])

    @app.route('/devices/deserializers')
    def deserializers():
        return jsonify(["MAX96724", "MAX96794", "MAX9294"])

    return app

if __name__ == '__main__':
    app = create_app()
    # Run on port 5001
    app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)
