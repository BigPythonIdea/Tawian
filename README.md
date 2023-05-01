# Taiwan Public Information Website CPA Audit Report Project

日期：2023年5月1日

紀錄人：Mooncat

資料庫: stockdb.sql

包含項目: 109 110 111 Q1~Q4 會計師稽核報告

抓取來源: 公開資訊站 會計師查核(核閱)報告

爬蟲檔案 1: get_stock_list.py 

爬蟲檔案 2: get_account_data.py

※ 檔案1 先抓公司代碼以及名稱

※ 檔案2 抓取會計師稽核報告

---

## 使用說明

* 先從requirements.txt 中安裝必要套件

* MySQL 安裝好把db匯入就能使用，如果要增修參考檔案1、2

* 如果要抓其他年份從檔案2中做更改

---
## 注意事項

* 預估抓取時間是30小時以上，作者CPU是AMD 5600x，依照效能不同抓取時間也不相同
---
## 未來代辦事項：

☐ 採用幾種不同的NLP技術，並將其應用在會計師稽核報告的分析中，比較其結果差異。
