def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def classify_number(n):
    classification = {}

    # Positive / Negative / Zero
    if n > 0:
        classification["sign"] = "Positive"
    elif n < 0:
        classification["sign"] = "Negative"
    else:
        classification["sign"] = "Zero"
        classification["prime"] = "Not Applicable"
        classification["perfect"] = "Not Applicable"
        classification["even_odd"] = "Even"
        return classification

    # Even / Odd
    classification["even_odd"] = "Even" if n % 2 == 0 else "Odd"

    # Prime / Composite
    if is_prime(n):
        classification["prime"] = "Prime"
    else:
        classification["prime"] = "Composite"

    # Perfect / Abundant / Deficient
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if n // i != i:
                sum_div += n // i

    if n == 1:
        classification["perfect"] = "Deficient"
    else:
        if sum_div == n:
            classification["perfect"] = "Perfect"
        elif sum_div > n:
            classification["perfect"] = "Abundant"
        else:
            classification["perfect"] = "Deficient"

    return classification


# Main Program
num = int(input("Enter a number: "))
result = classify_number(num)

print("\n----- Number Classification -----")
for key, value in result.items():
    print(f"{key.capitalize()} : {value}")
