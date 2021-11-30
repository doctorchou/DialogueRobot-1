from django.test import TestCase
from DiaRobot.Robot.nlp import Preprocess
from DiaRobot.Robot.nlp import Status

class NLPTestCase(TestCase):
    def setUp(self):
        super(NLPTestCase, self).setUp()
        self.pre = Preprocess("")

    def test_msg_process_navigation(self):
        #case 1
        self.pre.msg = "请问三食堂怎么走？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.navi)

        #case 2
        self.pre.msg = "去学院三"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.navi)

    def test_demand_process_navigation(self):
        #case 1
        self.pre.msg = "去学院三"
        
    
