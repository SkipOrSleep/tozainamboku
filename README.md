tozainamboku
============

このアプリは、FlaskによるAPI I/F開発の技術検証を目的としたものです。次の機能を含みます：

- 都道府県名・市区町村名を入力とし、その自治体の東西南北端の経緯度を返す
- 地方公共団体コードを入力とし、その自治体の東西南北端の経緯度を返す

なお、オリジナルのGeoJsonデータと地方公共団体コードのデータは、[こちら](https://github.com/niiyz/JapanCityGeoJson)を利用しました。

また東西南北端点の経緯度については、より直接的で正確なデータが国土地理院から提供されていることも付記しておきます。
- [東京都](https://www.gsi.go.jp/KOKUJYOHO/CENTER/kendata/tokyo_heso.pdf)
- [神奈川県](https://www.gsi.go.jp/KOKUJYOHO/CENTER/kendata/kanagawa_heso.pdf)