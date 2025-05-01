import csv
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble

# Function to run the Δ experiment multiple times
def run_delta_experiment(shots=100000, trials=10):
    # Use Qiskit's built-in quantum circuit simulator
    backend = Aer.get_backend("qasm_simulator")
    delta_results = []  # List to store Δ values from each trial

    for trial in range(1, trials + 1):
        # --- Construct the circuit ---
        qc = QuantumCircuit(3, 3)

        # Step 1: Place qubit 0 (control) in superposition
        qc.h(0)

        # Step 2: Apply branching logic
        qc.cx(0, 1)  # Simulate Branch A
        qc.cx(0, 2)  # Simulate Branch B

        # Step 3: Recombine branches using Hadamard
        qc.h(0)

        # Step 4: Measure all qubits
        qc.measure([0, 1, 2], [0, 1, 2])

        # --- Simulate the circuit ---
        t_qc = transpile(qc, backend)
        qobj = assemble(t_qc, shots=shots)
        result = backend.run(qobj).result()
        counts = result.get_counts()

        # --- Calculate Δ = P(000) - P(111) ---
        total = sum(counts.values())
        p000 = counts.get('000', 0) / total
        p111 = counts.get('111', 0) / total
        delta = p000 - p111

        # Store and display the result
        delta_results.append(delta)
        print(f"Trial {trial}: Δ = {delta:.5f}")

    # --- Save all Δ values to CSV file ---
    with open("delta_multi_trial_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["trial", "delta"])  # Header
        for i, d in enumerate(delta_results, 1):
            writer.writerow([i, d])  # Each row = [trial_number, delta_value]

    # --- Calculate statistical metrics ---
    mean_delta = np.mean(delta_results)
    std_delta = np.std(delta_results)

    print(f"\nMean Δ: {mean_delta:.5f}")
    print(f"Std Dev: {std_delta:.5f}")

    # --- Plot histogram of Δ values ---
    plt.figure(figsize=(8, 5))
    plt.hist(delta_results, bins=10, edgecolor='black')

    # Add vertical lines for collapse prediction (0) and observed mean
    plt.axvline(0, color='red', linestyle='--', label='Collapse Prediction (Δ = 0)')
    plt.axvline(mean_delta, color='blue', linestyle='-', label=f'Mean Δ ≈ {mean_delta:.5f}')

    plt.title("Distribution of Δ Across Trials")
    plt.xlabel("Δ Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run the experiment when the script is executed directly
if __name__ == "__main__":
    run_delta_experiment()
