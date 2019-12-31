import xml.dom.minidom as xdm

doc = xdm.Document()

Project = doc.createElement("project")
Project.setAttribute('name','ant-jmeter-test')
Project.setAttribute('default','all')
Project.setAttribute('basedir','.')

doc.appendChild(Project)

Tstamp = doc.createElement('tstamp')
Format = doc.createElement('format')
Format.setAttribute('property','time')
Format.setAttribute('pattern','yyyy/MM/dd/hh/mm')
Tstamp.appendChild(Format)
Project.appendChild(Tstamp)

propertylist = [{'name':'jmeter.home','value':'E:\\apache-jmeter-5.1'},
                {'name':'jmeter.result.jtl.dir','value':'E:\\BigData\\Hive\\jtl'},
                {'name':'jmeter.result.html.dir','value':'E:\\BigData\\Hive\\html'},
                {'name':'ReportName','value':'TestReport'},
                {'name':'jmeter.result.jtlName','value':'${jmeter.result.jtl.dir}/${ReportName}.jtl'},
                {'name':'jmeter.result.htmlName','value':'${jmeter.result.html.dir}/${ReportName}.html'}]

for p in propertylist:
    Property = doc.createElement("property")
    Property.setAttribute('name',p['name'])
    Property.setAttribute('value',p['value'])
    Project.appendChild(Property)

targetList = [{'name':'all'},
              {'name':'test'},
              {'name':'report'}]

antcallList = [{'target':'test'},
           {'target':'report'}]

includeList = [{'name':'collapse.png'},
               {'name':'expand.png'}]

for t in targetList:
    Target = doc.createElement("target")
    Target.setAttribute('name',t['name'])
    if t['name']=='all':
        for a in antcallList:
            antcall = doc.createElement("antcall")
            antcall.setAttribute('target',a['target'])
            Target.appendChild(antcall)
    elif t['name']=='test':
        taskdef = doc.createElement("taskdef")
        jmeter = doc.createElement("jmeter")
        testplans = doc.createElement("testplans")
        taskdef.setAttribute('name', 'jmeter')
        taskdef.setAttribute('classname', 'org.programmerplanet.ant.taskdefs.jmeter.JMeterTask')
        jmeter.setAttribute('jmeterhome', '${jmeter.home}')
        jmeter.setAttribute('resultlog', '${jmeter.result.jtlName}')
        testplans.setAttribute('dir', '/Users/yq519/Documents/jmeter/')
        testplans.setAttribute('includes', '*.jmx')
        Target.appendChild(taskdef)
        Target.appendChild(jmeter)
        jmeter.appendChild(testplans)
    elif t['name']=='report':
        xslt = doc.createElement("xslt")
        copy = doc.createElement("copy")
        fileset = doc.createElement("fileset")
        xslt.setAttribute('in', '${jmeter.result.jtlName}')
        xslt.setAttribute('out', '${jmeter.result.htmlName}')
        xslt.setAttribute('style', '${jmeter.home}/extras/jmeter-results-detail-report_21.xsl')
        copy.setAttribute('todir', '${jmeter.result.html.dir}')
        fileset.setAttribute('dir', '${jmeter.home}/extras')
        for i in includeList:
            include = doc.createElement("include")
            include.setAttribute('name',i['name'])
            fileset.appendChild(include)
        Target.appendChild(xslt)
        Target.appendChild(copy)
        copy.appendChild(fileset)

    Project.appendChild(Target)

xmlFile = open('jmeterTest_dom.xml','w')
doc.writexml(xmlFile, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
