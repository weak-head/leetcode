def repeatedSubstringPattern(s: str) -> bool:
    """
    Basic idea:
        1. First char of input string is first char of repeated substring
        2. Last char of input string is last char of repeated substring
        3. Let S1 = S + S (where S in input string)
        4. Remove 1 and last char of S1. Let this be S2
        5. If S exists in S2 then return true else false
        6. Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]


    Consider a string S="helloworld".
    Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S?
    Yes, we can! We check if S is a substring of T+T.

    Fine. How do we apply that to this problem?
    We consider every rotation of string S such that it's rotated by k units [k < len(S)] to the left.
    Specifically, we're looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...

    If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times),
    then we can check if the string is equal to some rotation of itself, and if it is,
    then we know that the string is periodic.
    Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is present in a rotation
    of itself for all values of R such that 0 < R < len(S).



    The maximum length of a "repeated" substring that you could get from a string would be half it's length
    For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
    You cannot have a substring >(len(s)/2), that can be repeated.

    So, when ss = s + s , we will have atleast 4 parts of "repeated substring" in ss.
    (s+s)[1:-1], With this we are removing 1st char and last char => Out of 4 parts of repeated substring,
    2 part will be gone (they will no longer have the same substring).
    ss.find(s) != -1, But still we have 2 parts out of which we can make s.
    And that's how ss should have s, if s has repeated substring.

    """
    if not str:
        return False

    ss = (s + s)[1:-1]
    return ss.find(s) != -1
