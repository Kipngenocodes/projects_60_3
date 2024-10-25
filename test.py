# test_cgi.py
try:
    import cgi
    print("cgi module is available.")
except ImportError as e:
    print(f"Error: {e}")
