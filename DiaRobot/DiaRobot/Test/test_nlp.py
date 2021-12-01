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
        self.assertEqual(self.pre.location, "三食堂")

        #case 2
        self.pre.msg = "去学院三"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.navi)
        self.assertEqual(self.pre.location, "学院三")

        #case 3
        self.pre.msg = "去"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.navi)

    def test_msg_process_query(self):
        pass

    def test_msg_process_recommend(self):
        pass

    def test_msg_process_reserve(self):
        pass

    def test_msg_process_unclear(self):
        #case 1
        self.pre.msg = "你能陪我聊聊天吗？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.unclear)

        #case2
        self.pre.msg = "今年的生肖是什么？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.unclear)
        
    
