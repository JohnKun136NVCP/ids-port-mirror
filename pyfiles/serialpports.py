import serial.tools.list_ports as list_ports
def ports():
    # code by michalmonday onhttps://github.com/michalmonday/CSV-Parser-for-Arduino/tree/master/examples/reading_from_computer_python/arduino_serial.py
    try:
        inputport = []
        for i, p in enumerate(list_ports.comports()):
            print(f'{i}. device={p.device} name={p.name} description={p.description} manufacturer={p.manufacturer}')
            inputport.append(p.device)
            nameport = int(input("Choose your port: "))
        return inputport[nameport]
    except:
        return -1
