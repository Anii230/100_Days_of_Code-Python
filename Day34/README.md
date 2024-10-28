# Project 34: Custom Email Spammer

### Objective:
Extend the previous program to include an option to send customized email messages to the first 10 email addresses. The program should:
1. **Print Each Email Individually**: Display one email at a time with a pause before the next one.
2. **Clear the Screen**: After each email, clear the screen to create a dynamic effect.

### Steps:
1. **Create a List of Email Addresses**: Store a list of 10+ email addresses to represent recipients.
2. **Customize the Email Message**:
   - Use the recipient's email address or name in the message.
   - Use an f-string to personalize each email.
3. **Display Each Email**:
   - Use a `for` loop to iterate over the first 10 emails.
   - Print each email, add a pause using `time.sleep()`, then clear the screen with `os.system("clear")` (or `cls` on Windows).

```plaintext
Dear john@test.com
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III
```
---

## Output:
