# Project 28: Battle System Game

Build an automated battle system using the character generator from Day 27!

### Instructions:
1. **Return Functions**: Modify your character generator to include return functions for health and strength.
2. **Generate Two Characters**: Create two unique characters and store their details (health, strength, name, type, etc.).
3. **Battle Simulation**: Use a `while True` loop to simulate rounds of battle between these two characters:
   - **Roll Dice**: Roll a six-sided dice for each character. The character with the higher roll wins that round.
   - **Apply Damage**: Calculate the damage as `(strength difference + 1)`, and deduct this from the loser’s health.
4. **Check Health**: After each round, check both characters' health:
   - If a character’s health is zero or below, they’ve died. Declare the surviving character as the winner!

5. **Screen Clear and Pause**: Use `time.sleep()` to add a delay and `os.system("clear")` to clear the screen between rounds for a cleaner look.

### Extra Challenge:
- **Add Colors and Emojis** for character reactions, damage, or winning announcements.
- **Add Sound Effects** for attacks and wins.

This should give you a fun, automated battle game. Enjoy coding your battles! 🎮⚔️🎲

---
## Output:
