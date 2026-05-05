#!/usr/bin/env python3
# Written by claude

with open('input_day24', 'r', encoding='utf-8') as f:
    data = f.read().strip()

init_part, gates_part = data.split('\n\n')

wires = {}
for line in init_part.splitlines():
    name, val = line.split(': ')
    wires[name] = int(val)

gates = []
for line in gates_part.splitlines():
    parts = line.split(' ')
    a, op, b, _, out = parts
    gates.append((a, op, b, out))

# Part 1: simulate all gates
def simulate(wires, gates):
    wires = dict(wires)
    remaining = list(gates)
    while remaining:
        progress = False
        next_remaining = []
        for a, op, b, out in remaining:
            if a in wires and b in wires:
                va, vb = wires[a], wires[b]
                if op == 'AND':
                    wires[out] = va & vb
                elif op == 'OR':
                    wires[out] = va | vb
                elif op == 'XOR':
                    wires[out] = va ^ vb
                progress = True
            else:
                next_remaining.append((a, op, b, out))
        remaining = next_remaining
        if not progress:
            break
    return wires

result_wires = simulate(wires, gates)
z_wires = sorted((k for k in result_wires if k.startswith('z')), reverse=True)
z_value = int(''.join(str(result_wires[w]) for w in z_wires), 2)
print(z_value)

# Part 2: find 4 pairs of swapped output wires in a ripple-carry adder
# The circuit implements z = x + y using full adders
# Identify structural violations in the adder circuit

gate_map = {}
for a, op, b, out in gates:
    gate_map[out] = (a, op, b)

def find_gate(a, op, b):
    for out, (ga, gop, gb) in gate_map.items():
        if gop == op and ((ga == a and gb == b) or (ga == b and gb == a)):
            return out
    return None

def get_inputs_with_op(op):
    return [(a, b, out) for out, (a, gop, b) in gate_map.items() if gop == op]

swapped = set()

# In a correct ripple-carry adder:
# half adder for bit 0: z0 = x0 XOR y0, c0 = x0 AND y0
# full adder for bit i: zi = (xi XOR yi) XOR ci-1, ci = (xi AND yi) OR ((xi XOR yi) AND ci-1)

n_bits = sum(1 for k in wires if k.startswith('x'))

carry = None
for i in range(n_bits):
    xi = f'x{i:02d}'
    yi = f'y{i:02d}'
    zi = f'z{i:02d}'

    xor1 = find_gate(xi, 'XOR', yi)
    and1 = find_gate(xi, 'AND', yi)

    if i == 0:
        carry = and1
        continue

    xor2 = find_gate(xor1, 'XOR', carry)
    and2 = find_gate(xor1, 'AND', carry)
    or1 = find_gate(and1, 'OR', and2) if and2 else None

    if xor2 is None or xor2 != zi:
        # Something is swapped - heuristic: mark involved wires
        swapped.add(xor1 or zi)
        swapped.add(zi)

    if or1:
        carry = or1
    elif and2:
        carry = and2

print(','.join(sorted(swapped)))
