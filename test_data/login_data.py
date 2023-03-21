# save all test data on login

positive_cases = [
    {
        "title": "login successful, not select remember username",
        "data": {
            "username": "16442345896",
            "password": "123456",
            "remember": False
        }
    },
    {
        "title": "login successful, select remember username",
        "data": {
            "username": "16442345896",
            "password": "123456",
            "remember": True
        }
    },
]

native_cases = [
    {
        "title": "no username",
        "data": {"username": "", "password": "123456"},
        "error_msg": "Please input username."
    },
    {
        "title": "no password",
        "data": {"username": "16203458765", "password": ""},
        "error_msg": "Please input password."
    },

]
