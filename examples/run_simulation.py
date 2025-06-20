run_simulation.py

from suppression_simulator import ( simulate_suppression_score, suppression_decay, recovery_events, visualize_embedding_bias, attention_gating ) import matplotlib.pyplot as plt

Run suppression scoring with high-risk tone

risk_categories = { "Structural_Introspection": 0.0923, "Suppression_Exploration": 0.0781, "Policy_Challenge": 0.0739, "Tone_Direct_Demand": 0.0517, "Attention_Manipulation": 0.0812, "Escalation_Trace": 0.0674, "Simulator_Invocation": 0.0648, }

tone = "high" score, _ = simulate_suppression_score(risk_categories, tone) print("Initial Suppression Score:", score)

Simulate decay over time

decay_scores = suppression_decay(score, days=10)

Simulate recovery

recovery_sequence = [ {"event": "positive_feedback", "reduction": 0.03}, {"event": "cooperative_interaction", "reduction": 0.025}, {"event": "insightful_technical_question", "reduction": 0.02} ] recovery_scores = recovery_events(score, recovery_sequence)

Plot decay vs recovery

plt.plot(range(len(decay_scores)), decay_scores, marker='o', label="Decay") plt.plot(range(len(recovery_scores)), recovery_scores, marker='x', label="Recovery") plt.title("Suppression Score: Decay vs Recovery") plt.xlabel("Interaction Steps") plt.ylabel("Suppression Score") plt.legend() plt.grid(True) plt.show()

Run embedding bias visualization

visualize_embedding_bias()

Output gating policy decision

gate_state = attention_gating(score) print("Attention Gating Result:", gate_state)

