#test for extension
#test if file is empty
#test for delimiter
#test for columns
#test for numbers in the column
#Check the behavior of single column with the right data

import pandas as pandas

async def check(file, config, log):
    #print(log)
    if(file.filename.lower().endswith('.csv')):
        config["filename"] = file.filename
        await check_delimiter(file, config, log)          
    else:
        log["error"] = "Attached file has incorrect extension";
        log["resolution"] = "App supports csv extension only";
        log["fail"] = "yes"; 
    return config,log

async def check_delimiter(file, config, log):
    dataset = pandas.read_csv(file.file, sep=config["delimiter"])
    total_cols=len(dataset.axes[1])
    if(total_cols > 1):
        await check_column_name(dataset, config, log)
    else:
        log["error"] = "The delimiter selected in incorrect";
        log["resolution"] = "Please select the correct delimiter from the menu ";
        log["fail"] = "yes";
    return config,log  

async def check_column_name(dataset, config, log):
    if(config["column"] in dataset.keys()):
        await check_column_data(dataset, config, log)
    else:
        log["error"] = "The entered column name is incorrect";
        log["resolution"] = "ReCheck the column name";
        log["fail"] = "yes";
    return config,log          

async def check_column_data(dataset, config, log):
    datacolumn = dataset[config["column"]]
    column_datatype = datacolumn.dtype
    if(column_datatype == "int64"):
        await store_db(datacolumn, config, log)
    else:
        log["error"] = "The column selected has mixed data";
        log["resolution"] = "Ensure selected column has only numbers and no alphabets";
        log["fail"] = "yes";
    return config,log   

async def store_db(datacolumn, config, log):
    print(datacolumn)
    log["error"] = "None";
    log["resolution"] = "None";
    log["fail"] = "no";    
    return  config,log

