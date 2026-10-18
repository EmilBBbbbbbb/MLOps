
def correct_name(name: str) -> str:
    name =name.lower()
    return name[0].upper()+name[1:]

if __name__ == "__main__":
    print(correct_name('вЛадимИр')) # noqa: T201
