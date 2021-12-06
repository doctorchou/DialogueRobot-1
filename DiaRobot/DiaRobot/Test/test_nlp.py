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
        self.assertEqual(self.pre.navi_location, "三食堂")

        #case 2
        self.pre.msg = "去学院三"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.navi)
        self.assertEqual(self.pre.navi_location, "学院三")

        #case 3
        self.pre.msg = "去"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.navi)
        self.assertEqual(self.pre.navi_location, "未知")

    def test_msg_process_query(self):
        #case 1
        self.pre.msg = "今天校园天气如何？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.que)
        self.assertEqual(self.pre.query_type, "天气")
        self.assertEqual(self.pre.query_location, "校园")
        
        #case 2
        self.pre.msg = "今年的校历？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.que)
        self.assertEqual(self.pre.query_type, "校历")

    def test_msg_process_recommend(self):
        #case 1
        self.pre.msg = "最近学校内有什么校级活动吗？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.recom)
        self.assertEqual(self.pre.recommend_type, "校级")
        self.assertEqual(self.pre.recommend_name, "所有")

        #case 2
        self.pre.msg = "计算机学院最近要组织什么活动吗？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.recom)
        self.assertEqual(self.pre.recommend_type, "院级")
        self.assertEqual(self.pre.recommend_name, "计算机")

        #case 3
        self.pre.msg = "最近学校内有什么活动可以推荐一下吗？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.recom)
        self.assertEqual(self.pre.recommend_type, "所有")
        self.assertEqual(self.pre.recommend_name, "所有")

    def test_msg_process_reserve(self):
        #case 1
        self.pre.msg = "帮我预约羽毛球馆"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.reser)
        self.assertEqual(self.pre.reserve_location, "羽毛球馆")

    def test_msg_process_unclear(self):
        #case 1
        self.pre.msg = "你能陪我聊聊天吗？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.unclear)

        #case2
        self.pre.msg = "今年的生肖是什么？"
        self.pre.MsgProcess()
        self.assertEqual(self.pre.status, Status.unclear)
        
    
