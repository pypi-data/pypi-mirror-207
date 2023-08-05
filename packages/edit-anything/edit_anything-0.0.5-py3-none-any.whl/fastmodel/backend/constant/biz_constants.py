import os

def app_abs_path():
    return os.path.dirname(os.path.abspath(__file__)).split("/backend")[0]

if __name__ == '__main__':
    print(app_abs_path())
