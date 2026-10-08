
def decoder_3_to_8(a, b, c):
    inputs = (a, b, c)

    outputs = [0] * 8

    index = a * 4 + b * 2 + c
    outputs[index] = 1

    return outputs


print("3-to-8 Decoder")
print("----------------")

a = int(input("Enter A (0 or 1): "))
b = int(input("Enter B (0 or 1): "))
c = int(input("Enter C (0 or 1): "))

if a in [0, 1] and b in [0, 1] and c in [0, 1]:
    outputs = decoder_3_to_8(a, b, c)

    print("\nInputs:")
    print(f"A = {a}, B = {b}, C = {c}")

    print("\nOutputs:")
    for i, value in enumerate(outputs):
        print(f"Y{i} = {value}")
else:
    print("Invalid input! Please enter only 0 or 1.")
