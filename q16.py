text = input("enter a text :")

cleantxt = text.replace( "  ","")

if cleantxt ==cleantxt[::1]:
    print('  palindrome')
else:
    print("text is not planindrome ")
    