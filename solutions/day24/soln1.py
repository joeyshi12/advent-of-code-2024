import re
from collections import deque
from dataclasses import dataclass


@dataclass
class LogicGate:
    in1: str
    in2: str
    op: str
    out: str


def read_input(filename: str) -> tuple[dict[str, int], list[LogicGate]]:
    with open(filename, "r") as file:
        input_values = {}
        for line in file:
            if line.isspace():
                break
            name, value = line.split(": ")
            input_values[name] = int(value)

        logic_gates = []
        for line in file:
            match = re.match("([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})", line)
            if match:
                in1, op, in2, out = match.groups()
                logic_gates.append(LogicGate(in1, in2, op, out))

        return input_values, logic_gates


def compute_output(input_values: dict[str, int],
                   logic_gates: list[LogicGate]) -> int:
    wire_values = input_values.copy()
    gate_queue = deque(logic_gates)
    while gate_queue:
        gate = gate_queue.popleft()
        if gate.in1 not in wire_values or gate.in2 not in wire_values:
            gate_queue.append(gate)
            continue

        match gate.op:
            case "AND":
                wire_values[gate.out] = wire_values[gate.in1] & wire_values[gate.in2]
            case "OR":
                wire_values[gate.out] = wire_values[gate.in1] | wire_values[gate.in2]
            case "XOR":
                wire_values[gate.out] = wire_values[gate.in1] ^ wire_values[gate.in2]
            case _:
                raise Exception(f"Invalid op {gate.op}")

    z_outputs = [gate.out for gate in logic_gates if gate.out[0] == "z"]
    z_outputs.sort(reverse=True)
    bitstring = "".join([str(wire_values[out]) for out in z_outputs])
    return int(bitstring, 2)


def main():
    input_values, logic_gates = read_input("input")
    print(compute_output(input_values, logic_gates))


if __name__ == "__main__":
    main()
