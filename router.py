import testFormInputs
import localdbOps

delimiter_dict = {
    "tab" : "\t",
    "comma":",",
    "semicolon":";",
    "none":""
}

async def test(file, delimiter, column, sid, config, log):
    config["column"] = column
    config["delimiter"] = delimiter_dict[delimiter]  #check for dict match else return undefined delimiter 
    await testFormInputs.check(file, config, log)    
    return config,log

async def bl_assertion(config, log): #localdb operations
    await localdbOps.bl_gen_digit_chart(config, log) 
    return config,log

async def push_to_client(config, log, master, sid):
    await localdbOps.update_json(config, log, master, sid)    
    await localdbOps.write_json(master)
    return master