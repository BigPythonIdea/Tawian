# Taiwan Public Information Website CPA Audit Report Project

日期：2023年5月29日

紀錄人：Mooncat

## 專案檔說明

| 專案名稱| 說明| 備註 |
| -------- | -------- | -------- |
| get_stock_list.py    | 取得公司代號/名稱    | 爬蟲1 |
| get_account_data.py    | 取得會計師稽核文本   | 要先執行爬蟲1才能用 |
| requirements.txt   | 環境需求 |  |
| stockdb.sql | 文本資料庫 | 直接可以使用 |
| get_similarity_score.py| 相似度對比 | [移動這裡](https://github.com/BigPythonIdea/Tawian/blob/master/NLP/%E5%A4%A7%E5%9E%8B%E8%AA%9E%E8%A8%80%E6%A8%A1%E5%9E%8B/get_similarity_score.py)|
| Diagram 1.jpg   | ER Model     | 爬蟲1 |

## 系統環境

* python 3.10
* MySql 8.0

## 開發環境

* vscode

## 建置作業

* 先從requirements.txt 中安裝必要套件

* MySQL 安裝好把db匯入就能使用，如果要增修參考檔[檔案1](https://github.com/BigPythonIdea/Tawian/blob/master/get_stock_list.py)、[檔案2](https://github.com/BigPythonIdea/Tawian/blob/master/get_account_data.py)

* 如果要抓其他年份從檔案2中做更改
* 直接clone就能用了

## 其他說明

* 包含項目: 109 110 111 Q1~Q4 會計師稽核報告

* 抓取來源: 公開資訊站 會計師查核(核閱)報告

## 注意事項

* 預估抓取時間是30小時以上，作者CPU是AMD 5600x，依照效能不同抓取時間也不相同

## 技術總結

1. 爬蟲抓取公司資料

2. 建置MySQL資料庫

3. 使用CKIP中的大型語言模型bert斷詞

4. TF-IDF + COSINE 計算文本相似度

## 未來代辦事項：
- [ ] 採用幾種不同的NLP技術，並將其應用在會計師稽核報告的分析中，比較其結果差異。
- [ ] 補充文獻
- [ ] 建置Docker Linux平台


