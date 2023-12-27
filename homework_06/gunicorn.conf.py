preload_app = True

workers = 2

threads = 4

timeout = 60

bind = '0.0.0.0:5000'

forwarded_allow_ips = '*'

secure_scheme_headers = {'X-Forwarded-Proto': 'https'}

wsgi_app = "app:app"
