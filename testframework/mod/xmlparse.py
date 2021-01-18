
try:
    import xml.etree.ElementTree as ET
except:
    import xml.etree.cElementTree as ET

class XMLParse:

    def __init__(self, filename=None):
        self.filename = filename

    def parse(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()

        suite_list = []
        for cur_suite in root:
            suite_name, nb_loop, retry_on_failure = self.get_suite_attr(cur_suite)
            testcase_list = []
            for cur_testcase in cur_suite:
                tc_name = self.get_testcase_attr(cur_testcase) + '.py'
                testcase_list.append(tc_name)

            suite_list.append({'suite_name': suite_name, 'nb_loop': nb_loop, 'retry_on_failure': retry_on_failure, 'testcase_list': testcase_list})

        return suite_list

    def get_suite_attr(self, cur_suite):
        try:
            suite_name = cur_suite.attrib['name']
        except:
            suite_name = 'invalid suite name'

        try:
            nb_loop = cur_suite.attrib['nb_loop']
        except:
            nb_loop = 1

        try:
            retry_on_failure = cur_suite.attrib['retry_on_failure']
        except:
            retry_on_failure = False

        return (suite_name, nb_loop, retry_on_failure)

    def get_testcase_attr(self, cur_testcase):
        try:
            tc_name = cur_testcase.text.strip()
        except:
            tc_name = 'invalid testcase name'

        return tc_name

    def get_all_files(self):
        test_files = []
        tests_files = {}
        all_info = self.parse()
        for x in all_info:
            for test_name in x['testcase_list']:
                test_files.append(test_name.split('/')[(-1)])
                tests_files[test_name] = test_name.split('/')[(-1)]

        print tests_files.keys()
        return tests_files


if __name__ == '__main__':
    xmlparse = XMLParse('campaign_OTA_simulation.xml')
    res1 = xmlparse.get_all_files()
    print(res1)

