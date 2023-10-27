def check_age(age):
    if age < 18:
        return 'You are a teenager'
    else:
        return 'You are an adult'

if __name__ == '__main__':
    print(check_age(20))  # Expected: You are an adult
    print(check_age(16))  # Expected: You are a teenager
