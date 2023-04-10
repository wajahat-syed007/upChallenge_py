import json
import pandas as pandas
from benfordslaw import benfordslaw

benfordslaw_dist = {
		"type": 'line',
        "label": 'Benfords Distribution',
        "data": [30.10, 17.61, 12.49, 9.69, 7.92, 6.69, 5.80, 5.12, 4.57], #Benfords distribution
        "borderWidth": 2,
		"borderColor": 'red'
      }
    
bl_chart_data= {
		"type":'bar',
        "label": 'Empirical Distribution',
        "data": [], #calculated distribution from the BL assertion will go here
        "borderWidth": 2,
		"borderColor": '#FFFF0',
        "result":"",        
    }

bl_details = {
}    

data = {
      "labels": ['1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0'],
      "datasets": [benfordslaw_dist,bl_chart_data],
      "bl_details":bl_details
    }   
  

async def write_json(master):
    json_object = json.dumps(master, indent=2)    
    with open("./db/localdb.json", "w") as outfile:
        try:
            outfile.write(json_object)
        except:
            master["log"]["resolution"] = "Unable to create file (write_json())"
            master["log"]["fail"] = "yes"
    return master
    
async def bl_gen_digit_chart(config, log): #get dataset from here
    path = config["path"] + config["filename"]
    datacolumn = pandas.read_csv(path, sep=config["delimiter"], usecols=[config["column"]])
    bl = benfordslaw(pos=1)
    results = bl.fit(datacolumn)
    #fig = bl.plot()  #internal library to generate all BL plots
    #print(fig)
    r = []
    for index, x in enumerate(results["percentage_emp"]):
        r.append(results["percentage_emp"][index][1])
    data["datasets"][1]["data"] = r
    bl_details["bl_result"] = "Anomaly detected: "+ str(results["P_significant"])
    bl_details["P"] = "P = " + str(results["P"])
    bl_details["Tstat"] = "Tstat = " + str(results["t"])
    bl_details["P_significant"] = "P_significant = " + str(results["P_significant"])
    #print(r)
    #df = pandas.read_csv(file.file, sep="\t", usecols=[2])

async def update_json(config, log, master, sid):
    session = {
        "chart" : data,
        "config" : config,
        "log" : log
        }
    x = {
       sid : session
       }
    master["sid"] = x
    #print(master)
    return master
