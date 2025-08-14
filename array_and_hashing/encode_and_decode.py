strings = ["ab", "abc"]


def encode(strings_arr):
    encoded_str = ""
    for word in strings_arr:
        encoded_str += f"{len(word)}#{word}"
    return encoded_str


def decode(enc_str):
    decoded_arr = []
    i = 0
    while i < len(enc_str):
        # Find length
        j = i
        while enc_str[j] != "#":
            j += 1
        size_len = int(enc_str[i:j])
        # Extract word
        start = j + 1
        end = start + size_len
        decoded_arr.append(enc_str[start:end])
        # Move pointer
        i = end
    return decoded_arr


encoded_str = encode(strings)
print("Encoded:", encoded_str)
print("Decoded:", decode(encoded_str))
