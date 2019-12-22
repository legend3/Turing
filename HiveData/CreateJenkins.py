import jenkins

template_xml = "/root/.jenkins/jobs/JHIVE_Hive/config.xml/config.xml"

server = jenkins.Jenkins('http://192.168.0.58:8089/', username='admin', password='admin')

job_list = {
    "test1_": "59 00 * * *",
    "test2_spider": "59 01 * * *",
    "test3_spider": "59 02 * * *",
}

classify = 'JHive_Real'
host = 'http://192.168.0.4:8089/'
project = 'test_spider'

for spider_name, crontab in job_list.items():
    with open(template_xml) as f:
        profile = f.read()

    JOB_CONFIG = profile.replace("crontab_value", crontab) \
        .replace("spider_name", spider_name) \
        .replace("HOST_TEMPLATE", host) \
        .replace("PROJECT_TEMPLATE", project)

    print(JOB_CONFIG[-200:])

    view_name = "{}{}_".format(classify, type)
    server.create_job(view_name, JOB_CONFIG)
    # del_job=server.delete_job(view_name+name)
    # print(del_job)
print (u'success')