import glob
import os
import time


BASE_DIR = '/sys/bus/w1/devices'


def device_path_to_file(path):
    return os.path.join(path, 'w1_slave')


def get_device_paths(base_dir=BASE_DIR):
    return glob.glob(os.path.join(base_dir, '28-*'))



def modprobe(mod):
    return os.system('modprobe {}'.format(mod))

# From https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software
def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


def get():
    device_file = device_path_to_file(get_device_paths()[0])
    temp_c, temp_f = read_temp(device_file)
    return temp_f


if __name__ == '__main__':
    modprobe('w1-gpio')
    modprobe('w1-therm')
    print(get())
