def check_strength(pwd: str, min_len=8) -> dict:
    length_ok = len(pwd) >= min_len
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    checks = {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
    }
    checks["score"] = sum(checks.values())
    return checks
pwd=input("Enter your password with 8 characters: ")
print(check_strength(pwd))