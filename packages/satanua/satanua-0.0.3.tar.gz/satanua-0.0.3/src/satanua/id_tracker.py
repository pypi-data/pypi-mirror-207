from .constants import SCENE_SIZE


def _id(gate_a, gate_b):
    return f"{gate_a.id} {gate_b.id}"

def render_all(os, ws, rotate=0, mirror_x=False, mirror_y=False):
    return '<?xml version="1.0" ?>\n<Atanua Version="Atanua/Win32 1.3.141220 (debug) - Wym" ChipCount="5" WireCount="3" key="267" scale="16">\n' + \
        os.render_all(rotate, mirror_x, mirror_y) + '\n' + ws.render_all() + \
        '\n</Atanua>'

class ObjStack:
    def __init__(self) -> None:
        self._id = -1
        self.stack = {}
    
    @property
    def id(self):
        self._id += 1
        return self._id

    def recalc_ids(self):
        self._id = -1
        for obj in sorted(list(self.stack.values()), key=lambda x: x.id):
            obj.id = self.id

    def add(self, obj):
        self.stack[obj.id] = obj
    
    def remove(self, obj):
        self.stack.pop(obj.id)
    
    def render_all(self, rotate, mirror_x, mirror_y):
        return "\n".join([obj.get_render_xml(rotate, mirror_x, mirror_y) for obj in list(self.stack.values())])

class WireStack:
    def __init__(self) -> None:
        self.stack = {}
        self.id = 100000
    
    def add(self, wire):
        wire.id = self.id
        self.id += 1
        self.stack[_id(wire.from_, wire.to_)] = wire
    
    def remove(self, from_, to_):
        self.stack.pop(_id(from_, to_))
    
    def render_all(self):
        return "\n".join([obj.get_render_xml() for obj in list(self.stack.values())])
