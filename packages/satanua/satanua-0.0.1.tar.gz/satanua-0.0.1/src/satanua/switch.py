from constants import GRID_SIZE, SCENE_SIZE
from wire import Wire

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

class Switch:
    def __init__(self, name, obj_stack, wire_stack, coordinates) -> None:
        self.id = obj_stack.id
        obj_stack.add(self)
        self.obj_stack = obj_stack
        self.wire_stack = wire_stack
        self.coordinates = coordinates
        self.name = name
        self.out = []
    
    def connect_out(self, other, other_pad = 0):
        self.out.append(other)
        wire = Wire(self, other, 0, other_pad)
        other.connect_in(self, wire, other_pad)
    
    def disconnect_out(self, other, other_pad = 0):
        self.out.pop(self.out.index(other))

        try:
            self.wire_stack.stack.pop(_id(self, other))
        except:
            self.wire_stack.stack.pop(_id(other, self))
        other.disconnect_in(self, other_pad)
    
    def get_render_xml(self, rotate, mirror_x, mirror_y):
        x, y = rotate_and_mirror(self.coordinates[0], self.coordinates[1], rotate, mirror_x, mirror_y)
        return f'<Chip Name="switch (&apos;{self.name}&apos;)" xpos="{x * GRID_SIZE}" ypos="{y * GRID_SIZE}" rot="0" key="{self.id}" />'
        