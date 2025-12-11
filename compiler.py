# compiler.py
# CALC Language Compiler
# Converts CALC code → Python code
# Usage: python compiler.py input.calc output.py

import sys

def compile_calc(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    output_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Variable assignment: let x = 5
        if line.startswith("let"):
            # Structure: ["let", "x", "=", "5"]
            parts = line.split(" ", 3)
            var_name = parts[1]
            expr = parts[3]
            output_lines.append(f"{var_name} = {expr}")

        # Print statement: print x + 5
        elif line.startswith("print"):
            expr = line[len("print "):]
            output_lines.append(f"print({expr})")

        else:
            print(f"Unknown syntax: {line}")

    # write Python output
    with open(output_file, "w") as f:
        for o in output_lines:
            f.write(o + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compiler.py input.calc output.py")
    else:
        compile_calc(sys.argv[1], sys.argv[2])

