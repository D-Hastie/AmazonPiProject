from amazonproduct import API
api = API(locale='uk')
result = api.item_lookup('0198596790')
for item in result.Items.Item:
    print ASIN
