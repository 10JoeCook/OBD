import obd

con = obd.OBD()
for command in obd.commands.__mode1__:
    print(command.name, con.query(command))
