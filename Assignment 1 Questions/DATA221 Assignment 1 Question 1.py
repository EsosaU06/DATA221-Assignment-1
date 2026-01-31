def MultiplyUntilThreshold(threshold):
    multiplier = 1
    product = 1
    while product < threshold:
        multiplier += 1
        # print(f"{product} * {multiplier}", end="")
        product = product * multiplier
        # print(f" = {product}")
        # does the calculations equivalent to "1x2x3x4..."
        # commented print statements make the calculations more clear
        
    print("Final product: ", product)
    print("Integer caused to the prouct to exceed the threshold:", multiplier)

# example code:
# MultiplyUntilThreshold(100)