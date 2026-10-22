
def correct_name(name: str) -> str:
    name =name.lower()
    return name[0].upper()+name[1:]

def check_email(email: str)-> bool:
    return not ("@" not in email or "." not in email)

if __name__ == "__main__":
    print(correct_name('вЛадимИр')) # noqa: T201
    print(check_email('email')) # noqa: T201
    print(check_email('email@mail.com')) # noqa: T201
