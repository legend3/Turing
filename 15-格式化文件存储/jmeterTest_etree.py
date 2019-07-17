from lxml import etree as xee

Project = xee.Element("project")
# xmlFile._setroot(e)#替换根
Project.set('name','ant-jmeter-test')
Project.set('default','all')
Project.set('basedir','.')
Tstamp = xee.SubElement(Project,'tstamp')
Format = xee.SubElement(Tstamp,'format')
Format.set('property','time')
Format.set('pattern','yyyy/MM/dd/hh/mm')

propertylist = [{'name':'jmeter.home','value':'E:\\apache-jmeter-5.1'},
                {'name':'jmeter.result.jtl.dir','value':'E:\\BigData\\Hive\\jtl'},
                {'name':'jmeter.result.html.dir','value':'E:\\BigData\\Hive\\html'},
                {'name':'ReportName','value':'TestReport'},
                {'name':'jmeter.result.jtlName','value':'${jmeter.result.jtl.dir}/${ReportName}.jtl'},
                {'name':'jmeter.result.htmlName','value':'${jmeter.result.html.dir}/${ReportName}.html'}]

for p in propertylist:
    Property = xee.SubElement(Project,"property")
    Property.set('name',p['name'])
    Property.set('value',p['value'])

targetList = [{'name':'all'},
              {'name':'test'},
              {'name':'report'}]

antcallList = [{'target':'test'},
           {'target':'report'}]

includeList = [{'name':'collapse.png'},
               {'name':'expand.png'}]

for t in targetList:
    Target = xee.SubElement(Project,"target")
    Target.set('name',t['name'])

    if t['name']=='all':
        for a in antcallList:
            antcall = xee.SubElement(Target,"antcall")
            antcall.set('target',a['target'])
    elif t['name']=='test':
        taskdef = xee.SubElement(Target,"taskdef")
        jmeter = xee.SubElement(Target,"jmeter")
        testplans = xee.SubElement(jmeter,"testplans")
        taskdef.set('name', 'jmeter')
        taskdef.set('classname', 'org.programmerplanet.ant.taskdefs.jmeter.JMeterTask')
        jmeter.set('jmeterhome', '${jmeter.home}')
        jmeter.set('resultlog', '${jmeter.result.jtlName}')
        testplans.set('dir', '/Users/yq519/Documents/jmeter/')
        testplans.set('includes', '*.jmx')
    elif t['name']=='report':
        xslt = xee.SubElement(Target,"xslt")
        copy = xee.SubElement(Target,"copy")
        fileset = xee.SubElement(copy,"fileset")
        xslt.set('in', '${jmeter.result.jtlName}')
        xslt.set('out', '${jmeter.result.htmlName}')
        xslt.set('style', '${jmeter.home}/extras/jmeter-results-detail-report_21.xsl')
        copy.set('todir', '${jmeter.result.html.dir}')
        fileset.set('dir', '${jmeter.home}/extras')
        for i in includeList:
            include = xee.SubElement(fileset,"include")
            include.set('name',i['name'])
xmlFile = xee.ElementTree(Project)

'''
xml_declaration:xml头补，默认为False
pretty_print:编辑，默认为False
'''
xee.dump(Project)
xmlFile.write('jmeterTest_etree.xml', encoding='utf-8', method='xml',xml_declaration=True,pretty_print=True)