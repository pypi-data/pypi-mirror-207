from constants import GRID_SIZE


class Wire:
    def __init__(self, from_, to_, from_pad, to_pad) -> None:
        self.from_ = from_
        self.to_ = to_
        self.from_pad = from_pad
        self.to_pad = to_pad
        self.id = 0
    
    def debug_print(self):
        print(self.from_id, self.to_id)
    
    def get_render_xml(self):
        return f'<Wire chip1="{self.from_.id}" pad1="{self.from_pad}" chip2="{self.to_.id}" pad2="{self.to_pad}" key="{self.id}" />'
