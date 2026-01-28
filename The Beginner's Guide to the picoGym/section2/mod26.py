C = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}"
shift = int(13)
M = ""
for c in C:
    code = ord(c)
    if c.islower():
        code = (code - ord('a') - shift) % 26 + ord('a')
    elif c.isupper():
        code = (code - ord('A') - shift) % 26 + ord('A')
    M += chr(code)
print(M)