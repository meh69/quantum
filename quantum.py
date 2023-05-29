
from ibm_quantum_widgets import *
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session, Options
service = QiskitRuntimeService(channel="ibm_quantum")

from qiskit import QuantumCircuit, Aer, execute

circuit = QuantumCircuit(3, 3)
circuit.initialize([0, 1], 0)
circuit.h(1)
circuit.cx(1, 2)
circuit.cx(0, 1)
circuit.h(0)
circuit.barrier()
circuit.measure([0, 1], [0, 1])
circuit.barrier()
circuit.cx(1, 2)
circuit.cz(0, 2)
circuit.measure(2, 2)
backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend, shots=1)
result = job.result()
counts = result.get_counts(circuit)

print("Measurement Results:", counts)
