from .wire import Wire
from .constants import *

def _id(gate_a, gate_b):
    return f"{gate_a.id} {gate_b.id}"

def rotate_and_mirror(x, y, rotate, mirror_x, mirror_y):
    for _ in range(rotate):
        x, y = SCENE_SIZE - y, x
    if mirror_x:
        x = SCENE_SIZE - x
    if mirror_y:
        y = SCENE_SIZE - y
    return x, y

class Gate:
    def __init__(self, name, obj_stack, wire_stack, coordinates = None, in_pads = 2):
        self.name = name
        self.id = obj_stack.id
        self.in_ = [None for i in range(in_pads)]
        self.out = None
        self.wire_stack = wire_stack
        self.obj_stack = obj_stack
        self.coordinates = coordinates
        self.obj_stack.add(self)
    
    def set_coordinates(self, x, y):
        self.coordinates = [x, y]
    
    def debug_print(self):
        print(self.coordinates)
    
    def connect_out(self, other, other_pad = 0):
        self.out = other
        wire = Wire(self, other, len(self.in_), other_pad)
        other.connect_in(self, wire, other_pad)
    
    def connect_in(self, other, wire, in_pad = 0):
        self.in_[in_pad] = other
        self.wire_stack.add(wire)
    
    def disconnect_out(self, other):
        self.out = None

        try:
            other_pad = self.wire_stack.stack.pop(_id(self, other)).to_pad
        except:
            other_pad = self.wire_stack.stack.pop(_id(other, self)).from_pad
        other.disconnect_in(self, other_pad)
    
    def disconnect_in(self, other, in_pad):
        self.in_[in_pad] = None

    def get_connections(self):
        return self.in_[0], self.in_[1], self.out
    
    def get_render_xml(self, rotate, mirror_x, mirror_y):
        x, y = rotate_and_mirror(self.coordinates[0], self.coordinates[1], rotate, mirror_x, mirror_y)
        return f'<Chip Name="{self.name}" xpos="{x * GRID_SIZE}" ypos="{y * GRID_SIZE}" rot="{rotate}" key="{self.id}" />'
