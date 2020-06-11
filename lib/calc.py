#!/usr/local/bin/python
# coding:utf-8

import sys
import os
import io
import json
import yaml
import argparse
import pandas as pd

# 文字コード設定
sys.stdin  = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

class Main():
    """
    GeoJsonファイルから東西南北端を抽出し、yaml形式で標準出力する。
    """

    def __call__(self, input):

        with open(input, 'r') as inputfile, open('code.yml', 'r') as codefile:
            data = json.load(inputfile)
            code = yaml.safe_load(codefile)

            columns = ['longitude', 'latitude']
            points = pd.DataFrame(columns=columns)

            for feature in data["features"]:
                for coordinate in feature["geometry"]["coordinates"]:
                    c = pd.DataFrame(data=coordinate, columns=columns, dtype='float')
                    points = points.append(c)
                    points = points.reset_index(drop=True)

            # city_code = data["features"][0]["id"]
            city_code = os.path.splitext(os.path.basename(input))[0]
            for c in code:
                if city_code == c["code"]:
                    city_name = c["name"]
                    break

            north_idx = points['latitude'].idxmax()
            south_idx = points['latitude'].idxmin()
            east_idx = points['longitude'].idxmax()
            west_idx = points['longitude'].idxmin()

            print("- name: " + "\"" + city_name + "\"")
            print("  code: " + "\"" + city_code + "\"")
            print("  east:")
            print("    lat: " + str(points.iloc[east_idx]['latitude']))
            print("    lon: " + str(points.iloc[east_idx]['longitude']))
            print("  west:")
            print("    lat: " + str(points.iloc[west_idx]['latitude']))
            print("    lon: " + str(points.iloc[west_idx]['longitude']))
            print("  south:")
            print("    lat: " + str(points.iloc[south_idx]['latitude']))
            print("    lon: " + str(points.iloc[south_idx]['longitude']))
            print("  north:")
            print("    lat: " + str(points.iloc[north_idx]['latitude']))
            print("    lon: " + str(points.iloc[north_idx]['longitude']))

        return


if __name__ == '__main__':

    # 引数
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input file path')
    args = parser.parse_args()

    main = Main()
    main(args.input)

    exit()
