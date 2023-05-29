This code demonstrates a simple quantum teleportation protocol using Qiskit, a quantum computing framework. Here's a breakdown of the code:
The code begins by importing necessary libraries and modules from Qiskit and other related packages.
The deprecated qiskit-ibmq-provider package is imported along with its associated dependencies. The code suggests checking the migration guide for more details on the deprecation and migration process.
The IBM Quantum account is loaded using the QiskitRuntimeService to establish a connection with the IBM Quantum backend.
Next, the code imports the necessary modules from Qiskit for creating and executing quantum circuits.
A QuantumCircuit object with three qubits and three classical bits is created.
The initial state to be teleported is prepared using the initialize method, setting the qubit 0 to the state |0⟩ and qubit 1 to the state |1⟩.
An entangled Bell pair is created by applying a Hadamard gate (h) to qubit 1 and a controlled-X gate (cx) between qubits 1 and 2.
The teleportation protocol is then applied step by step:
A controlled-X gate is applied between qubits 0 and 1.
A Hadamard gate is applied to qubit 0.
A barrier is added for visual separation of steps.
Measurements are performed on qubits 0 and 1, storing the results in classical bits 0 and 1.
Another barrier is added.
A controlled-X gate is applied between qubits 1 and 2.
A controlled-Z gate is applied.


Created By Students of Presidency University,Bangalore- 
Vicky Kumar-20201CAI0092  
Mann Kumar-20201CAI0113 
Ritik Kumar-20201CAI0091
Arya Teja-20201CAI0102
