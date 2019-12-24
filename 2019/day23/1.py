#!/usr/bin/env python3


import intcode
import threading
import queue


class Network(object):
    def __init__(self):
        self.devices = {}

    def connect(self, address, ingress, egress):
        self.devices[address] = (ingress, egress)

    def packet_switch(self):
        while True:
            for adr, ch in self.devices.items():
                self.devices[adr][0].put(-1)

                try:
                    dst = ch[1].get_nowait()
                    x = ch[1].get()
                    y = ch[1].get()
                    if dst == 255:
                        return x, y
                    self.devices[dst][0].put(x)
                    self.devices[dst][0].put(y)
                except queue.Empty:
                    pass


def rebuild_network():
    network = Network()
    threads = []
    computers = []
    prog = intcode.load_program("input")

    for adr in range(50):
        ingress = queue.Queue()
        egress = queue.Queue()
        computer = intcode.Computer(prog[:], intcode.PipeIOHandler(ingress, egress, [adr]))
        computers.append(computer)
        network.connect(adr, ingress, egress)
        t = threading.Thread(target=computer.execute)
        t.start()
        threads.append(t)

    x, y = network.packet_switch()

    for c in computers:
        c.suspend()

    for t in threads:
        t.join()

    return y


print(rebuild_network())
