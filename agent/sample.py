def insecure():
    username = "admin"
    password = "admin123"
    @123 # Intentional Syntax Error
    return eval("2 + 2")
