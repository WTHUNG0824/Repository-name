
import requests

def get_realtime_price(stock):
    url=f"https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_{stock}.tw"
    r=requests.get(url,timeout=10).json()

    msg=r["msgArray"]
    if not msg:
        return None

    data=msg[0]

    return {
        "price":data.get("z"),
        "bid":data.get("b"),
        "ask":data.get("a"),
        "volume":data.get("v")
    }
