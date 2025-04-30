from qiskit import QuantumCircuit, Aer, transpile, assemble

def run_experiment(shots=100000):
    qc = QuantumCircuit(3, 3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.h(0)
    qc.measure([0, 1, 2], [0, 1, 2])

    backend = Aer.get_backend("qasm_simulator")
    t_qc = transpile(qc, backend)
    qobj = assemble(t_qc, shots=shots)
    result = backend.run(qobj).result()
    counts = result.get_counts()

    total = sum(counts.values())
    p000 = counts.get('000', 0) / total
    p111 = counts.get('111', 0) / total
    delta = p000 - p111

    print("Counts:", counts)
    print("Δ = P(000) - P(111) =", delta)

if __name__ == "__main__":
    run_experiment()