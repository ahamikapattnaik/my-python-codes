# Create a function that would get you binomial coefficients for any (ax + b)^n

def binomial_coefficients(a, b, n):
    coefficients = [1]

    for i in range(1, n + 1):
        next_coefficients = []
        next_coefficients.append(1)

        for j in range(1, i):
            next_coefficients.append(coefficients[j - 1] + coefficients[j])

        next_coefficients.append(1)
        coefficients = next_coefficients

    return coefficients


def binomial_expansion(a, b, n):
    coefficients = binomial_coefficients(a, b, n)
    expansion = ""

    for i in range(n + 1):
        coefficient = coefficients[i]
        term = coefficient * (a ** (n - i)) * (b ** i)

        if term != 0:
          if i != n:
            sign = "+" if term > 0 else "-"  #sign of the term

            expansion += f" {sign} {abs(term)}x^{n - i}"
          else:
            expansion += f" + {term}" if term > 0 else f" - {-term}"  #include last term with sign

    return expansion

# Build the calculator

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
n = int(input("Enter the value of n: "))

result = binomial_expansion(a, b, n)
print(f"Input: ({a}x + {b})^{n}")
print("Output:",result)
