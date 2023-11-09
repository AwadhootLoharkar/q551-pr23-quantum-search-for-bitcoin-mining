from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.providers.aer import QasmSimulator

# Number of qubits required for a 10-digit binary number
n = 10

# Create a quantum circuit with n qubits
oracle_circuit = QuantumCircuit(n)

# Define the pattern you want to find (6 leading zeros)
pattern = '000000'

# Apply a CNOT gate to each of the last four qubits controlled by the first six qubits
for i in range(len(pattern)):
    if pattern[i] == '0':
        oracle_circuit.cx(i, i + len(pattern))

# Apply an X gate to the last four qubits
oracle_circuit.x(range(len(pattern), n))

# Apply the same CNOT gates again
for i in range(len(pattern)):
    if pattern[i] == '0':
        oracle_circuit.cx(i, i + len(pattern))

# Apply the X gate again
oracle_circuit.x(range(len(pattern), n)

# Draw the oracle circuit for visualization
oracle_circuit.draw()
