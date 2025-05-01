import csv
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, transpile, assemble

def run_delta_experiment(shots=100000, trials=10):
    backend = Aer.get_backend("qasm_simulator")
    delta_results = []

    for trial in range(1, trials + 1):
        qc = QuantumCircuit(3, 3)
        qc.h(0)
        qc.cx(0, 1)
        qc.cx(0, 2)
        qc.h(0)
        qc.measure([0, 1, 2], [0, 1, 2])

        t_qc = transpile(qc, backend)
        qobj = assemble(t_qc, shots=shots)
        result = backend.run(qobj).result()
        counts = result.get_counts()

        total = sum(counts.values())
        p000 = counts.get('000', 0) / total
        p111 = counts.get('111', 0) / total
        delta = p000 - p111

        delta_results.append(delta)
        print(f"Trial {trial}: Δ = {delta:.5f}")

    # Write results to CSV
    with open("delta_multi_trial_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["trial", "delta"])
        for i, delta in enumerate(delta_results, start=1):
            writer.writerow([i, delta])

    # Plot histogram
    plt.hist(delta_results, bins=10, edgecolor='black')
    plt.title("Distribution of Δ Across Trials")
    plt.xlabel("Δ Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_delta_experiment()
