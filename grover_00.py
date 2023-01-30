import cirq
import openfermion

def print_qubit_result(simulation_result, qid):
  measured_00s = 0
  measured_01s = 0
  measured_10s = 0
  measured_11s = 0
#  for key in simulation_result.measurements:
#    print(key)
#    print(simulation_result.measurements[key].size)
  for i in range(simulation_result.measurements['1'].size):
#  for basis_state in simulation_result.measurements['1']:
    if simulation_result.measurements['1'][i] == 0 and simulation_result.measurements['2'][i] == 0:
      measured_00s += 1
    if simulation_result.measurements['1'][i] == 0 and simulation_result.measurements['2'][i] == 1:
      measured_01s += 1
    if simulation_result.measurements['1'][i] == 1 and simulation_result.measurements['2'][i] == 0:
      measured_10s += 1
    if simulation_result.measurements['1'][i] == 1 and simulation_result.measurements['2'][i] == 1:
      measured_11s += 1
    measured_00_probability = \
      100 * measured_00s / (measured_00s + measured_01s + measured_10s + measured_11s)
    measured_01_probability = \
      100 * measured_01s / (measured_00s + measured_01s + measured_10s + measured_11s)
    measured_10_probability = \
      100 * measured_10s / (measured_00s + measured_01s + measured_10s + measured_11s)
    measured_11_probability = \
      100 * measured_11s / (measured_00s + measured_01s + measured_10s + measured_11s)
  print(" probability distribution: " +
          "00 = " +
          str(measured_00_probability) + "%, " +
          "01 = " +
          str(measured_01_probability) + "%, "  +
          "10 = " +
          str(measured_10_probability) + "%, "  +
          "11 = " +
          str(measured_11_probability) + "%")


# Pick a qubit.
qubits = cirq.LineQubit.range(5)

# Create a circuit
circuit = cirq.Circuit(
	cirq.H(qubits[1]),
	cirq.H(qubits[2])
)

hermitian_T_gate = cirq.inverse(cirq.Z**0.25) #cirq.Z**0.25 = T gate

circuit.append(cirq.S(qubits[1]))
circuit.append(cirq.S(qubits[2]))

circuit.append(cirq.H(qubits[2]))

circuit.append(cirq.CNOT(qubits[1],qubits[2]))

circuit.append(cirq.H(qubits[2]))

circuit.append(cirq.S(qubits[1]))
circuit.append(cirq.S(qubits[2]))

circuit.append(cirq.H(qubits[1]))
circuit.append(cirq.H(qubits[2]))

circuit.append(cirq.X(qubits[1]))
circuit.append(cirq.X(qubits[2]))

circuit.append(cirq.H(qubits[1]))

circuit.append(cirq.CNOT(qubits[1],qubits[2]))

circuit.append(cirq.H(qubits[1]))

circuit.append(cirq.X(qubits[1]))
circuit.append(cirq.X(qubits[2]))

circuit.append(cirq.H(qubits[1]))
circuit.append(cirq.H(qubits[2]))

circuit.append(cirq.measure(qubits[1]))
circuit.append(cirq.measure(qubits[2]))


print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=100)
print("Results:")
print(result)
#print(result.type())
print_qubit_result(result,0)

