class Provider:
    def __init__(self, name):
        self.name = name
        self.feedback = {}  # client: score

    def add_feedback(self, client, score):
        self.feedback[client] = score

    def trust_score(self, client):
        return self.feedback.get(client, 0)

    def reputation(self):
        if len(self.feedback) == 0:
            return 0
        return sum(self.feedback.values()) / len(self.feedback)

    def __str__(self):
        return f"{self.name} | Reputation: {self.reputation():.2f}"


class TrustSystem:
    def __init__(self):
        self.providers = []

    def add_provider(self, provider):
        self.providers.append(provider)

    def best_provider(self):
        return max(self.providers, key=lambda p: p.reputation())


# Create providers
p1 = Provider("Provider A")
p2 = Provider("Provider B")
p3 = Provider("Provider C")

# Clients' feedback (client_name, score)
p1.add_feedback("Client1", 1)
p1.add_feedback("Client2", -1)
p1.add_feedback("Client3", 1)

p2.add_feedback("Client1", 1)
p2.add_feedback("Client2", 1)
p2.add_feedback("Client3", 1)

p3.add_feedback("Client1", -1)
p3.add_feedback("Client2", -1)

# Trust system
system = TrustSystem()
system.add_provider(p1)
system.add_provider(p2)
system.add_provider(p3)

# Display trust and reputation scores
for p in system.providers:
    print(f"{p.name} Feedback: {p.feedback}, Reputation: {p.reputation():.2f}")

# Find best provider
best = system.best_provider()
print("\nBest Provider:", best.name, "with Reputation:", round(best.reputation(), 2))
