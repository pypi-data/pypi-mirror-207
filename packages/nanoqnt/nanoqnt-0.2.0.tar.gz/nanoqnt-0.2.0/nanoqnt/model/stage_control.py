from time import sleep

import pyvisa

rm = pyvisa.ResourceManager('@py')


class StageControl:
    def __init__(self):
        self.scan_running = False
        self.stage = rm.open_resource('ASRL8::INSTR')
        self.arduino = rm.open_resource('ASRL7::INSTR')
        self.stage.baud_rate = 115200
        self.arduino.baud_rate = 115200
        self.arduino.write_termination = '\r'
        self.stage.read_termination = '\n'
        self.stage.write_termination = '\r'
        sleep(2)
        self.arduino.timeout = 5000
        self.stage.timeout = 5000

    def live(self):
        print(self.arduino.query('live').strip())

    def stop_live(self):
        print(self.arduino.query('stop').strip())

    def snap(self):
        print(self.arduino.query('snap').strip())

    def move(self, position):
        print(self.stage.query(f'GT z{position}').strip())

    def prepare_scan(self, start):
        self.stop_live()
        print('Move to start')
        self.stage.query(f'GT z{start}')
        while self.stage.query('RZ z') == '$RS z1':
            sleep(0.01)

    def scan(self, start, end, step_size):
        self.scan_running = True

        if (end-start)/step_size < 0:
            step_size = -step_size

        for p in range(start, end, step_size):
            self.stage.query(f'GT z{p}')
            while self.stage.query('RS z') == '$RS z1':
                sleep(0.001)
            sleep(0.1)
            self.arduino.query('snap')

        print('Done')