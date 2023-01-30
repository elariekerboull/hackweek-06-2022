import cirq
import openfermion

def print_qubit_result(simulation_result):
  measured_00s = 0
  measured_01s = 0
  measured_10s = 0
  measured_11s = 0
  stringA = ""
  stringB = ""
#  for key in simulation_result.measurements:
#    print(key)
#    print(simulation_result.measurements[key].size)
  for i in range(simulation_result.measurements['1'].size):
#  for basis_state in simulation_result.measurements['1']:
    if simulation_result.measurements['1'][i] == simulation_result.measurements['2'][i]:
      stringA += str(simulation_result.measurements['0'][i])
      stringB += str(simulation_result.measurements['3'][i])
  print(" Key A " + stringA +
          "\n Key B " + stringB)


# Pick a qubit.
qubits = cirq.LineQubit.range(5)

iteration_number = 100

# Create a circuit
circuit = cirq.Circuit(
	# 3 random values
	cirq.H(qubits[0]), # a
	cirq.H(qubits[1]), # b
	cirq.H(qubits[2]) # c
)

circuit.append(cirq.X(qubits[3]).controlled_by(qubits[0])) # Same as CNOT but implemented that way for clarity

circuit.append(cirq.H(qubits[3]).controlled_by(qubits[1]))

circuit.append(cirq.H(qubits[3]).controlled_by(qubits[2]))

circuit.append(cirq.measure(qubits[0])) # Optional
circuit.append(cirq.measure(qubits[1]))
circuit.append(cirq.measure(qubits[2]))
circuit.append(cirq.measure(qubits[3]))


print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=iteration_number)
print("Results:")
print(result)

print_qubit_result(result)

