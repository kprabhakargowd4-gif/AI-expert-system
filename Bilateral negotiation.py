import random

# --- Parameters ---
TOTAL_RESOURCE = 100
MAX_ROUNDS = 10
discount_A = 0.9  # Agent A's discount factor
discount_B = 0.85  # Agent B's discount factor

# Initial offers (percentage of 100 units)
offer_A = 60  # A keeps 60, offers 40 to B
offer_B = 40  # B keeps 60, offers 40 to A

rounds = 0
agreement = False

print("Bilateral Negotiation Simulation\n")

while rounds < MAX_ROUNDS:
    rounds += 1
    print(f"Round {rounds}:")

    # Agent A makes an offer
    if rounds % 2 == 1:
        print(f"Agent A offers {offer_A} to self and {TOTAL_RESOURCE - offer_A} to Agent B.")
        # Agent B decides to accept if offer >= 50 for B
        if TOTAL_RESOURCE - offer_A >= 50:
            print("Agent B accepts the offer.\n")
            agreement = True
            final_share_A = offer_A * (discount_A ** rounds)
            final_share_B = (TOTAL_RESOURCE - offer_A) * (discount_B ** rounds)
            break
        else:
            print("Agent B rejects.\n")
            offer_A -= 5  # A concedes a bit next round

    # Agent B makes an offer
    else:
        print(f"Agent B offers {offer_B} to self and {TOTAL_RESOURCE - offer_B} to Agent A.")
        # Agent A accepts if A gets at least 50
        if TOTAL_RESOURCE - offer_B >= 50:
            print("Agent A accepts the offer.\n")
            agreement = True
            final_share_A = (TOTAL_RESOURCE - offer_B) * (discount_A ** rounds)
            final_share_B = offer_B * (discount_B ** rounds)
            break
        else:
            print("Agent A rejects.\n")
            offer_B -= 5  # B concedes

if agreement:
    print("✅ Agreement Reached!")
    print(f"Final Division: Agent A = {final_share_A:.2f}, Agent B = {final_share_B:.2f}")
    total = final_share_A + final_share_B
    print(f"Total Utility = {total:.2f}")
    print(f"Rounds Taken = {rounds}")
    # Nash-like fairness check: roughly equal utilities
    if abs(final_share_A - final_share_B) <= 5:
        print("🤝 The result is approximately Nash Fair.\n")
    else:
        print("⚖️ The result is not perfectly fair.\n")
else:
    print("❌ No agreement reached after maximum rounds.")
