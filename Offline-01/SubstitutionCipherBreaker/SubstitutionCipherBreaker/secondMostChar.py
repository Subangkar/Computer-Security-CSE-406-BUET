text = "THQVHAQCYCSPMAWARNTLNRTAVQUOEQWWNPQRTZQEYAWARTHQTENARTHQTENARKALLONWWMFINOQWTNTCAXQINKRVEQNTQTHQNXNLNRVHQKHQRTHQTENARLQNXQWTHQWTNTAYR"


def char_count(str):
    counts = dict()
    words = str.split()

    for char in str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    counts_ordered = sorted(counts.items(), key=lambda kv: kv[1])
    # print(counts_ordered)
    # return counts_ordered[-2]
    return counts_ordered


# print(char_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))
# print()
list_chars = char_count(text)

# for char_i in reversed(list_chars):
#     print(char_i[0], end=' ')
#     print(char_i[1], end='\n')
