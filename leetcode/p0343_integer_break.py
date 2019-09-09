def integer_break(n):
    """
    Dynamic programming
    O(n^2)
    """

    products = [0] * (n + 1)
    products[1] = 1

    for current_integer in range(2, n + 1):
        for part in range(1, current_integer):

            # multiply two numbers
            two_product = part * (current_integer - part)
            # multiply the 'part' with the aggregated product
            aggregated_product = part * (products[current_integer - part])
            max_product = max(two_product, aggregated_product)

            products[current_integer] = max(products[current_integer], max_product)

    return products[n]
