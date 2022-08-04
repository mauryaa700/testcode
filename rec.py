import pymongo

client = pymongo.MongoClient("mongodb+srv://Maurya247:Amauryaa1998@cluster0.3jjdk3k.mongodb.net/?retryWrites=true&w=majority")
db = client.test

dataset=[

    {"name": "ashish",
    "mail":"mauryaa@gmail.com",
    "subject":"FSDS"},
    {"name": "orgha",
    "mail":"argha@gmail.com",
    "subject":"PMP"},
    {"name": "Jitesh",
    "mail":"jitesh@gmail.com",
    "subject":"AWS"},
    {"name": "Nimit",
    "mail":"nimit@gmail.com",
    "subject":"OCI"}

]

dataset1=[
 {"name":"Aachen","id":1,"nametype":"Valid","recclass":"L5","mass":"21","fall":"Fell","year":"1880-01-01T00:00:00.000","reclat":"50.775000","reclong":"6.083330","geolocation":{"type":"Point","coordinates":[6.08333,50.775]}}
,{"name":"Aarhus","id":2,"nametype":"Valid","recclass":"H6","mass":"720","fall":"Fell","year":"1951-01-01T00:00:00.000","reclat":"56.183330","reclong":"10.233330","geolocation":{"type":"Point","coordinates":[10.23333,56.18333]}}
,{"name":"Abee","id":6,"nametype":"Valid","recclass":"EH4","mass":"107000","fall":"Fell","year":"1952-01-01T00:00:00.000","reclat":"54.216670","reclong":"-113.000000","geolocation":{"type":"Point","coordinates":[-113,54.21667]}}
,{"name":"Acapulco","id":10,"nametype":"Valid","recclass":"Acapulcoite","mass":"1914","fall":"Fell","year":"1976-01-01T00:00:00.000","reclat":"16.883330","reclong":"-99.900000","geolocation":{"type":"Point","coordinates":[-99.9,16.88333]}}
,{"name":"Achiras","id":370,"nametype":"Valid","recclass":"L6","mass":"780","fall":"Fell","year":"1902-01-01T00:00:00.000","reclat":"-33.166670","reclong":"-64.950000","geolocation":{"type":"Point","coordinates":[-64.95,-33.16667]}}
,{"name":"Adhi Kot","id":379,"nametype":"Valid","recclass":"EH4","mass":"4239","fall":"Fell","year":"1919-01-01T00:00:00.000","reclat":"32.100000","reclong":"71.800000","geolocation":{"type":"Point","coordinates":[71.8,32.1]}}
,{"name":"Adzhi-Bogdo (stone)","id":390,"nametype":"Valid","recclass":"LL3-6","mass":"910","fall":"Fell","year":"1949-01-01T00:00:00.000","reclat":"44.833330","reclong":"95.166670","geolocation":{"type":"Point","coordinates":[95.16667,44.83333]}}
,{"name":"Agen","id":392,"nametype":"Valid","recclass":"H5","mass":"30000","fall":"Fell","year":"1814-01-01T00:00:00.000","reclat":"44.216670","reclong":"0.616670","geolocation":{"type":"Point","coordinates":[0.61667,44.21667]}}
,{"name":"Aguada","id":398,"nametype":"Valid","recclass":"L6","mass":"1620","fall":"Fell","year":"1930-01-01T00:00:00.000","reclat":"-31.600000","reclong":"-65.233330","geolocation":{"type":"Point","coordinates":[-65.23333,-31.6]}}
,{"name":"Aguila Blanca","id":417,"nametype":"Valid","recclass":"L","mass":"1440","fall":"Fell","year":"1920-01-01T00:00:00.000","reclat":"-30.866670","reclong":"-64.550000","geolocation":{"type":"Point","coordinates":[-64.55,-30.86667]}}
,{"name":"Aioun el Atrouss","id":423,"nametype":"Valid","recclass":"Diogenite-pm","mass":"1000","fall":"Fell","year":"1974-01-01T00:00:00.000","reclat":"16.398060","reclong":"-9.570280","geolocation":{"type":"Point","coordinates":[-9.57028,16.39806]}}
,{"name":"Aïr","id":424,"nametype":"Valid","recclass":"L6","mass":"24000","fall":"Fell","year":"1925-01-01T00:00:00.000","reclat":"19.083330","reclong":"8.383330","geolocation":{"type":"Point","coordinates":[8.38333,19.08333]}}
,{"name":"Aire-sur-la-Lys","id":425,"nametype":"Valid","recclass":"Unknown","fall":"Fell","year":"1769-01-01T00:00:00.000","reclat":"50.666670","reclong":"2.333330","geolocation":{"type":"Point","coordinates":[2.33333,50.66667]}}
,{"name":"Akaba","id":426,"nametype":"Valid","recclass":"L6","mass":"779","fall":"Fell","year":"1949-01-01T00:00:00.000","reclat":"29.516670","reclong":"35.050000","geolocation":{"type":"Point","coordinates":[35.05,29.51667]}}
,{"name":"Akbarpur","id":427,"nametype":"Valid","recclass":"H4","mass":"1800","fall":"Fell","year":"1838-01-01T00:00:00.000","reclat":"29.716670","reclong":"77.950000","geolocation":{"type":"Point","coordinates":[77.95,29.71667]}}
,{"name":"Akwanga","id":432,"nametype":"Valid","recclass":"H","mass":"3000","fall":"Fell","year":"1959-01-01T00:00:00.000","reclat":"8.916670","reclong":"8.433330","geolocation":{"type":"Point","coordinates":[8.43333,8.91667]}}
,{"name":"Akyumak","id":433,"nametype":"Valid","recclass":"Iron, IVA","mass":"50000","fall":"Fell","year":"1981-01-01T00:00:00.000","reclat":"39.916670","reclong":"42.816670","geolocation":{"type":"Point","coordinates":[42.81667,39.91667]}}
,{"name":"Al Rais","id":446,"nametype":"Valid","recclass":"CR2-an","mass":"160","fall":"Fell","year":"1957-01-01T00:00:00.000","reclat":"24.416670","reclong":"39.516670","geolocation":{"type":"Point","coordinates":[39.51667,24.41667]}}
,{"name":"Al Zarnkh","id":447,"nametype":"Valid","recclass":"LL5","mass":"700","fall":"Fell","year":"2001-01-01T00:00:00.000","reclat":"13.660330","reclong":"28.960000","geolocation":{"type":"Point","coordinates":[28.96,13.66033]}}
,{"name":"Alais","id":448,"nametype":"Valid","recclass":"CI1","mass":"6000","fall":"Fell","year":"1806-01-01T00:00:00.000","reclat":"44.116670","reclong":"4.083330","geolocation":{"type":"Point","coordinates":[4.08333,44.11667]}}
,{"name":"Albareto","id":453,"nametype":"Valid","recclass":"L/LL4","mass":"2000","fall":"Fell","year":"1766-01-01T00:00:00.000","reclat":"44.650000","reclong":"11.016670","geolocation":{"type":"Point","coordinates":[11.01667,44.65]}}
,{"name":"Alberta","id":454,"nametype":"Valid","recclass":"L","mass":"625","fall":"Fell","year":"1949-01-01T00:00:00.000","reclat":"2.000000","reclong":"22.666670","geolocation":{"type":"Point","coordinates":[22.66667,2]}}
,{"name":"Alby sur Chéran","id":458,"nametype":"Valid","recclass":"Eucrite-mmict","mass":"252","fall":"Fell","year":"2002-01-01T00:00:00.000","reclat":"45.821330","reclong":"6.015330","geolocation":{"type":"Point","coordinates":[6.01533,45.82133]}}
]
dataset2=[
 {"name":"Aachen","id":1,"nametype":"Valid","recclass":"L5","mass":"21","fall":"Fell","year":"1880-01-01T00:00:00.000","reclat":"50.775000","reclong":"6.083330","geolocation":{"type":"Point","coordinates":[6.08333,50.775]}}
,{"name":"Aarhus","id":2,"nametype":"Valid","recclass":"H6","mass":"720","fall":"Fell","year":"1951-01-01T00:00:00.000","reclat":"56.183330","reclong":"10.233330","geolocation":{"type":"Point","coordinates":[10.23333,56.18333]}}
,{"name":"Abee","id":6,"nametype":"Valid","recclass":"EH4","mass":"107000","fall":"Fell","year":"1952-01-01T00:00:00.000","reclat":"54.216670","reclong":"-113.000000","geolocation":{"type":"Point","coordinates":[-113,54.21667]}}
,{"name":"Acapulco","id":10,"nametype":"Valid","recclass":"Acapulcoite","mass":"1914","fall":"Fell","year":"1976-01-01T00:00:00.000","reclat":"16.883330","reclong":"-99.900000","geolocation":{"type":"Point","coordinates":[-99.9,16.88333]}}
,{"name":"Achiras","id":370,"nametype":"Valid","recclass":"L6","mass":"780","fall":"Fell","year":"1902-01-01T00:00:00.000","reclat":"-33.166670","reclong":"-64.950000","geolocation":{"type":"Point","coordinates":[-64.95,-33.16667]}}
,{"name":"Adhi Kot","id":379,"nametype":"Valid","recclass":"EH4","mass":"4239","fall":"Fell","year":"1919-01-01T00:00:00.000","reclat":"32.100000","reclong":"71.800000","geolocation":{"type":"Point","coordinates":[71.8,32.1]}}
,{"name":"Adzhi-Bogdo (stone)","id":390,"nametype":"Valid","recclass":"LL3-6","mass":"910","fall":"Fell","year":"1949-01-01T00:00:00.000","reclat":"44.833330","reclong":"95.166670","geolocation":{"type":"Point","coordinates":[95.16667,44.83333]}}
,{"name":"Agen","id":392,"nametype":"Valid","recclass":"H5","mass":"30000","fall":"Fell","year":"1814-01-01T00:00:00.000","reclat":"44.216670","reclong":"0.616670","geolocation":{"type":"Point","coordinates":[0.61667,44.21667]}}
,{"name":"Aguada","id":398,"nametype":"Valid","recclass":"L6","mass":"1620","fall":"Fell","year":"1930-01-01T00:00:00.000","reclat":"-31.600000","reclong":"-65.233330","geolocation":{"type":"Point","coordinates":[-65.23333,-31.6]}}
,{"name":"Aguila Blanca","id":417,"nametype":"Valid","recclass":"L","mass":"1440","fall":"Fell","year":"1920-01-01T00:00:00.000","reclat":"-30.866670","reclong":"-64.550000","geolocation":{"type":"Point","coordinates":[-64.55,-30.86667]}}
,{"name":"Aioun el Atrouss","id":423,"nametype":"Valid","recclass":"Diogenite-pm","mass":"1000","fall":"Fell","year":"1974-01-01T00:00:00.000","reclat":"16.398060","reclong":"-9.570280","geolocation":{"type":"Point","coordinates":[-9.57028,16.39806]}}
,{"name":"Aïr","id":424,"nametype":"Valid","recclass":"L6","mass":"24000","fall":"Fell","year":"1925-01-01T00:00:00.000","reclat":"19.083330","reclong":"8.383330","geolocation":{"type":"Point","coordinates":[8.38333,19.08333]}}
,{"name":"Aire-sur-la-Lys","id":425,"nametype":"Valid","recclass":"Unknown","fall":"Fell","year":"1769-01-01T00:00:00.000","reclat":"50.666670","reclong":"2.333330","geolocation":{"type":"Point","coordinates":[2.33333,50.66667]}}
,{"name":"Akaba","id":426,"nametype":"Valid","recclass":"L6","mass":"779","fall":"Fell","year":"1949-01-01T00:00:00.000","reclat":"29.516670","reclong":"35.050000","geolocation":{"type":"Point","coordinates":[35.05,29.51667]}}
,{"name":"Akbarpur","id":427,"nametype":"Valid","recclass":"H4","mass":"1800","fall":"Fell","year":"1838-01-01T00:00:00.000","reclat":"29.716670","reclong":"77.950000","geolocation":{"type":"Point","coordinates":[77.95,29.71667]}}
,{"name":"Akwanga","id":432,"nametype":"Valid","recclass":"H","mass":"3000","fall":"Fell","year":"1959-01-01T00:00:00.000","reclat":"8.916670","reclong":"8.433330","geolocation":{"type":"Point","coordinates":[8.43333,8.91667]}}
,{"name":"Akyumak","id":433,"nametype":"Valid","recclass":"Iron, IVA","mass":"50000","fall":"Fell","year":"1981-01-01T00:00:00.000","reclat":"39.916670","reclong":"42.816670","geolocation":{"type":"Point","coordinates":[42.81667,39.91667]}}
,{"name":"Al Rais","id":446,"nametype":"Valid","recclass":"CR2-an","mass":"160","fall":"Fell","year":"1957-01-01T00:00:00.000","reclat":"24.416670","reclong":"39.516670","geolocation":{"type":"Point","coordinates":[39.51667,24.41667]}}
,{"name":"Al Zarnkh","id":447,"nametype":"Valid","recclass":"LL5","mass":"700","fall":"Fell","year":"2001-01-01T00:00:00.000","reclat":"13.660330","reclong":"28.960000","geolocation":{"type":"Point","coordinates":[28.96,13.66033]}}
,{"name":"Alais","id":448,"nametype":"Valid","recclass":"CI1","mass":"6000","fall":"Fell","year":"1806-01-01T00:00:00.000","reclat":"44.116670","reclong":"4.083330","geolocation":{"type":"Point","coordinates":[4.08333,44.11667]}}
,{"name":"Albareto","id":453,"nametype":"Valid","recclass":"L/LL4","mass":"2000","fall":"Fell","year":"1766-01-01T00:00:00.000","reclat":"44.650000","reclong":"11.016670","geolocation":{"type":"Point","coordinates":[11.01667,44.65]}}
,{"name":"Alberta","id":454,"nametype":"Valid","recclass":"L","mass":"625","fall":"Fell","year":"1949-01-01T00:00:00.000","reclat":"2.000000","reclong":"22.666670","geolocation":{"type":"Point","coordinates":[22.66667,2]}}
,{"name":"Alby sur Chéran","id":458,"nametype":"Valid","recclass":"Eucrite-mmict","mass":"252","fall":"Fell","year":"2002-01-01T00:00:00.000","reclat":"45.821330","reclong":"6.015330","geolocation":{"type":"Point","coordinates":[6.01533,45.82133]}}
]
database = client['myinfo']
#collection=database["ashu"]
#collection1=database["dpkg"]
collection2=database["data"]
#collection.insert_one(data)
#collection.insert_many(dataset)
#collection1.insert_many(dataset1)
collection2.insert_many(dataset2)

