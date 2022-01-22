import time
import obd


def connection_time_test(attempts: int) -> time:
    total_time = 0
    for i in range(attempts):
        start_time = time.perf_counter()
        con = obd.OBD()
        end_time = time.perf_counter()
        total_time += end_time - start_time
        con.close()
    return total_time / attempts


def query_time_test(test_query: obd.OBDCommand, attempts: int) -> time:
    con = obd.OBD()
    total_time = 0
    for i in range(1000):
        start_time = time.perf_counter()
        resp = con.query(test_query)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return total_time / attempts


def speed_multi_query_test(test_query: obd.OBDCommand, queries: int, attempts: int) -> time:
    con = obd.OBD()
    total_time = 0
    for i in range(1000):
        start_time = time.perf_counter()
        for j in range(queries):
            resp = con.query(test_query)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return total_time / attempts


ATTEMPTS = 10
NO_QUERIES = 10
conn = obd.OBD()
print("-----Connection Time-----")
print("Connection Time:", connection_time_test(ATTEMPTS))
print("-----RPM Results-----")
print("Res: ", conn.query(obd.commands.RPM))
print("Single: ", query_time_test(obd.commands.RPM, ATTEMPTS))
print("Multi", speed_multi_query_test(obd.commands.RPM, NO_QUERIES, ATTEMPTS))
print("-----Speed Results-----")
print("Res: ", conn.query(obd.commands.SPEED))
print("Single: ", query_time_test(obd.commands.SPEED, ATTEMPTS))
print("Multi", speed_multi_query_test(obd.commands.SPEED, NO_QUERIES, ATTEMPTS))
print("-----Oil Temp Results-----")
print("Res: ", conn.query(obd.commands.OIL_TEMP))
print("Single: ", query_time_test(obd.commands.OIL_TEMP, ATTEMPTS))
print("Multi", speed_multi_query_test(obd.commands.OIL_TEMP, NO_QUERIES, ATTEMPTS))
conn.close()
print("-----END-----")
