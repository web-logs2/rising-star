# coding: utf-8
import bytedtqs

app_id_boe = "HgfDEjJtAsNLWGyKNtc10vVAsOf2InD9L1uSk8Is957e3V5p"
app_key_boe = "89f3Jwlc65nGvsPPcaH3wHcMTmDXVOEKHmo4TOpUmyl1WrOY"
app_id_cn = "uRk0BRpeO0Rg3YO1cl93c5N94H7MdQR35tSQqEatKS8JirYw"
app_key_cn = "mwWtH38hmU7aoFN2eJtTCI5w9lkyuxofyerf5FkTrbj3Qskn"
app_id_lq = "Bs1HS1cAwFG19p0vi9KRj7D7rX3MzSbRso18aSK6QH1rILnU"
app_key_lq = "5jJC1tLQU9k211Bz1kp7Xu5TydDEkbgPuw60C5f8tL04QdqN"
user_name ="duanze"
cluster = bytedtqs.Cluster.BOE
bytedtqs.EngineType = 'presto'

client = bytedtqs.TQSClient(app_id_boe, app_key_boe, cluster)
sql = "select date2pdate('20220815')"
analyze_result = client.analyze_query(user_name, sql)
# conf = {'tqs.gbk.result.enabled':'true'}
if analyze_result.is_success():
    job = client.execute_query(user_name, sql)
    if job.is_success():
        result = job.get_result()
        print(result.fetch_all_data())
    else:
        print(job.analysis_error_message)
        print(job.query_error_url)
        print(job.query_log_url)
        print(job.tracking_urls)
else:
    print(analyze_result.error_message)

# job = client.get_job(7197675)
# result = job.get_result()
# print(job)
# print("2222222222"+result.result_url)
# print("333333333"+result.result_url_gbk)


