def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters = x[1::2]
    s = ' '

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]

    return s


def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]

    s = ''
    s = s + second_half
    s = s + first_half
    return s


print("------Hello everyone------")
print("----Welcome to word/sentence encoder----")

# in this loop you can encode any word or sentence 10 times only
for i in range(10):

    user_input = input(
        "Please write the word or sentence you want to be coded into a secret message\n")
    print("\nChoose your encoding method:")
    print("\n\t1. Even-Odd Swap (Swap every two adjancent letter)")
    print("\n\t2. Swap Middle (Splits the word exactly in half and moves the back half to front)")
    encoding_method_choice = int(input("\nPress 1 for option 1 or Press 2 for option 2: "))

    if encoding_method_choice == 1:
     encoded_evenodd_output = even_odd_swap(user_input)
     print("\nEncoded output is: ",encoded_evenodd_output)

    if encoding_method_choice == 2:
     encode_swapmiddle_output = swap_middle(user_input)
     print("\nEncoded output is: ",encode_swapmiddle_output)

    user_choice = input(
        "\npress enter to encode more word/sentence? or press 4 to exit: ")

    if user_choice == "4":
       print("Ok bye")
       break

print("\nTen word/sentences can be encoded at a time.")
