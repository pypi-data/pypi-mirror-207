from .constants import *
from .gate import Gate
from .connection_pin import ConnectionPin
from .switch import Switch

def count_inputs(svf):
    return sum([sum([int(num != None) for num in row]) for row in svf])

class GateBlock:
    def __init__(self, gates_type, coordinates, obj_stack, wire_stack, size=8, input_gates = None):
        self.size = size
        self.coordinates = coordinates
        self.gates_type = gates_type
        self.obj_stack = obj_stack
        self.wire_stack = wire_stack
        self.in_pins = []
        self.in_pads_connected = 0
        self.out_gates = [] # preserve out pins for the pyramid creation. Are also used to store connection pins temporarily
        if input_gates: 
            self.size = len(input_gates)
            self.out_gates = input_gates
        self.place_gates()
    
    def place_gates(self):
        if len(self.out_gates) == 0:
            self.place_in_pins()
        if self.size == 1:
            pin2 = self.out_gates.pop()
            self.out_gates.append(pin := ConnectionPin(
                self.obj_stack,
                self.wire_stack,
                [
                    self.coordinates[0] - HORIZONTAL_LG_OFFSET, 
                    self.coordinates[1]
                ]
                ))
            pin2.connect_out(pin)
            return
        self.create_pyramid()
    
    def place_in_pins(self):
        for i in range(self.size): # first, create input pins
            self.in_pins.append(pin := ConnectionPin(
                self.obj_stack,
                self.wire_stack,
                [
                    self.coordinates[0] - HORIZONTAL_LG_OFFSET, 
                    self.coordinates[1] + (VERTICAL_LG_HALF_OFFSET * (i - i % 2))
                    # this just applies the offset in a way that with the creation of next layers first layer will be properly placed
                ]
                ))
            self.out_gates.append(pin)
    
    def adjust_in_pins_positions(self):
        for i, pin in enumerate(self.in_pins):
            pin.coordinates[1] = pin.out[0].coordinates[1] + GATES_INTERNAL_PIN_OFFSETS[pin.out[0].in_.index(pin)]
        
    def get_next_pin(self):
        try:
            return self.in_pins[self.in_pads_connected]
        except:
            print("Max size exceeded")
    
    def connect_next_pin(self, from_):
        pin = self.in_pins[self.in_pads_connected]
        to_gate = pin.out[0]
        to_pad = to_gate.in_.index(pin)
        pin.disconnect_out(to_gate, to_pad)
        self.obj_stack.remove(pin)
        from_.connect_out(to_gate, to_pad)
        self.in_pads_connected += 1
    
    def create_pyramid(self): #then fill the rest
        while len(self.out_gates) > 1:
            layer_repeats = int(len(self.out_gates) / 2)
            offset = len(self.out_gates) % 2 # need this to not immediately connect free out_gate but connect it in the end, otherwise it will overlap
            for layer in range(layer_repeats):
                gate1: Gate = self.out_gates.pop(offset)
                gate2: Gate = self.out_gates.pop(offset)

                self.out_gates.append(gate := Gate(
                    self.gates_type,
                    self.obj_stack,
                    self.wire_stack,
                    [
                        max(gate1.coordinates[0], gate2.coordinates[0]) + HORIZONTAL_LG_OFFSET,
                        (gate1.coordinates[1] + gate2.coordinates[1]) / 2
                    ]
                ))
                gate1.connect_out(gate, 0)
                gate2.connect_out(gate, 1)
        self.adjust_in_pins_positions()
    
class SingleVarScheme:
    def __init__(self, obj_stack, wire_stack, formula: list[list], mode = "AND", coordinates = [100, 0]) -> None:
        if mode == "AND":
            self.gates_sequence = ["Logic AND", "Logic OR"]
        elif mode == "OR":
            self.gates_sequence = ["Logic OR", "Logic AND"]
        self.coordinates = coordinates
        self.formula = formula
        self.obj_stack = obj_stack
        self.wire_stack = wire_stack
        self.blocks = []
        self.inputs = []
    
    def create_blocks(self):
        first_layer_outputs = []
        acc_offset = 0
        for i, row in enumerate(self.formula):
            row_nulls = sum([int(i == None) for i in row])
            draw_size = int((len(row) - row_nulls) * VERTICAL_LG_OFFSET / 2)
            self.blocks.append(block := GateBlock(
                self.gates_sequence[0],
                [self.coordinates[0], self.coordinates[1] + acc_offset],
                self.obj_stack,
                self.wire_stack,
                len(row) - row_nulls
            ))
            self.inputs += block.in_pins
            acc_offset += draw_size
            first_layer_outputs.append(block.out_gates[0])
        GateBlock(
            self.gates_sequence[1],
            [0, 0],
            self.obj_stack,
            self.wire_stack,
            0,
            first_layer_outputs
        )

class MultiVarScheme:
    def __init__(self, obj_stack, wire_stack, formulas=[[1]], modes=["AND"], coordinates=[100, 0]) -> None:
        self.obj_stack = obj_stack
        self.wire_stack = wire_stack
        self.coordinates = coordinates
        self.modes = modes
        self.formulas = formulas
        self.schemes = []
    
    def create_schemes(self):
        accumulated_offset = 0
        for index, single_var_formula in enumerate(self.formulas):
            self.schemes.append(svs := SingleVarScheme(
                self.obj_stack,
                self.wire_stack,
                single_var_formula,
                self.modes[index],
                [
                    self.coordinates[0],
                    self.coordinates[1] + accumulated_offset
                ]
            ))
            svs.create_blocks()
            accumulated_offset += count_inputs(single_var_formula) * VERTICAL_LG_OFFSET / 2

class Decoder:
    def __init__(self, obj_stack, wire_stack, formulas=[[[1]]], modes=["AND"], coordinates=[0, 0]) -> None:
        self.obj_stack = obj_stack
        self.wire_stack = wire_stack
        self.formulas = formulas
        self.modes = modes
        self.in_size = len(formulas[0][0])
        self.coordinates = coordinates
        self.input_pins: list[ConnectionPin] = []
    
    def build(self):
        self.create_schemes()
        self.place_starting_pins()
        self.connect_pins()
    
    def create_schemes(self):
        self.multi_var_scheme = MultiVarScheme(
            self.obj_stack,
            self.wire_stack,
            self.formulas,
            self.modes,
            [
                self.coordinates[0] + (self.in_size * INPUTS_HORIZONTAL_OFFSET),
                self.coordinates[1] + INPUTS_VERTICAL_OFFSET
            ]
        )
        self.multi_var_scheme.create_schemes()
    
    def place_starting_pins(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(self.in_size):
            self.input_pins.append(Switch(
                letters[i],
                self.obj_stack,
                self.wire_stack,
                [
                    self.coordinates[0] + (i * INPUTS_HORIZONTAL_OFFSET),
                    self.coordinates[1]
                ]
            ))
    
    def connect_pins(self):
        for i_scheme, svs in enumerate(self.multi_var_scheme.schemes):
            for i_block, block in enumerate(svs.blocks):
                formula_row = self.formulas[i_scheme][i_block]
                offset = SWITCH_HORIZONTAL_OFFSET if i_block == 0 and i_scheme == 0 else 0
                for index, num in enumerate(formula_row):
                    if num != None:

                        conn_pin = block.get_next_pin()

                        fut_input_pin = ConnectionPin(
                            self.obj_stack,
                            self.wire_stack,
                            [
                                self.input_pins[index].coordinates[0] + offset,
                                conn_pin.coordinates[1]
                            ]
                        )

                        self.input_pins[index].connect_out(fut_input_pin, 0)
                        self.input_pins[index] = fut_input_pin
                        connect_from = fut_input_pin

                        if num == 0:
                            not_gate = Gate(
                                "Logic NOT",
                                self.obj_stack,
                                self.wire_stack,
                                [
                                    connect_from.coordinates[0] + NOT_GATE_HORIZONTAL_OFFSET,
                                    connect_from.coordinates[1] + NOT_GATE_VERTICAL_OFFSET
                                ],
                                in_pads=1
                            )
                            self.input_pins[index].connect_out(not_gate, 0)
                            block.connect_next_pin(not_gate)
                        else:
                            block.connect_next_pin(connect_from)


        self.obj_stack.recalc_ids()
