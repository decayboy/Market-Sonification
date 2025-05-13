import rtmidi
import random

class MidiEngine:
    def __init__(self):
        self.midiout = rtmidi.MidiOut()
        ports = self.midiout.get_ports()
        if ports:
            self.midiout.open_port(0)
        else:
            self.midiout.open_virtual_port("Market_Sonifier")

    def play_note(self, note, velocity=80, channel=0, duration=0.2):
        self.midiout.send_message([0x90 + channel, note, velocity])
    
    def stop_note(self, note, channel=0):
        self.midiout.send_message([0x80 + channel, note, 0])

    def percussion_hit(self):
        drum_note = random.choice([36, 38, 42, 46])  # Kick, snare, hihat
        self.midiout.send_message([0x99, drum_note, 100])
