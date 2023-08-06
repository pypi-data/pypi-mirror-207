from .enums import DecoderModes
from .gate import Gate
from .connection_pin import ConnectionPin
from .gate_block import GateBlock, SingleVarScheme, MultiVarScheme, Decoder
from .wire import Wire
from .id_tracker import WireStack, ObjStack, render_all


class App:
    def __init__(self) -> None:
        self.ws = WireStack()
        self.os = ObjStack()
    
    def run(self):
        dec = Decoder(
            self.os,
            self.ws,
            formulas=[
                [
                    [0, 0, 1, 0],
                    [1, 0, 1, 0],
                    [1, 0, 0, 1]
                ],
                [
                    [0, 0, 0, 1],
                    [0, 0, 1, 0],
                    [0, 1, 0, 0],
                    [1, 0, 0, 1]
                ],
                [
                    [0, 0, 0, 1],
                    [0, 1, 0, 0],
                    [0, 1, 0, 1],
                    [1, 0, 0, 1]
                ],
                [
                    [0, 0, 1, 0],
                    [0, 1, 0, 1],
                    [1, 0, 0, 1]
                ],
                [
                    [0, 0, 1, 0]
                ],
                [
                    [0, 1, 0, 0],
                    [0, 1, 0, 1],
                    [1, 0, 0, 1]
                ],
                [[1, 1, 1, 0]],
                [
                    [1, 1, 1, 0],
                    [1, 1, 0, 1],
                    [1, 0, 1, 1],
                    [1, 0, 1, 0],
                    [0, 1, 1, 0]
                ]
            ],
            modes=[
                DecoderModes.AND_OR,
                DecoderModes.AND_OR,
                DecoderModes.AND_OR,
                DecoderModes.AND_OR,
                DecoderModes.AND_OR,
                DecoderModes.AND_OR,
                DecoderModes.OR_AND,
                DecoderModes.OR_AND
            ],
        )
        
        dec.build()
        with open("test.atanua", "w") as f:
            f.write(render_all(self.os, self.ws, 0))

if __name__ == "__main__":
    a = App()
    a.run()
