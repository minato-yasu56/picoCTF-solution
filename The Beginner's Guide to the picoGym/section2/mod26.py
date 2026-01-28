C = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}"
shift = int(13)
M = ""
for c in C:
    code = ord(c)
    if c.islower():
        # a ~ z : 0 ~ 25
        # c の場合 (99[c] - 97[a] - 13) % 26 = 15
        # 15 + 97 = 112 => p
        code = (code - ord('a') - shift) % 26 + ord('a')
    elif c.isupper():
        # A ~ Z : 0 ~ 25
        code = (code - ord('A') - shift) % 26 + ord('A')
    M += chr(code)
print(M)