import os


def get_path(root, path, filename) -> str:
    """"""
    data_dir = os.getcwd().replace("\\", "/")
    data_file = os.path.join(data_dir, root, path, filename)
    return data_file


if __name__ == '__main__':
    code_path = "123.py"
    data_path = "123.csv"

    codes = get_path('resource', 'strategies', code_path)
    data = get_path('resource', 'data', data_path)
    output = get_path('resource', 'output', '')
    print(codes, data, output)
# run_backtest(codes, data, output, strategy_id, json.loads(settings))
