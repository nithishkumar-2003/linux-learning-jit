import multiprocessing
import time
import os
import sys

def run_devices():
    # run the devices service
    from devices_service import app as devices_app
    devices_app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)

def run_registers():
    from registers_service import app as registers_app
    registers_app.run(host='127.0.0.1', port=5002, debug=False, use_reloader=False)

def main():
    # When run_all is started, change cwd so modules import correctly
    base = os.path.dirname(__file__)
    sys.path.insert(0, base)

    p1 = multiprocessing.Process(target=run_devices, name='devices_service')
    p2 = multiprocessing.Process(target=run_registers, name='registers_service')

    p1.start()
    p2.start()

    # Wait a moment for services to start
    time.sleep(1.0)

    try:
        # Start UI (it will call the local services)
        from ui_client import ui_app
        ui_app.main()
    finally:
        # Terminate child processes when UI closes
        for p in (p1, p2):
            if p.is_alive():
                p.terminate()
                p.join(timeout=1.0)

if __name__ == '__main__':
    main()
