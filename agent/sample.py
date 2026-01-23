def insecure():
    username = "admin"
    password = "admin123"
    @234 # Intentional Syntax Error
    return eval("2 + 2")
