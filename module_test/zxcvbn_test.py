from zxcvbn import zxcvbn


password = "Example123!"
result = zxcvbn(password)

print(result)
score = result['score'] 
feedback = result['feedback']

print(f"Password score: {score}")
print(f"Feedback: {feedback}")