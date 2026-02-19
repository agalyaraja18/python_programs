def normalize_name(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    s = " ".join(s.split())
    return s.title()
s=input("Enter the string: ")
print(normalize_name(s))
