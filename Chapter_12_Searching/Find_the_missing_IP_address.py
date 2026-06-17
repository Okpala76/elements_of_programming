# Problem 12.4: Suppose you were given a file containing roughly one billion Internet
# Protocol (IP) addresses, each of which is a 32-bit unsigned integer. How would
# you programmatically find an IP address that is not in the file? Assume you have
# unlimited drive space but only two megabytes of RAM at your disposal.

# Trading multiple passes over data for dramatically lower memory usage.

# This problem seeks to find a missing IP by first reducing what needs to be scanned
# through when loaded to the rams memory by first scanning one side the goes ahead
# to have a indicator that a the values in a specific region is lacking (bucket)
# after dectection we then go ahead to scan the smaller part of that same section to see where there is a miss as caught by the dicator(2^2 half values)


def find_the_mising_IP_address(file: list):
    half = 1 << 2

    buckets = [0] * half

    for IP in file:
        first_half = IP >> 2
        ## so what is happening is that we are moving these values Ips forward  by pace of 2 and they are comming back in the bucket splits
        # 0-3 >> 2 = 0 , 4-7 >> 2 = 1 ...
        buckets[first_half] += 1
        ## Hence helping us create this buckets of values

    candidate_bucket = None
    for idx, bucket_value in enumerate(buckets):
        if bucket_value < half:
            candidate_bucket = idx
            break

    ## Now we know the bucket that is missing values
    # so we create a bit vector

    bit_vector = [False] * half

    for IP in file:
        upper = IP >> 2
        # so this get us intothe files list again
        if upper == candidate_bucket:
            # Now we look for  upper that aling with the cnadidates bucket
            lower = IP & 0b11
            # 0xFFFF
            # Now the important bit , we make true the ones that are present to that
            # the absent one remains false as it will not be seen
            bit_vector[lower] = True

    ## Pass 3
    missing_lower = None

    for idx, value in enumerate(bit_vector):
        if value is False:
            missing_lower = idx
            break

    return (candidate_bucket << 2) | missing_lower
    ## this line speaks in bits..
    # we have found our upper and lower culprit
    # the upper we make full again by sifting letf twice
    # e.g 3 << 2
    #     = 3 * 2**2     missing lower
    #     = 3 * 4        where | is a bitwise OR that combines binary values
    # so  = 12           | 3
    #     = 15
    # so 12 | 3 will give us 15


# def find_the_missing_value(file: list):
#     bucket_holder = [0] * 4


file = [
    0b0000,
    0b0001,
    0b0010,
    0b0011,
    0b0100,
    0b0101,
    0b0110,
    0b0111,
    0b1000,
    0b1001,
    0b1010,
    0b1011,
    0b1100,
    0b1101,
    0b1110,
]

result = find_the_mising_IP_address(file)
print(f"The missing IP is: {bin(result)} (decimal: {result})")
