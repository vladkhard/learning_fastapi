def index():
    value = 0
    def increase():
        nonlocal value
        value += 1
        return value
    return increase

generate_id = index()
