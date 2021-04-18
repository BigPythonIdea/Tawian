import pandas as pd

url = pd.read_html("<Your url>")
df = pd.DataFrame(url[0]["代碼"])
df.to_csv("<Name>")
